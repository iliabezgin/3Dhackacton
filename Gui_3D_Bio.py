from tkinter import *
import tkinter as tk


import main_model
import plots
from PIL import ImageTk, Image


def quit_program():
    quit()


class Gui_3D_Bio:
    def __init__(self, root):
        self._root = root
        self.__titleFrame = Frame(root, width=800, height=50,
                                  bg='light blue')
        self.__leftButtonsFrame = Frame(root, width=15, height=750,
                                        bg='light blue')
        self.__rightButtonsFrame = Frame(root, width=15, height=750,
                                         bg='light blue')
        self.__middleTopFrame = Frame(root, width=770, height=130,
                                      bg='light blue')
        self.__middleBottomFrame = Frame(root, width=770, height=650,
                                         bg='grey93')
        self.__lowBorder = Frame(root, width=800, height=70, bg='light blue')
        self.__lowBorder.pack(side='bottom')

        self.__givenSequence = tk.StringVar()
        self.__firstCheckBoxStatus = tk.IntVar()
        self.__secondCheckBoxStatus = tk.IntVar()
        self.__thirdCheckBoxStatus = tk.IntVar()
        self.__fourthCheckBoxStatus = tk.IntVar()
        self.__fifthCheckBoxStatus = tk.IntVar()
        self.__randomInitCheckBoxStatus = tk.IntVar()
        self.__diffChainsCheckBoxStatus = tk.IntVar()
        self.__kInSize = tk.IntVar()
        self.__kOutSize = tk.IntVar()
        self.__beadRadiusSize = tk.IntVar()
        self.__sphereRadiusSize = tk.IntVar()
        self.__kbsValue = tk.IntVar()
        self.__locationToSave = tk.StringVar()
        self.__chainsNumber = tk.IntVar()
        self.__aminoAmount = tk.IntVar()
        self.__lightMode = True
        self.__allButton = []
        self.__allEntry = []
        self.__allLabels = []
        self.__allLabelFrames = []
        self.__informativeLabels = []
        self.__allCheckBoxes = []

    def get_k_in(self):
        return self.__kInSize

    def get_k_out(self):
        return self.__kOutSize

    def get_sequence(self):
        return self.__givenSequence

    def get_location(self):
        return self.__locationToSave

    def get_bead_radius(self):
        return self.__beadRadiusSize

    def get_sphere_radius(self):
        return self.__sphereRadiusSize

    def get_kbs(self):
        return self.__kbsValue

    def root_init(self):
        self.__titleFrame.pack(side='top', fill='both')
        title = Label(self.__titleFrame, text='Membraneless Organelles Final '
                                              'Project',
                      font=("Linux Libertine Mono O", 15, 'bold'), bg='light blue',
                      fg='black')
        title.pack()
        self.__allLabels.append(title)
        self.__leftButtonsFrame.pack(side='left', fill='both')
        self.__rightButtonsFrame.pack(side="right", fill='both')
        self.__middleTopFrame.pack(fill='both')
        self.__middleBottomFrame.pack(side='top', fill='both')

    def change_mode_button(self):
        for index in range(2):
            space = Label(self.__leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        changeModeButton = Button(self.__leftButtonsFrame,
                                  text='Dark/Light Mode',
                                  height=1,
                                  width=15, font=("Ariel", 10, 'bold'),
                                  bg='white',
                                  command=lambda: self.dark_light_switch())
        changeModeButton.pack(side='top')
        self.__allButton.append(changeModeButton)

        for index in range(3):
            space = Label(self.__leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        exitButton = Button(self.__leftButtonsFrame, text='Exit', height=1,
                            width=15, font=("Ariel", 10, 'bold'),
                            bg='white',
                            command=lambda: quit())
        exitButton.pack(side='top')
        self.__allButton.append(exitButton)

    def grid_entry(self):
        entryLabelFrame = LabelFrame(self.__middleTopFrame,
                                     text='Program Input',
                                     fg='black', bg='light blue',
                                     font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(entryLabelFrame)
        entryLabel = Label(entryLabelFrame, text='Enter Sequence:',
                           bg='light blue',
                           fg='black', font=("Ariel", 9, 'bold'))
        self.__allLabels.append(entryLabel)
        entryPlace = Entry(entryLabelFrame,
                           textvariable=self.__givenSequence, bd=2)
        self.__allEntry.append(entryPlace)
        submitButton = Button(entryLabelFrame, text='Start Simulation',
                              height=1,
                              width=15, font=("Ariel", 10, 'bold'), bg='white',
                              command=lambda: self.submit_input())
        self.__allButton.append(submitButton)

        entryLabelFrame.pack(side='left', padx=7, pady=7)
        entryLabel.pack(side='top')
        entryPlace.pack(side='top')

        for index in range(1):
            space = Label(entryLabelFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        submitButton.pack(side='top')

    def pop_up_plot(self, path):
        window = tk.Toplevel()
        window.wm_title("Plot")
        window.configure(background='grey')

        img = ImageTk.PhotoImage(Image.open(path))
        image_label = Label(window, image=img)
        image_label.photo = img
        image_label.pack()

    def submit_input(self):
        random_init_flag = False
        random_diff_type = False
        for label in self.__informativeLabels:
            label.pack_forget()

        simulationRunLabel = Label(self.__middleBottomFrame,
                                   text='Running Simulation!',
                                   fg='blue', bg='grey93', font=("Ariel", 10, 'normal'))
        simulationRunLabel.pack(side='top')
        self.__informativeLabels.append(simulationRunLabel)

        if self.__randomInitCheckBoxStatus.get() == 1:
            random_init_flag = True

        if self.__diffChainsCheckBoxStatus.get() == 1:
            random_diff_type = True

        T_ns, E, D, chains_on_iteration = main_model.create_model(self.__givenSequence.get(), self.__chainsNumber.get(),
                                                                  self.__locationToSave.get(),
                                                                  self.__beadRadiusSize.get(),
                                                                  self.__sphereRadiusSize.get(),
                                                                  self.__kbsValue.get(), self.__aminoAmount.get(),
                                                                  self.__kInSize.get(), self.__kOutSize.get(),
                                                                  random_init_flag, random_diff_type)

        if self.__firstCheckBoxStatus.get() == 1:
            firstPlotLabel = Label(self.__middleBottomFrame,
                                   text='Generating Energy Over Time Plot...',
                                   fg='blue', bg='grey93', font=("Ariel", 9, 'normal'))
            firstPlotLabel.pack(side='top')
            self.__informativeLabels.append(firstPlotLabel)
            plots.simulation_energy_over_time(E, T_ns, 1)
            self.pop_up_plot("energy_graph.png")

        if self.__secondCheckBoxStatus.get() == 1:
            secondPlotLabel = Label(self.__middleBottomFrame,
                                    text='Generating End To End Over Time Plot...',
                                    fg='blue', bg='grey93', font=("Ariel", 9, 'normal'))
            secondPlotLabel.pack(side='top')
            self.__informativeLabels.append(secondPlotLabel)
            plots.end_to_end_distances_over_time(E, T_ns, 1)
            self.pop_up_plot("distances_graph.png")

        if self.__thirdCheckBoxStatus.get() == 1:
            thirdPlotLabel = Label(self.__middleBottomFrame,
                                   text='Generating Distribution Of Energy Over Time Plot...',
                                   fg='blue', bg='grey93', font=("Ariel", 9, 'normal'))
            thirdPlotLabel.pack(side='top')
            self.__informativeLabels.append(thirdPlotLabel)
            plots.distribution_of_energy_over_time(E, T_ns, 1)
            self.pop_up_plot("dist_of_E.png")

        if self.__fourthCheckBoxStatus.get() == 1:
            fourthPlotLabel = Label(self.__middleBottomFrame,
                                    text='Generating Distribution Of Distances Over Time Plot...',
                                    fg='blue', bg='grey93', font=("Ariel", 9, 'normal'))
            fourthPlotLabel.pack(side='top')
            self.__informativeLabels.append(fourthPlotLabel)
            plots.distribution_of_dist_over_time(D)
            self.pop_up_plot("dist_of_D.png")

        if self.__fifthCheckBoxStatus.get() == 1:
            fifthPlotLabel = Label(self.__middleBottomFrame,
                                   text='Generating Distribution Of Bead Locations...',
                                   fg='blue', bg='grey93', font=("Ariel", 9, 'normal'))
            fifthPlotLabel.pack(side='top')
            self.__informativeLabels.append(fifthPlotLabel)
            plots.distribution_of_beads_locations(chains_on_iteration, T_ns, 1)
            self.pop_up_plot("variance_of_centers.png")

        endOfRunLabel = Label(self.__middleBottomFrame,
                              text='Simulating is Over, Check Out Your Plots',
                              fg='blue', bg='grey93', font=("Ariel", 10, 'normal'))
        endOfRunLabel.pack(side='top')
        self.__informativeLabels.append(endOfRunLabel)

    def dark_light_switch(self):

        if self.__lightMode:
            self.__titleFrame.configure(background='gray20')
            self.__leftButtonsFrame.configure(background='gray20')
            self.__rightButtonsFrame.configure(background='gray20')
            self.__middleTopFrame.configure(background='gray20')
            self.__lowBorder.configure(background='gray20')
            for label in self.__allLabels:
                label.config(bg='gray20')
                label.config(fg='white')

            for button in self.__allButton:
                button.config(bg='black')
                button.config(fg='white')

            for labelFrame in self.__allLabelFrames:
                labelFrame.config(bg='gray20')
                labelFrame['fg'] = 'white'

            for checkBox in self.__allCheckBoxes:
                checkBox.config(bg='gray20')

            self.__lightMode = False
        else:
            self.__titleFrame.configure(background='light blue')
            self.__leftButtonsFrame.configure(background='light blue')
            self.__rightButtonsFrame.configure(background='light blue')
            self.__middleTopFrame.configure(background='light blue')
            self.__lowBorder.configure(background='light blue')

            for label in self.__allLabels:
                label.config(bg='light blue')
                label.config(fg='black')

            for button in self.__allButton:
                button.config(bg='white')
                button.config(fg='black')

            for labelFrame in self.__allLabelFrames:
                labelFrame.config(bg='light blue')
                labelFrame['fg'] = 'black'

            for checkBox in self.__allCheckBoxes:
                checkBox.config(bg='light blue')

            self.__lightMode = True

    def grid_plot_checkboxes(self):

        plot_label = Label(self.__rightButtonsFrame, text='Select Your Plots:',
                           bg='light blue')
        plot_label.pack(side='top')
        self.__allLabels.append(plot_label)

        for index in range(1):
            space = Label(self.__rightButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        firstCheckBox = Checkbutton(self.__rightButtonsFrame, text='Energy Over Time',
                                    variable=self.__firstCheckBoxStatus,
                                    bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        firstCheckBox.pack(side='top')
        self.__allCheckBoxes.append(firstCheckBox)

        secondCheckBox = Checkbutton(self.__rightButtonsFrame,
                                     text='End to End Distances',
                                     variable=self.__secondCheckBoxStatus,
                                     bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        secondCheckBox.pack(side='top')
        self.__allCheckBoxes.append(secondCheckBox)

        thirdCheckBox = Checkbutton(self.__rightButtonsFrame,
                                    text='Energy Distribution',
                                    variable=self.__thirdCheckBoxStatus,
                                    bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        thirdCheckBox.pack(side='top')
        self.__allCheckBoxes.append(thirdCheckBox)

        fourthCheckBox = Checkbutton(self.__rightButtonsFrame,
                                     text='Location Distribution',
                                     variable=self.__fourthCheckBoxStatus,
                                     bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        fourthCheckBox.pack(side='top')
        self.__allCheckBoxes.append(fourthCheckBox)

        fifthCheckBox = Checkbutton(self.__rightButtonsFrame,
                                    text='Beads Location',
                                    variable=self.__fifthCheckBoxStatus,
                                    bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        fifthCheckBox.pack(side='top')
        self.__allCheckBoxes.append(fifthCheckBox)

    def grid_scales(self):
        k_in_LabelFrame = LabelFrame(self.__middleTopFrame,
                                     text='Argument 1:',
                                     fg='black', bg='light blue',
                                     font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(k_in_LabelFrame)

        k_out_LabelFrame = LabelFrame(self.__middleTopFrame,
                                      text='Argument 2:',
                                      fg='black', bg='light blue',
                                      font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(k_out_LabelFrame)

        k_in_LabelFrame.pack(side='left')
        k_out_LabelFrame.pack(side='left')

        k_in_label = Label(k_in_LabelFrame, text="K-In:",
                           bg='light blue', fg='black', font=("Ariel", 9, 'bold'))
        k_in_scale = Entry(k_in_LabelFrame,
                           textvariable=self.__kInSize, bd=2)
        k_in_label.pack(side='left')
        k_in_scale.pack(side='left')
        self.__allLabels.append(k_in_label)

        k_out_label = Label(k_out_LabelFrame,
                            text="K-Out:", bg='light blue',
                            fg='black', font=("Ariel", 9, 'bold'))

        k_out_scale = Entry(k_out_LabelFrame,
                            textvariable=self.__kOutSize, bd=2)
        k_out_label.pack(side='left')
        k_out_scale.pack(side='left')
        self.__allLabels.append(k_out_label)

        self.__allEntry.append(k_in_scale)
        self.__allEntry.append(k_out_scale)

    def grid_left_side_widgets(self):
        entryLabelFrame = LabelFrame(self.__leftButtonsFrame,
                                     text='Output Save Location',
                                     fg='black', bg='light blue',
                                     font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(entryLabelFrame)
        entryLabel = Label(entryLabelFrame, text='Enter Name For RMF:',
                           bg='light blue',
                           fg='black', font=("Ariel", 9, 'bold'))
        self.__allLabels.append(entryLabel)
        entryPlace = Entry(entryLabelFrame,
                           textvariable=self.__locationToSave, bd=2)
        self.__allEntry.append(entryPlace)

        entryLabelFrame.pack(side='top', padx=7, pady=7)
        entryLabel.pack(side='top')
        entryPlace.pack(side='top')

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        bead_radius_LabelFrame = LabelFrame(self.__leftButtonsFrame,
                                            text='Argument 3:',
                                            fg='black', bg='light blue',
                                            font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(bead_radius_LabelFrame)

        bead_radius_LabelFrame.pack(side='top')

        bead_radius_label = Label(bead_radius_LabelFrame,
                                  text="Enter Bead Radius:", bg='light blue',
                                  fg='black', font=("Ariel", 9, 'bold'))

        bead_radius_entry = Entry(bead_radius_LabelFrame,
                                  textvariable=self.__beadRadiusSize, bd=2)

        bead_radius_label.pack()
        bead_radius_entry.pack()
        self.__allLabels.append(bead_radius_label)
        self.__allEntry.append(bead_radius_entry)

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        sphere_radius_LabelFrame = LabelFrame(self.__leftButtonsFrame,
                                              text='Argument 4:',
                                              fg='black', bg='light blue',
                                              font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(sphere_radius_LabelFrame)

        sphere_radius_LabelFrame.pack(side='top')

        sphere_radius_label = Label(sphere_radius_LabelFrame,
                                    text="Enter Sphere Radius:", bg='light blue',
                                    fg='black', font=("Ariel", 9, 'bold'))

        sphere_radius_scale = Entry(sphere_radius_LabelFrame,
                                    textvariable=self.__sphereRadiusSize, bd=2)
        sphere_radius_label.pack()
        sphere_radius_scale.pack()
        self.__allLabels.append(sphere_radius_label)
        self.__allEntry.append(sphere_radius_scale)

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        kbs_LabelFrame = LabelFrame(self.__leftButtonsFrame,
                                    text='Argument 5:',
                                    fg='black', bg='light blue',
                                    font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(kbs_LabelFrame)

        kbs_LabelFrame.pack(side='top')

        kbs_label = Label(kbs_LabelFrame,
                          text="Enter KBS:", bg='light blue',
                          fg='black', font=("Ariel", 9, 'bold'))

        kbs_scale = Entry(kbs_LabelFrame,
                          textvariable=self.__kbsValue, bd=2)
        kbs_label.pack()
        kbs_scale.pack()
        self.__allLabels.append(kbs_label)
        self.__allEntry.append(kbs_scale)

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        chains_number_LabelFrame = LabelFrame(self.__leftButtonsFrame,
                                              text='Argument 6:',
                                              fg='black', bg='light blue',
                                              font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(chains_number_LabelFrame)

        chains_number_LabelFrame.pack(side='top')

        chainsNumber_label = Label(chains_number_LabelFrame,
                                   text="Enter Number Of Chains:", bg='light blue',
                                   fg='black', font=("Ariel", 9, 'bold'))

        chains_number_scale = Entry(chains_number_LabelFrame,
                                    textvariable=self.__chainsNumber, bd=2)
        chainsNumber_label.pack()
        chains_number_scale.pack()
        self.__allLabels.append(chainsNumber_label)
        self.__allEntry.append(chains_number_scale)

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        amino_amount_LabelFrame = LabelFrame(self.__leftButtonsFrame,
                                             text='Argument 7:',
                                             fg='black', bg='light blue',
                                             font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(amino_amount_LabelFrame)

        amino_amount_LabelFrame.pack(side='top')

        amino_amount_label = Label(amino_amount_LabelFrame,
                                   text="Amino Acid Number:", bg='light blue',
                                   fg='black', font=("Ariel", 9, 'bold'))

        amino_amount_scale = Entry(amino_amount_LabelFrame,
                                   textvariable=self.__aminoAmount, bd=2)
        amino_amount_label.pack()
        amino_amount_scale.pack()
        self.__allLabels.append(amino_amount_label)
        self.__allEntry.append(amino_amount_scale)

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

    def grid_instructions(self):

        for index in range(2):
            space = Label(self.__rightButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        random_init_LabelFrame = LabelFrame(self.__rightButtonsFrame,
                                            text='Argument 8:',
                                            fg='black', bg='light blue',
                                            font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(random_init_LabelFrame)

        random_init_LabelFrame.pack(side='top')

        random_init_checkbox = Checkbutton(random_init_LabelFrame, text='Is Centered?',
                                           variable=self.__randomInitCheckBoxStatus,
                                           bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        random_init_checkbox.pack(side='top')
        self.__allCheckBoxes.append(random_init_checkbox)

        for index in range(1):
            space = Label(self.__rightButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        diff_chains_type_LabelFrame = LabelFrame(self.__rightButtonsFrame,
                                                 text='Argument 9:',
                                                 fg='black', bg='light blue',
                                                 font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(diff_chains_type_LabelFrame)

        diff_chains_type_LabelFrame.pack(side='top')

        diff_chains_checkbox = Checkbutton(diff_chains_type_LabelFrame, text='Two Groups?',
                                           variable=self.__diffChainsCheckBoxStatus,
                                           bg='light blue', fg='red', font=("Ariel", 7, 'normal'))
        diff_chains_checkbox.pack(side='top')
        self.__allCheckBoxes.append(diff_chains_checkbox)

        for index in range(2):
            space = Label(self.__rightButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        quickInstructions = Label(self.__rightButtonsFrame,
                                  text='Quick Instructions:', bg='light blue')
        quickInstructions.pack(side='top')
        self.__allLabels.append(quickInstructions)

        stepOne = Label(self.__rightButtonsFrame,
                        text='Step One:', bg='light blue')
        stepOne.pack(side='top')
        self.__allLabels.append(stepOne)

        fillAllArg = Label(self.__rightButtonsFrame,
                           text='Fill All The Arguments 1-9', bg='light blue',
                           font=("Ariel", 7, 'normal'))
        fillAllArg.pack(side='top')
        self.__allLabels.append(fillAllArg)

        stepTwo = Label(self.__rightButtonsFrame,
                        text='Step Two:', bg='light blue')
        stepTwo.pack(side='top')
        self.__allLabels.append(stepTwo)

        placeToSave = Label(self.__rightButtonsFrame,
                            text='Fill Your File Name', bg='light blue',
                            font=("Ariel", 7, 'normal'))
        placeToSave.pack(side='top')
        self.__allLabels.append(placeToSave)

        stepThree = Label(self.__rightButtonsFrame,
                          text='Step Three:', bg='light blue')
        stepThree.pack(side='top')
        self.__allLabels.append(stepThree)

        FillSequence = Label(self.__rightButtonsFrame,
                             text='Fill Your Sequence', bg='light blue',
                             font=("Ariel", 7, 'normal'))
        FillSequence.pack(side='top')
        self.__allLabels.append(FillSequence)

        stepFour = Label(self.__rightButtonsFrame,
                         text='Step Four:', bg='light blue')
        stepFour.pack(side='top')
        self.__allLabels.append(stepFour)

        startSimulator = Label(self.__rightButtonsFrame,
                               text='Press "Start Simulator"', bg='light blue',
                               font=("Ariel", 7, 'normal'))
        startSimulator.pack(side='top')
        self.__allLabels.append(startSimulator)

        for index in range(1):
            space = Label(self.__rightButtonsFrame, text="", bg='light blue')
            space.pack(side='top')
            self.__allLabels.append(space)

        enjoy = Label(self.__rightButtonsFrame,
                      text='Enjoy!', bg='light blue')
        enjoy.pack(side='top')
        self.__allLabels.append(enjoy)

        ilia = Label(self.__rightButtonsFrame,
                     text='Ilia Bezgin', bg='light blue',
                     font=("Ariel", 6, 'normal'))
        ilia.pack(side='bottom')
        self.__allLabels.append(ilia)

        rina = Label(self.__rightButtonsFrame,
                     text='Rina Karnauch', bg='light blue',
                     font=("Ariel", 6, 'normal'))
        rina.pack(side='bottom')
        self.__allLabels.append(rina)

        roy = Label(self.__rightButtonsFrame,
                    text='Roy Maman', bg='light blue',
                    font=("Ariel", 6, 'normal'))
        roy.pack(side='bottom')
        self.__allLabels.append(roy)

        ofek = Label(self.__rightButtonsFrame,
                     text='Ofek Kaveh', bg='light blue',
                     font=("Ariel", 6, 'normal'))
        ofek.pack(side='bottom')
        self.__allLabels.append(ofek)

        by = Label(self.__rightButtonsFrame,
                   text='By:', bg='light blue',
                   font=("Ariel", 7, 'normal'))
        by.pack(side='bottom')
        self.__allLabels.append(by)


def main():
    root = Tk()
    program = Gui_3D_Bio(root)
    program.root_init()
    program.grid_plot_checkboxes()
    program.grid_entry()
    program.grid_scales()
    program.grid_left_side_widgets()
    program.grid_instructions()
    program.change_mode_button()
    root.title("Hackathon Program")
    root.geometry('800x800')
    root.resizable(False, False)

    root.mainloop()
