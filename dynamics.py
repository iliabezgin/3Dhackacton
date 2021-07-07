import sys
import IMP
import IMP.atom
import IMP.algebra
import IMP.rmf
import IMP.core
import IMP.container
import IMP.display
import IMP.npctransport
import RMF
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm


sys.path.append('/usr/lib/python3.6/dist-packages')

from dataclasses import dataclass

@dataclass  # https://docs.python.org/3/library/dataclasses.html
class ProteinChain:
    """
    A string-of-beads representation of a protein chain
    from specified beads. The beads are connected by a restraint
    (think springs between consecutive beads)
    """
    # the "parent" of all beads in the chain
    root_p: IMP.Particle
    # the list of bead particles comprising the chain
    beads: list
    # a spring restraint on consecutive beads
    restraint: IMP.Restraint
    # The protein sequence that this chain represents
    sequence: str

    def __post_init__(
            self):  # this is called by automatically generated __init__
        # make sure root is the parent of all beads
        for bead in self.beads:
            assert IMP.atom.Hierarchy(bead).get_parent() == self.root_as_h

    @property
    def model(self) -> IMP.Model:
        return self.root_p.get_model()

    @property  # Hierarchy is a decorator
    def root_as_h(self) -> IMP.atom.Hierarchy:
        return IMP.atom.Hierarchy(self.root_p)



FAKE_MASS = 1.0


class ProteinChainFactory:
    """
    A class for generating chains of beads
    """
    def __init__(self,
                 model: IMP.Model,
                 # bead radius in angstroms (10^-10 m)
                 default_radius_A: float = 10.0,
                 # distance between bead centers, relative to radius
                 relative_rest_distance: float = 2.0,
                 # force coefficient for spring connecting consecutive beads in kcal/mol/A^2 (force is k*distance)
                 k_in: float = 1.0,
                 # number of residues per bead in the string-of-beads
                 nres_per_bead: int = 5,
                 # interaction strength between beads and bounding sphere
                 kbs: float = 0.1,
                 # bounding sphere radius
                 sphere_radius: float = 100,
                 # inter strings interaction strength
                 k_out: float = 1.0
                 ):
        """
        :param model
        :param default_radius_A       Bead radius in angstroms
        :param relative_rest_distance Distance between bead centers, relative to radius
        :param k_kcal_per_mol_per_A2  Force coefficient for spring connecting consecutive beads
                                      in kcal/mol/A^2 units
        :param nres_per_bead          Number of protein residues represented by a single bead
        """
        self._model = model
        self._default_radius_A = default_radius_A
        self._rest_distance_A = relative_rest_distance * default_radius_A
        self._k_in = k_in
        self._k_out = k_out
        self._nres_per_bead = nres_per_bead
        self._kbs = kbs
        self._sphere_radius = sphere_radius
        self.s = IMP.algebra.Sphere3D(IMP.algebra.Vector3D(0, 0, 0), self._sphere_radius)
        self.init_locations = []

    @property
    def model(self): return self._model

    @property
    def default_radius_A(self): return self._default_radius_A

    @property
    def rest_distance_A(self): return self._rest_distance_A

    @property
    def k_in(self): return self._k_in

    @property
    def k_out(self): return self._k_out

    @property
    def nres_per_bead(self): return self._nres_per_bead

    def _create_bead(self,
                     name: str,
                     init_coord: IMP.algebra.Vector3D = None):
        p = IMP.Particle(self.model, name)
        p_as_xyzr = IMP.core.XYZR.setup_particle(
            p)  # A Decorator design pattern - adding functionality to an object at run time (~run-time inheritance)
        if init_coord is not None:
            p_as_xyzr.set_coordinates(init_coord)
        p_as_xyzr.set_coordinates_are_optimized(True)
        p_as_xyzr.set_radius(self.default_radius_A)
        IMP.atom.Mass.setup_particle(p, FAKE_MASS)  # required by Hierarchy
        IMP.atom.Diffusion.setup_particle(p)
        IMP.atom.Hierarchy.setup_particle(
            p)  # allow inclusion in IMP hierarchies
        IMP.display.Colored.setup_particle(p,
                                           IMP.display.get_display_color(0))
        return p

    def _create_restraint(self,
                          beads  # spring constant
                          ):
        hdps = IMP.core.HarmonicDistancePairScore(self.rest_distance_A,
                                                  self.k_in)
        cpc = IMP.container.ConsecutivePairContainer(self.model,
                                                     beads)  # convention - use abbreviation for multiword class names
        pr = IMP.container.PairsRestraint(hdps, cpc)
        return pr, hdps

    def get_interchain_restraint(self, chain0: ProteinChain,
                                 chain1: ProteinChain):
        """
        Returns interchain restraint
        """
        center_A = 5
        threshold_A = 10
        thb = IMP.core.TruncatedHarmonicBound(center_A,
                                              self.k_out,
                                              threshold_A)
        dps = IMP.core.DistancePairScore(thb)
        pr = IMP.core.PairRestraint(chain0.model,
                                    dps,
                                    [chain0.beads[2], chain1.beads[2]])
        return pr

    def get_bounding_sphere_restraint(self, beads):
        """
        Returns bounding sphere restraint
        """
        f = IMP.core.HarmonicUpperBound(0, self._kbs) # mean = 0, k = 0.1 (k_kcal_per_mol_per_A2)
        bsss = IMP.core.BoundingSphere3DSingletonScore(f, self.s)
        r = IMP.container.SingletonsRestraint(bsss, beads)
        return r

    def create(self,
               sequence: str,  # protein sequence
               name: str,
               in_center: bool):  # a name of your choice for the protein chain
        p = IMP.Particle(self.model, name)
        p_as_h = IMP.atom.Hierarchy.setup_particle(
            p)  # allow inclusion in IMP hierarchies
        # add beads:
        n = len(sequence)
        nbeads = max(1, round(n / self.nres_per_bead))
        beads = []
        init_location = None
        if not in_center:
            init_location = self.get_free_location_in_sphere(self.init_locations)
        for i in range(nbeads):
            bead = self._create_bead(f"{name}_{i}", init_coord=init_location)
            p_as_h.add_child(bead)
            beads.append(bead)
        # restrain beads on a "string":
        restraint, harmonic_distance_pair_score = self._create_restraint(beads)

        return ProteinChain(root_p=p,
                            beads=beads,
                            restraint=restraint,
                            sequence=sequence)

    def get_free_location_in_sphere(self, ready_locations: [IMP.algebra.Vector3D]):
        new_location = IMP.algebra.get_random_vector_in(IMP.algebra.Sphere3D(IMP.algebra.Vector3D(0, 0, 0), self._sphere_radius/2))
        while not self.check_locations_collision(new_location, ready_locations, self.default_radius_A * 2):
            new_location = IMP.algebra.get_random_vector_in(self.s)
        return new_location

    def check_locations_collision(self,
                                  location_to_check: IMP.algebra.Vector3D,
                                  ready_locations: [IMP.algebra.Vector3D],
                                  threshold: float):
        for ready_location in ready_locations:
            if IMP.algebra.get_distance(location_to_check, ready_location) < threshold:
                return False
        return True
