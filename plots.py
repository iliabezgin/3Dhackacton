from main_model import *
from dynamics import *

import math
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd


def generate_heatmap(data, labels_dict, file_title, plot_title):
    """
    method to generate heatmap with name file title of the given data
    """

    fig = plt.figure()
    ax = sn.heatmap(data,
                    linewidths=0.3)
    figure = ax.get_figure()

    if labels_dict:
        ax.set_xlabel(labels_dict["x"])
        ax.set_ylabel(labels_dict["y"])
    if plot_title:
        ax.set_title(plot_title)

    figure.savefig(file_title)


def generate_history_plot(data, labels_dict, file_title, plot_title):
    fig = plt.figure()
    ax = sns.histplot(data)

    if labels_dict:
        ax.set_xlabel(labels_dict["x"])
    if plot_title:
        ax.set_title(plot_title)

    plt.legend()
    plt.savefig(file_title)


def generate_2D_scatter_plot(x, y, labels_dict, file_title, plot_title):
    """
    method to generate 2D scatter plot
    """
    fig = plt.figure()
    plt.scatter(x, y)

    if labels_dict:
        plt.xlabel(labels_dict["x"])
        plt.ylabel(labels_dict["y"])
    if plot_title:
        plt.title(plot_title)

    plt.legend()
    plt.savefig(file_title)


def generate_3D_scatter_plot(x, y, z, labels_dict, file_title, plot_title):
    """
    method to generate 3D scatter plot
    """
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z,
               marker=".")

    if labels_dict:
        ax.set_xlabel(labels_dict["x"])
        ax.set_ylabel(labels_dict["y"])
        ax.set_zlabel(labels_dict["z"])
    if plot_title:
        ax.set_title(plot_title)

    plt.legend()
    plt.savefig(file_title)


def generate_2D_N_plots(x, y, labels_dict, file_title, plot_title, no_start):
    """
    generate 2d plot with several plots on it
    """

    fig = plt.figure()

    for sub_y in y:
        sub_y = sub_y[no_start]
        plt.plot(x, sub_y)

    if labels_dict:
        plt.xlabel(labels_dict["x"])
        plt.ylabel(labels_dict["y"])
    if plot_title:
        plt.title(plot_title)

    plt.legend()
    plt.savefig(file_title)


def generate_2D_plot(x, y, labels_dict, file_title, plot_title):
    """
    generate simple 2d plot
    """
    fig = plt.figure()
    plt.plot(x, y)

    if labels_dict:
        plt.xlabel(labels_dict["x"])
        plt.ylabel(labels_dict["y"])
    if plot_title:
        plt.title(plot_title)

    plt.legend()
    plt.savefig(file_title)


def simulation_energy_over_time(E, T_ns, T_ns_threshold):
    """
    method to create function of energy as a function of time
    """
    no_start = (T_ns > T_ns_threshold)
    # (x, y, labels_dict, file_title, plot_title)
    generate_2D_plot(T_ns[no_start], E[no_start],
                     {'x': r'time [$ns$]',
                      'y': r'E [$kcal/mol/A^2$]'},
                     "energy_graph",
                     "Energy(time) graph")


def end_to_end_distances_over_time(D, T_ns, T_ns_threshold):
    """
    method to create plot of distances of end to end as
    a function of time
    """
    no_start = (T_ns > T_ns_threshold)
    # (x, y, labels_dict, file_title, plot_title)
    generate_2D_N_plots(T_ns[no_start], D,
                        {'x': r'time [$ns$]',
                         'y': r'end-to-end distance [$A$]'},
                        "distances_graph",
                        "end to end Distances(time) graph",
                        no_start)


def distribution_of_energy_over_time(E, T_ns, T_ns_threshold):
    """
    method to create plot of distribution of energy over time
    """
    no_start = (T_ns > T_ns_threshold)
    generate_history_plot(E[no_start],
                          {"x": r'energy [$kcal^{-1}mol^{-1}A^2$]'},
                          "dist_of_E",
                          "distribution of Energy history plot")


def distribution_of_dist_over_time(D):
    D_concat = np.concatenate(D[0:])
    generate_history_plot(D_concat,
                          {"x": r'N''-C'' distance [A]'},
                          "dist_of_D",
                          "distribution of Distances history plot")


def distribution_of_beads_locations(iter_chains, T_ns, T_ns_threshold):
    """
    get distribution of center masses of chains as a function of iterations
    """
    # each value inside centers is an array, for current iteration
    # each array contains all centers of frame, per the current iteration
    # centers = C[i][j] -> center of j'th chain in i'th iteration
    no_start = (T_ns > T_ns_threshold)
    vars = []
    centers = [[calculate_center_of_mass(chain) for chain in
                chains_on_cur_iteration] for
               chains_on_cur_iteration in iter_chains]
    for cen in centers:
        iteration_var = np.var(np.array(cen))
        vars.append(iteration_var)

    # the plot itself
    generate_2D_plot(T_ns[no_start], vars,
                     {'x': r'time [$ns$]',
                      'y': r'variance of center of mass'},
                     "variance_of_centers",
                     "Var(time) graph")


# functions for new plots


def calculate_distance_in_xyz(vector):
    """
    distance of vector from (0,0,0)
    """
    x, y, z = vector[0], vector[1], vector[2]
    x, y, z = x ** 2, y ** 2, z ** 2
    return math.sqrt(x + y + z)


def calculate_center_of_mass(chain):
    """
    calculate center of mass of current chain position
    """
    D = IMP.algebra.Vector3D(0, 0, 0)
    M = 0
    for bead in chain.beads:
        bead_mass = bead.get_mass()
        coords = bead.get_coordinates()
        D += coords
        M += bead_mass
    return calculate_distance_in_xyz(D / M)
