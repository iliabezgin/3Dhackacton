from tkinter import *
import tkinter as tk
import main_model


def quit_program():
    quit()


class Gui_3D_Bio:
    def __init__(self, root):
        self._root = root
        self.__titleFrame = Frame(root, width=800, height=50,
                                  bg='orange')
        self.__leftButtonsFrame = Frame(root, width=15, height=750,
                                        bg='orange')
        self.__rightButtonsFrame = Frame(root, width=15, height=750,
                                         bg='orange')
        self.__middleTopFrame = Frame(root, width=770, height=130,
                                      bg='orange')
        self.__middleBottomFrame = Frame(root, width=770, height=650,
                                         bg='ghost white')
        self.__lowBorder = Frame(root, width=800, height=70, bg='orange')
        self.__lowBorder.pack(side='bottom')

        self.__givenSequence = tk.StringVar()
        self.__firstCheckBoxStatus = tk.IntVar()
        self.__secondCheckBoxStatus = tk.IntVar()
        self.__thirdCheckBoxStatus = tk.IntVar()
        self.__kInSize = tk.IntVar()
        self.__kOutSize = tk.IntVar()
        self.__beadRadiusSize = tk.IntVar()
        self.__sphereRadiusSize = tk.IntVar()
        self.__kbsValue = tk.IntVar()
        self.__locationToSave = tk.StringVar()
        self.__lightMode = True
        self.__allButton = []
        self.__allEntry = []
        self.__allLabels = []
        self.__allLabelFrames = []
        self.__informativeLabels = []
        self.__allCheckBoxes = []
        self.__allScales = []

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

    def add_space_left_button_menu(self, n):
        """
        the method will create space labels
        :param n: int
        :return: None
        """
        for index in range(n):
            space = Label(self.__leftButtonsFrame, text="", bg='blue')
            space.pack(side='top')
            self.__allLabels.append(space)

    def root_init(self):
        self.__titleFrame.pack(side='top', fill='both')
        title = Label(self.__titleFrame, text='Membraneless Organelles Final '
                                              'Project',
                      font=("Ariel", 15, 'normal'), bg='orange',
                      fg='black')
        title.pack()
        self.__allLabels.append(title)
        self.__leftButtonsFrame.pack(side='left', fill='both')
        self.__rightButtonsFrame.pack(side="right", fill='both')
        self.__middleTopFrame.pack(fill='both')
        self.__middleBottomFrame.pack(side='top')

    def change_mode_button(self):
        changeModeButton = Button(self.__leftButtonsFrame,
                                  text='Dark/Light Mode',
                                  height=1,
                                  width=15, font=("Ariel", 10, 'bold'),
                                  bg='white',
                                  command=lambda: self.dark_light_switch())
        changeModeButton.pack(side='top')
        self.__allButton.append(changeModeButton)

        for index in range(11):
            space = Label(self.__leftButtonsFrame, text="", bg='orange')
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
                                     fg='black', bg='orange',
                                     font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(entryLabelFrame)
        entryLabel = Label(entryLabelFrame, text='Enter Sequence:',
                           bg='orange',
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
            space = Label(entryLabelFrame, text="", bg='orange')
            space.pack(side='top')
            self.__allLabels.append(space)

        submitButton.pack(side='top')

    def submit_input(self):
        for label in self.__informativeLabels:
            label.pack_forget()
        isFirstPlot = self.__firstCheckBoxStatus.get()
        isSecondPlot = self.__secondCheckBoxStatus.get()
        isThirdPlot = self.__thirdCheckBoxStatus.get()

        if isFirstPlot == 1:
            firstPlotLabel = Label(self.__middleBottomFrame,
                                   text='You Chose To Show First Plot',
                                   fg='blue')
            firstPlotLabel.pack(side='top', fill='both')
            self.__informativeLabels.append(firstPlotLabel)

        if isSecondPlot == 1:
            secondPlotLabel = Label(self.__middleBottomFrame,
                                    text='You Chose To Show Second Plot',
                                    fg='blue')
            secondPlotLabel.pack(side='top', fill='both')
            self.__informativeLabels.append(secondPlotLabel)

        if isThirdPlot == 1:
            thirdPlotLabel = Label(self.__middleBottomFrame,
                                   text='You Chose To Show Third Plot',
                                   fg='blue')
            thirdPlotLabel.pack(side='top', fill='both')
            self.__informativeLabels.append(thirdPlotLabel)

        main_model.create_model(self.__givenSequence.get(), 4,
                                self.__locationToSave.get(),
                                self.__beadRadiusSize.get(),
                                self.__sphereRadiusSize.get(),
                                self.__kbsValue.get(), 5,
                                self.__kInSize.get(), self.__kOutSize.get())

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

            for entry in self.__allEntry:
                entry.config(bg='ghost white')
                entry.config(fg='black')

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
            self.__titleFrame.configure(background='orange')
            self.__leftButtonsFrame.configure(background='orange')
            self.__rightButtonsFrame.configure(background='orange')
            self.__middleTopFrame.configure(background='orange')
            self.__lowBorder.configure(background='orange')

            for label in self.__allLabels:
                label.config(bg='orange')
                label.config(fg='black')

            for entry in self.__allEntry:
                entry.config(bg='ghost white')
                entry.config(fg='black')

            for button in self.__allButton:
                button.config(bg='white')
                button.config(fg='black')

            for labelFrame in self.__allLabelFrames:
                labelFrame.config(bg='orange')
                labelFrame['fg'] = 'black'

            for checkBox in self.__allCheckBoxes:
                checkBox.config(bg='orange')

            self.__lightMode = True

    def grid_plot_checkboxes(self):
        plot_label = Label(self.__rightButtonsFrame, text='Select Your Plots:',
                           bg='orange')
        plot_label.pack(side='top')
        self.__allLabels.append(plot_label)
        firstCheckBox = Checkbutton(self.__rightButtonsFrame, text='First Plot'
                                    , variable=self.__firstCheckBoxStatus,
                                    bg='orange', fg='red')
        firstCheckBox.pack(side='top')
        self.__allCheckBoxes.append(firstCheckBox)

        secondCheckBox = Checkbutton(self.__rightButtonsFrame,
                                     text='Second Plot',
                                     variable=self.__secondCheckBoxStatus,
                                     bg='orange', fg='red')
        secondCheckBox.pack(side='top')
        self.__allCheckBoxes.append(secondCheckBox)

        thirdCheckBox = Checkbutton(self.__rightButtonsFrame,
                                    text='Third Plot',
                                    variable=self.__thirdCheckBoxStatus,
                                    bg='orange', fg='red')
        thirdCheckBox.pack(side='top')
        self.__allCheckBoxes.append(thirdCheckBox)

    def grid_scales(self):
        k_in_LabelFrame = LabelFrame(self.__middleTopFrame,
                                     text='Argument 1:',
                                     fg='black', bg='orange',
                                     font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(k_in_LabelFrame)

        k_out_LabelFrame = LabelFrame(self.__middleTopFrame,
                                      text='Argument 2:',
                                      fg='black', bg='orange',
                                      font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(k_out_LabelFrame)

        k_in_LabelFrame.pack(side='left')
        k_out_LabelFrame.pack(side='left')

        k_in_label = Label(k_in_LabelFrame, text="K-In:",
                           bg='orange', fg='black', font=("Ariel", 9, 'bold'))
        k_in_scale = Entry(k_in_LabelFrame,
                           textvariable=self.__kInSize, bd=2)
        k_in_label.pack(side='left')
        k_in_scale.pack(side='left')
        self.__allLabels.append(k_in_label)

        k_out_label = Label(k_out_LabelFrame,
                            text="K-Out:", bg='orange',
                            fg='black', font=("Ariel", 9, 'bold'))

        k_out_scale = Entry(k_out_LabelFrame,
                            textvariable=self.__kOutSize, bd=2)
        k_out_label.pack(side='left')
        k_out_scale.pack(side='left')
        self.__allLabels.append(k_out_label)

        self.__allScales.append(k_in_scale)
        self.__allScales.append(k_out_scale)

    def grid_left_side_widgets(self):
        entryLabelFrame = LabelFrame(self.__leftButtonsFrame,
                                     text='Output Save Location',
                                     fg='black', bg='orange',
                                     font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(entryLabelFrame)
        entryLabel = Label(entryLabelFrame, text='Enter Location For RMF:',
                           bg='orange',
                           fg='black', font=("Ariel", 9, 'bold'))
        self.__allLabels.append(entryLabel)
        entryPlace = Entry(entryLabelFrame,
                           textvariable=self.__locationToSave, bd=2)
        self.__allEntry.append(entryPlace)

        entryLabelFrame.pack(side='top', padx=7, pady=7)
        entryLabel.pack(side='top')
        entryPlace.pack(side='top')

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='orange')
            space.pack(side='top')
            self.__allLabels.append(space)

        bead_radius_LabelFrame = LabelFrame(self.__leftButtonsFrame,
                                            text='Argument 3:',
                                            fg='black', bg='orange',
                                            font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(bead_radius_LabelFrame)

        bead_radius_LabelFrame.pack(side='top')

        bead_radius_label = Label(bead_radius_LabelFrame,
                                  text="Enter Bead Radius:", bg='orange',
                                  fg='black', font=("Ariel", 9, 'bold'))

        bead_radius_entry = Entry(bead_radius_LabelFrame,
                                  textvariable=self.__beadRadiusSize, bd=2)

        bead_radius_label.pack()
        bead_radius_entry.pack()
        self.__allLabels.append(bead_radius_label)
        self.__allEntry.append(bead_radius_entry)

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='orange')
            space.pack(side='top')
            self.__allLabels.append(space)

        sphere_radius_LabelFrame = LabelFrame(self.__leftButtonsFrame,
                                              text='Argument 4:',
                                              fg='black', bg='orange',
                                              font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(sphere_radius_LabelFrame)

        sphere_radius_LabelFrame.pack(side='top')

        sphere_radius_label = Label(sphere_radius_LabelFrame,
                                    text="Enter Sphere Radius:", bg='orange',
                                    fg='black', font=("Ariel", 9, 'bold'))

        sphere_radius_scale = Entry(sphere_radius_LabelFrame,
                                    textvariable=self.__sphereRadiusSize, bd=2)
        sphere_radius_label.pack()
        sphere_radius_scale.pack()
        self.__allLabels.append(sphere_radius_label)
        self.__allScales.append(sphere_radius_scale)

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='orange')
            space.pack(side='top')
            self.__allLabels.append(space)

        kbs_LabelFrame = LabelFrame(self.__leftButtonsFrame,
                                    text='Argument 5:',
                                    fg='black', bg='orange',
                                    font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(kbs_LabelFrame)

        kbs_LabelFrame.pack(side='top')

        kbs_label = Label(kbs_LabelFrame,
                          text="Enter KBS:", bg='orange',
                          fg='black', font=("Ariel", 9, 'bold'))

        kbs_scale = Entry(kbs_LabelFrame,
                          textvariable=self.__kbsValue, bd=2)
        kbs_label.pack()
        kbs_scale.pack()
        self.__allLabels.append(kbs_label)
        self.__allScales.append(kbs_scale)

        for index in range(4):
            space = Label(self.__leftButtonsFrame, text="", bg='orange')
            space.pack(side='top')
            self.__allLabels.append(space)

    def grid_instructions(self):

        for index in range(6):
            space = Label(self.__rightButtonsFrame, text="", bg='orange')
            space.pack(side='top')
            self.__allLabels.append(space)

        quickInstructions = Label(self.__rightButtonsFrame,
                                  text='Quick Instructions:', bg='orange')
        quickInstructions.pack(side='top')
        self.__allLabels.append(quickInstructions)

        stepOne = Label(self.__rightButtonsFrame,
                        text='Step One:', bg='orange')
        stepOne.pack(side='top')
        self.__allLabels.append(stepOne)

        fillAllArg = Label(self.__rightButtonsFrame,
                           text='Fill All The Arguments 1-5', bg='orange',
                           font=("Ariel", 7, 'normal'))
        fillAllArg.pack(side='top')
        self.__allLabels.append(fillAllArg)

        stepTwo = Label(self.__rightButtonsFrame,
                        text='Step Two:', bg='orange')
        stepTwo.pack(side='top')
        self.__allLabels.append(stepTwo)

        placeToSave = Label(self.__rightButtonsFrame,
                            text='Fill Your Save Location', bg='orange',
                            font=("Ariel", 7, 'normal'))
        placeToSave.pack(side='top')
        self.__allLabels.append(placeToSave)

        stepThree = Label(self.__rightButtonsFrame,
                          text='Step Three:', bg='orange')
        stepThree.pack(side='top')
        self.__allLabels.append(stepThree)

        FillSequence = Label(self.__rightButtonsFrame,
                             text='Fill Your Sequence', bg='orange',
                             font=("Ariel", 7, 'normal'))
        FillSequence.pack(side='top')
        self.__allLabels.append(FillSequence)

        stepFour = Label(self.__rightButtonsFrame,
                         text='Step Four:', bg='orange')
        stepFour.pack(side='top')
        self.__allLabels.append(stepFour)

        startSimulator = Label(self.__rightButtonsFrame,
                               text='Press "Start Simulator"', bg='orange',
                               font=("Ariel", 7, 'normal'))
        startSimulator.pack(side='top')
        self.__allLabels.append(startSimulator)

        for index in range(1):
            space = Label(self.__rightButtonsFrame, text="", bg='orange')
            space.pack(side='top')
            self.__allLabels.append(space)

        enjoy = Label(self.__rightButtonsFrame,
                      text='Enjoy!', bg='orange')
        enjoy.pack(side='top')
        self.__allLabels.append(enjoy)


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
