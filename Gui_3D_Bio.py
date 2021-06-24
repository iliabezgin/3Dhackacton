from tkinter import *
import tkinter as tk

import main_model
import plots
from PIL import ImageTk, Image


def quit_program():
    quit()


def pop_up_plot_window(path):
    window = tk.Toplevel()
    window.wm_title("Plot")
    window.configure(background='grey')

    img = ImageTk.PhotoImage(Image.open(path))
    image_label = Label(window, image=img)
    image_label.photo = img
    image_label.pack()


class Gui_3D_Bio:
    def __init__(self, root):
        self._root = root
        self._titleFrame = Frame(root, width=800, height=50,
                                 bg='light blue')
        self._leftButtonsFrame = Frame(root, width=15, height=750,
                                       bg='light blue')
        self._rightButtonsFrame = Frame(root, width=15, height=750,
                                        bg='light blue')
        self._middleTopFrame = Frame(root, width=770, height=130,
                                     bg='light blue')
        self._middleBottomFrame = Frame(root, width=770, height=650,
                                        bg='grey93')
        self._lowBorder = Frame(root, width=800, height=70, bg='light blue')
        self._lowBorder.pack(side='bottom')
        self._givenSequence = tk.StringVar()
        self._firstCheckBoxStatus = tk.IntVar()
        self._secondCheckBoxStatus = tk.IntVar()
        self._thirdCheckBoxStatus = tk.IntVar()
        self._fourthCheckBoxStatus = tk.IntVar()
        self._fifthCheckBoxStatus = tk.IntVar()
        self._randomInitCheckBoxStatus = tk.IntVar()
        self._diffChainsCheckBoxStatus = tk.IntVar()
        self._kInSize = tk.IntVar()
        self._kOutSize = tk.IntVar()
        self._beadRadiusSize = tk.IntVar()
        self._sphereRadiusSize = tk.IntVar()
        self._kbsValue = tk.IntVar()
        self._locationToSave = tk.StringVar()
        self._chainsNumber = tk.IntVar()
        self._aminoAmount = tk.IntVar()
        self._lightMode = True
        self._allButton = []
        self._allEntry = []
        self._allLabels = []
        self._allLabelFrames = []
        self._informativeLabels = []
        self._allCheckBoxes = []

    def labelCreateAndPack(self, frame, side, text, font, bg, fg):
        title = Label(frame, text=text, font=font, bg=bg, fg=fg)
        title.pack(side=side)
        return title

    def buttonCreateAndPack(self, frame, text, height, width, font, bg, command, side):
        button = Button(frame,
                        text=text,
                        height=height,
                        width=width, font=font,
                        bg=bg,
                        command=command)
        button.pack(side=side)
        self._allButton.append(button)
        return button

    def labelFrameCreation(self, frame, text, fg, bg, font, side, padx, pady):
        labelFrame = LabelFrame(frame, text=text, fg=fg, bg=bg, font=font)
        self._allLabelFrames.append(labelFrame)
        labelFrame.pack(side=side, padx=padx, pady=pady)

        return labelFrame

    def spaceCreation(self, frame, amount, side, bg):
        for index in range(amount):
            space = Label(frame, text="", bg=bg)
            space.pack(side=side)
            self._allLabels.append(space)

    def titleCreation(self):
        title = self.labelCreateAndPack(self._titleFrame, 'top', 'Membraneless Organelles Final Project',
                                        ("Linux Libertine Mono O", 15, 'bold'), 'light blue', 'black')
        self._allLabels.append(title)

    def mainFramesInit(self):
        self._titleFrame.pack(side='top', fill='both')
        self._leftButtonsFrame.pack(side='left', fill='both')
        self._rightButtonsFrame.pack(side="right", fill='both')
        self._middleTopFrame.pack(fill='both')
        self._middleBottomFrame.pack(side='top', fill='both')

        self.titleCreation()

    def changeModeButton(self):
        self.spaceCreation(self._leftButtonsFrame, 2, 'top', 'light blue')

        self.buttonCreateAndPack(self._leftButtonsFrame, 'Dark/Light Mode', 1, 15, ("Ariel", 10, 'bold'), 'white',
                                 lambda: self.dark_light_switch(), 'top')

        self.spaceCreation(self._leftButtonsFrame, 3, 'top', 'light blue')

        self.buttonCreateAndPack(self._leftButtonsFrame, 'Exit', 1, 15, ("Ariel", 10, 'bold'), 'white',
                                 lambda: quit(), 'top')

    def gridEntry(self):
        entryLabelFrame = LabelFrame(self._middleTopFrame,
                                     text='Program Input',
                                     fg='black', bg='light blue',
                                     font=("Ariel", 10, 'normal'))
        self._allLabelFrames.append(entryLabelFrame)
        entryLabelFrame.pack(side='left', padx=7, pady=7)
        entryLabel = Label(entryLabelFrame, text='Enter Sequence:',
                           bg='light blue',
                           fg='black', font=("Ariel", 9, 'bold'))
        self._allLabels.append(entryLabel)
        entryPlace = Entry(entryLabelFrame,
                           textvariable=self._givenSequence, bd=2)
        self._allEntry.append(entryPlace)
        submitButton = Button(entryLabelFrame, text='Start Simulation',
                              height=1,
                              width=15, font=("Ariel", 10, 'bold'), bg='white',
                              command=lambda: self.submit_input())
        self._allButton.append(submitButton)

        entryLabel.pack(side='top')
        entryPlace.pack(side='top')

        for index in range(1):
            space = Label(entryLabelFrame, text="", bg='light blue')
            space.pack(side='top')
            self._allLabels.append(space)

        submitButton.pack(side='top')

    def check_validity(self):

        if self._kInSize.get() < 0:
            return False
        if self._kOutSize.get() < 0:
            return False
        if self._beadRadiusSize.get() < 0:
            return False
        if self._sphereRadiusSize.get() < 0:
            return False
        if self._kbsValue.get() < 0:
            return False
        if self._chainsNumber.get() < 0:
            return False
        if self._aminoAmount.get() < 0:
            return False
        return True

    def submit_input(self):
        random_init_flag = False
        random_diff_type = False

        for label in self._informativeLabels:
            label.pack_forget()

        if not self.check_validity():
            invalidInputLabel = Label(self._middleBottomFrame,
                                      text='Invalid Input Given. Hint: Negative Argument',
                                      fg='blue', bg='grey93', font=("Ariel", 10, 'normal'))
            invalidInputLabel.pack(side='top')
            self._informativeLabels.append(invalidInputLabel)
            return

        simulationRunLabel = Label(self._middleBottomFrame,
                                   text='Running Simulation!',
                                   fg='blue', bg='grey93', font=("Ariel", 10, 'normal'))
        simulationRunLabel.pack(side='top')
        self._informativeLabels.append(simulationRunLabel)

        if self._randomInitCheckBoxStatus.get() == 1:
            random_init_flag = True

        if self._diffChainsCheckBoxStatus.get() == 1:
            random_diff_type = True

        T_ns, E, D, chains_on_iteration = main_model.create_model(self._givenSequence.get(), self._chainsNumber.get(),
                                                                  self._locationToSave.get(),
                                                                  self._beadRadiusSize.get(),
                                                                  self._sphereRadiusSize.get(),
                                                                  self._kbsValue.get(), self._aminoAmount.get(),
                                                                  self._kInSize.get(), self._kOutSize.get(),
                                                                  random_init_flag, random_diff_type)

        if self._firstCheckBoxStatus.get() == 1:
            firstPlotLabel = Label(self._middleBottomFrame,
                                   text='Generating Energy Over Time Plot...',
                                   fg='blue', bg='grey93', font=("Ariel", 9, 'normal'))
            firstPlotLabel.pack(side='top')
            self._informativeLabels.append(firstPlotLabel)
            plots.simulation_energy_over_time(E, T_ns, 1)
            pop_up_plot_window("energy_graph.png")

        if self._secondCheckBoxStatus.get() == 1:
            secondPlotLabel = Label(self._middleBottomFrame,
                                    text='Generating End To End Over Time Plot...',
                                    fg='blue', bg='grey93', font=("Ariel", 9, 'normal'))
            secondPlotLabel.pack(side='top')
            self._informativeLabels.append(secondPlotLabel)
            plots.end_to_end_distances_over_time(D, T_ns, 1)
            pop_up_plot_window("distances_graph.png")

        if self._thirdCheckBoxStatus.get() == 1:
            thirdPlotLabel = Label(self._middleBottomFrame,
                                   text='Generating Distribution Of Energy Over Time Plot...',
                                   fg='blue', bg='grey93', font=("Ariel", 9, 'normal'))
            thirdPlotLabel.pack(side='top')
            self._informativeLabels.append(thirdPlotLabel)
            plots.distribution_of_energy_over_time(E, T_ns, 1)
            pop_up_plot_window("dist_of_E.png")

        if self._fourthCheckBoxStatus.get() == 1:
            fourthPlotLabel = Label(self._middleBottomFrame,
                                    text='Generating Distribution Of Distances Over Time Plot...',
                                    fg='blue', bg='grey93', font=("Ariel", 9, 'normal'))
            fourthPlotLabel.pack(side='top')
            self._informativeLabels.append(fourthPlotLabel)
            plots.distribution_of_dist_over_time(D)
            pop_up_plot_window("dist_of_D.png")

        if self._fifthCheckBoxStatus.get() == 1:
            fifthPlotLabel = Label(self._middleBottomFrame,
                                   text='Generating Distribution Of Bead Locations...',
                                   fg='blue', bg='grey93', font=("Ariel", 9, 'normal'))
            fifthPlotLabel.pack(side='top')
            self._informativeLabels.append(fifthPlotLabel)
            plots.distribution_of_beads_locations(chains_on_iteration, T_ns, 1)
            pop_up_plot_window("variance_of_centers.png")

        endOfRunLabel = Label(self._middleBottomFrame,
                              text='Simulating is Over, Check Out Your Plots',
                              fg='blue', bg='grey93', font=("Ariel", 10, 'normal'))
        endOfRunLabel.pack(side='top')
        self._informativeLabels.append(endOfRunLabel)

    def dark_light_switch(self):

        if self._lightMode:
            self._titleFrame.configure(background='gray20')
            self._leftButtonsFrame.configure(background='gray20')
            self._rightButtonsFrame.configure(background='gray20')
            self._middleTopFrame.configure(background='gray20')
            self._lowBorder.configure(background='gray20')
            for label in self._allLabels:
                label.config(bg='gray20')
                label.config(fg='white')

            for button in self._allButton:
                button.config(bg='black')
                button.config(fg='white')

            for labelFrame in self._allLabelFrames:
                labelFrame.config(bg='gray20')
                labelFrame['fg'] = 'white'

            for checkBox in self._allCheckBoxes:
                checkBox.config(bg='gray20')

            self._lightMode = False
        else:
            self._titleFrame.configure(background='light blue')
            self._leftButtonsFrame.configure(background='light blue')
            self._rightButtonsFrame.configure(background='light blue')
            self._middleTopFrame.configure(background='light blue')
            self._lowBorder.configure(background='light blue')

            for label in self._allLabels:
                label.config(bg='light blue')
                label.config(fg='black')

            for button in self._allButton:
                button.config(bg='white')
                button.config(fg='black')

            for labelFrame in self._allLabelFrames:
                labelFrame.config(bg='light blue')
                labelFrame['fg'] = 'black'

            for checkBox in self._allCheckBoxes:
                checkBox.config(bg='light blue')

            self._lightMode = True

    def grid_plot_checkboxes(self):

        plot_label = Label(self._rightButtonsFrame, text='Select Your Plots:',
                           bg='light blue')
        plot_label.pack(side='top')
        self._allLabels.append(plot_label)

        for index in range(1):
            space = Label(self._rightButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self._allLabels.append(space)

        firstCheckBox = Checkbutton(self._rightButtonsFrame, text='Energy Over Time',
                                    variable=self._firstCheckBoxStatus,
                                    bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        firstCheckBox.pack(side='top')
        self._allCheckBoxes.append(firstCheckBox)

        secondCheckBox = Checkbutton(self._rightButtonsFrame,
                                     text='End to End Distances',
                                     variable=self._secondCheckBoxStatus,
                                     bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        secondCheckBox.pack(side='top')
        self._allCheckBoxes.append(secondCheckBox)

        thirdCheckBox = Checkbutton(self._rightButtonsFrame,
                                    text='Energy Distribution',
                                    variable=self._thirdCheckBoxStatus,
                                    bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        thirdCheckBox.pack(side='top')
        self._allCheckBoxes.append(thirdCheckBox)

        fourthCheckBox = Checkbutton(self._rightButtonsFrame,
                                     text='Location Distribution',
                                     variable=self._fourthCheckBoxStatus,
                                     bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        fourthCheckBox.pack(side='top')
        self._allCheckBoxes.append(fourthCheckBox)

        fifthCheckBox = Checkbutton(self._rightButtonsFrame,
                                    text='Beads Location',
                                    variable=self._fifthCheckBoxStatus,
                                    bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        fifthCheckBox.pack(side='top')
        self._allCheckBoxes.append(fifthCheckBox)

    def grid_scales(self):
        k_in_LabelFrame = LabelFrame(self._middleTopFrame,
                                     text='Argument 1:',
                                     fg='black', bg='light blue',
                                     font=("Ariel", 10, 'normal'))
        self._allLabelFrames.append(k_in_LabelFrame)

        k_out_LabelFrame = LabelFrame(self._middleTopFrame,
                                      text='Argument 2:',
                                      fg='black', bg='light blue',
                                      font=("Ariel", 10, 'normal'))
        self._allLabelFrames.append(k_out_LabelFrame)

        k_in_LabelFrame.pack(side='left')
        k_out_LabelFrame.pack(side='left')

        k_in_label = Label(k_in_LabelFrame, text="K-In:",
                           bg='light blue', fg='black', font=("Ariel", 9, 'bold'))
        k_in_scale = Entry(k_in_LabelFrame,
                           textvariable=self._kInSize, bd=2)
        k_in_label.pack(side='left')
        k_in_scale.pack(side='left')
        self._allLabels.append(k_in_label)

        k_out_label = Label(k_out_LabelFrame,
                            text="K-Out:", bg='light blue',
                            fg='black', font=("Ariel", 9, 'bold'))

        k_out_scale = Entry(k_out_LabelFrame,
                            textvariable=self._kOutSize, bd=2)
        k_out_label.pack(side='left')
        k_out_scale.pack(side='left')
        self._allLabels.append(k_out_label)

        self._allEntry.append(k_in_scale)
        self._allEntry.append(k_out_scale)

    def grid_left_side_widgets(self):
        entryLabelFrame = LabelFrame(self._leftButtonsFrame,
                                     text='Output Save Location',
                                     fg='black', bg='light blue',
                                     font=("Ariel", 10, 'normal'))
        self._allLabelFrames.append(entryLabelFrame)
        entryLabel = Label(entryLabelFrame, text='Enter Name For RMF:',
                           bg='light blue',
                           fg='black', font=("Ariel", 9, 'bold'))
        self._allLabels.append(entryLabel)
        entryPlace = Entry(entryLabelFrame,
                           textvariable=self._locationToSave, bd=2)
        self._allEntry.append(entryPlace)

        entryLabelFrame.pack(side='top', padx=7, pady=7)
        entryLabel.pack(side='top')
        entryPlace.pack(side='top')

        for index in range(1):
            space = Label(self._leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self._allLabels.append(space)

        bead_radius_LabelFrame = LabelFrame(self._leftButtonsFrame,
                                            text='Argument 3:',
                                            fg='black', bg='light blue',
                                            font=("Ariel", 10, 'normal'))
        self._allLabelFrames.append(bead_radius_LabelFrame)

        bead_radius_LabelFrame.pack(side='top')

        bead_radius_label = Label(bead_radius_LabelFrame,
                                  text="Enter Bead Radius:", bg='light blue',
                                  fg='black', font=("Ariel", 9, 'bold'))

        bead_radius_entry = Entry(bead_radius_LabelFrame,
                                  textvariable=self._beadRadiusSize, bd=2)

        bead_radius_label.pack()
        bead_radius_entry.pack()
        self._allLabels.append(bead_radius_label)
        self._allEntry.append(bead_radius_entry)

        for index in range(1):
            space = Label(self._leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self._allLabels.append(space)

        sphere_radius_LabelFrame = LabelFrame(self._leftButtonsFrame,
                                              text='Argument 4:',
                                              fg='black', bg='light blue',
                                              font=("Ariel", 10, 'normal'))
        self._allLabelFrames.append(sphere_radius_LabelFrame)

        sphere_radius_LabelFrame.pack(side='top')

        sphere_radius_label = Label(sphere_radius_LabelFrame,
                                    text="Enter Sphere Radius:", bg='light blue',
                                    fg='black', font=("Ariel", 9, 'bold'))

        sphere_radius_scale = Entry(sphere_radius_LabelFrame,
                                    textvariable=self._sphereRadiusSize, bd=2)
        sphere_radius_label.pack()
        sphere_radius_scale.pack()
        self._allLabels.append(sphere_radius_label)
        self._allEntry.append(sphere_radius_scale)

        for index in range(1):
            space = Label(self._leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self._allLabels.append(space)

        kbs_LabelFrame = LabelFrame(self._leftButtonsFrame,
                                    text='Argument 5:',
                                    fg='black', bg='light blue',
                                    font=("Ariel", 10, 'normal'))
        self._allLabelFrames.append(kbs_LabelFrame)

        kbs_LabelFrame.pack(side='top')

        kbs_label = Label(kbs_LabelFrame,
                          text="Enter KBS:", bg='light blue',
                          fg='black', font=("Ariel", 9, 'bold'))

        kbs_scale = Entry(kbs_LabelFrame,
                          textvariable=self._kbsValue, bd=2)
        kbs_label.pack()
        kbs_scale.pack()
        self._allLabels.append(kbs_label)
        self._allEntry.append(kbs_scale)

        for index in range(1):
            space = Label(self._leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self._allLabels.append(space)

        chains_number_LabelFrame = LabelFrame(self._leftButtonsFrame,
                                              text='Argument 6:',
                                              fg='black', bg='light blue',
                                              font=("Ariel", 10, 'normal'))
        self._allLabelFrames.append(chains_number_LabelFrame)

        chains_number_LabelFrame.pack(side='top')

        chainsNumber_label = Label(chains_number_LabelFrame,
                                   text="Enter Number Of Chains:", bg='light blue',
                                   fg='black', font=("Ariel", 9, 'bold'))

        chains_number_scale = Entry(chains_number_LabelFrame,
                                    textvariable=self._chainsNumber, bd=2)
        chainsNumber_label.pack()
        chains_number_scale.pack()
        self._allLabels.append(chainsNumber_label)
        self._allEntry.append(chains_number_scale)

        for index in range(1):
            space = Label(self._leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self._allLabels.append(space)

        amino_amount_LabelFrame = LabelFrame(self._leftButtonsFrame,
                                             text='Argument 7:',
                                             fg='black', bg='light blue',
                                             font=("Ariel", 10, 'normal'))
        self._allLabelFrames.append(amino_amount_LabelFrame)

        amino_amount_LabelFrame.pack(side='top')

        amino_amount_label = Label(amino_amount_LabelFrame,
                                   text="Amino Acid Number:", bg='light blue',
                                   fg='black', font=("Ariel", 9, 'bold'))

        amino_amount_scale = Entry(amino_amount_LabelFrame,
                                   textvariable=self._aminoAmount, bd=2)
        amino_amount_label.pack()
        amino_amount_scale.pack()
        self._allLabels.append(amino_amount_label)
        self._allEntry.append(amino_amount_scale)

        for index in range(1):
            space = Label(self._leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self._allLabels.append(space)

    def grid_instructions(self):

        for index in range(2):
            space = Label(self._rightButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self._allLabels.append(space)

        random_init_LabelFrame = LabelFrame(self._rightButtonsFrame,
                                            text='Argument 8:',
                                            fg='black', bg='light blue',
                                            font=("Ariel", 10, 'normal'))
        self._allLabelFrames.append(random_init_LabelFrame)

        random_init_LabelFrame.pack(side='top')

        random_init_checkbox = Checkbutton(random_init_LabelFrame, text='Is Centered?',
                                           variable=self._randomInitCheckBoxStatus,
                                           bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        random_init_checkbox.pack(side='top')
        self._allCheckBoxes.append(random_init_checkbox)

        for index in range(1):
            space = Label(self._rightButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self._allLabels.append(space)

        diff_chains_type_LabelFrame = LabelFrame(self._rightButtonsFrame,
                                                 text='Argument 9:',
                                                 fg='black', bg='light blue',
                                                 font=("Ariel", 10, 'normal'))
        self._allLabelFrames.append(diff_chains_type_LabelFrame)

        diff_chains_type_LabelFrame.pack(side='top')

        diff_chains_checkbox = Checkbutton(diff_chains_type_LabelFrame, text='Two Groups?',
                                           variable=self._diffChainsCheckBoxStatus,
                                           bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        diff_chains_checkbox.pack(side='top')
        self._allCheckBoxes.append(diff_chains_checkbox)

        for index in range(2):
            space = Label(self._rightButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self._allLabels.append(space)

        quickInstructions = Label(self._rightButtonsFrame,
                                  text='Quick Instructions:', bg='light blue')
        quickInstructions.pack(side='top')
        self._allLabels.append(quickInstructions)

        stepOne = Label(self._rightButtonsFrame,
                        text='Step One:', bg='light blue')
        stepOne.pack(side='top')
        self._allLabels.append(stepOne)

        fillAllArg = Label(self._rightButtonsFrame,
                           text='Fill All The Arguments 1-9', bg='light blue',
                           font=("Ariel", 7, 'normal'))
        fillAllArg.pack(side='top')
        self._allLabels.append(fillAllArg)

        stepTwo = Label(self._rightButtonsFrame,
                        text='Step Two:', bg='light blue')
        stepTwo.pack(side='top')
        self._allLabels.append(stepTwo)

        placeToSave = Label(self._rightButtonsFrame,
                            text='Fill Your File Name', bg='light blue',
                            font=("Ariel", 7, 'normal'))
        placeToSave.pack(side='top')
        self._allLabels.append(placeToSave)

        stepThree = Label(self._rightButtonsFrame,
                          text='Step Three:', bg='light blue')
        stepThree.pack(side='top')
        self._allLabels.append(stepThree)

        FillSequence = Label(self._rightButtonsFrame,
                             text='Fill Your Sequence', bg='light blue',
                             font=("Ariel", 7, 'normal'))
        FillSequence.pack(side='top')
        self._allLabels.append(FillSequence)

        stepFour = Label(self._rightButtonsFrame,
                         text='Step Four:', bg='light blue')
        stepFour.pack(side='top')
        self._allLabels.append(stepFour)

        startSimulator = Label(self._rightButtonsFrame,
                               text='Press "Start Simulator"', bg='light blue',
                               font=("Ariel", 7, 'normal'))
        startSimulator.pack(side='top')
        self._allLabels.append(startSimulator)

        for index in range(1):
            space = Label(self._rightButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self._allLabels.append(space)

        enjoy = Label(self._rightButtonsFrame,
                      text='Enjoy!', bg='light blue')
        enjoy.pack(side='top')
        self._allLabels.append(enjoy)

        ilia = Label(self._rightButtonsFrame,
                     text='Ilia Bezgin', bg='light blue',
                     font=("Ariel", 6, 'normal'))
        ilia.pack(side='bottom')
        self._allLabels.append(ilia)

        rina = Label(self._rightButtonsFrame,
                     text='Rina Karnauch', bg='light blue',
                     font=("Ariel", 6, 'normal'))
        rina.pack(side='bottom')
        self._allLabels.append(rina)

        roy = Label(self._rightButtonsFrame,
                    text='Roy Maman', bg='light blue',
                    font=("Ariel", 6, 'normal'))
        roy.pack(side='bottom')
        self._allLabels.append(roy)

        ofek = Label(self._rightButtonsFrame,
                     text='Ofek Kaveh', bg='light blue',
                     font=("Ariel", 6, 'normal'))
        ofek.pack(side='bottom')
        self._allLabels.append(ofek)

        by = Label(self._rightButtonsFrame,
                   text='By:', bg='light blue',
                   font=("Ariel", 7, 'normal'))
        by.pack(side='bottom')
        self._allLabels.append(by)


def gui_buttons_and_design_init(program):
    program.mainFramesInit()
    program.grid_plot_checkboxes()
    program.gridEntry()
    program.grid_scales()
    program.grid_left_side_widgets()
    program.grid_instructions()
    program.changeModeButton()


def main():
    root = Tk()
    program = Gui_3D_Bio(root)
    gui_buttons_and_design_init(program)
    root.title("Hackathon Program")
    root.geometry('800x800')
    root.resizable(False, False)

    root.mainloop()
