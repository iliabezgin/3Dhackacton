from tkinter import *
import tkinter as tk
import main_model


class Gui_3D_Bio:
    def __init__(self, root):
        self._root = root
        self.__titleFrame = Frame(root, width=800, height=50,
                                  bg='gray98')
        self.__leftButtonsFrame = Frame(root, width=15, height=750,
                                        bg='gray92')
        self.__rightButtonsFrame = Frame(root, width=15, height=750,
                                         bg='gray92')
        self.__middleTopFrame = Frame(root, width=770, height=130,
                                      bg='gray91')
        self.__middleBottomFrame = Frame(root, width=770, height=650,
                                         bg='gray94')

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
        return self.__kInSize.get()

    def get_k_out(self):
        return self.__kOutSize.get()

    def get_sequence(self):
        return self.__givenSequence.get()

    def get_location(self):
        return self.__locationToSave.get()

    def get_bead_radius(self):
        return self.__beadRadiusSize.get()

    def get_sphere_radius(self):
        return self.__sphereRadiusSize.get()

    def get_kbs(self):
        return self.__kbsValue.get()

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
                      font=("Ariel", 15, 'normal'), bg='gray98',
                      fg='black')
        title.pack()
        self.__allLabels.append(title)
        self.__leftButtonsFrame.pack(side='left', fill='both')
        self.__rightButtonsFrame.pack(side="right", fill='both')
        self.__middleTopFrame.pack(fill='both')
        self.__middleBottomFrame.pack(side='top')

    def grid_buttons(self):
        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='gray92')
            space.pack(side='bottom')
            self.__allLabels.append(space)

        for index in range(1):
            space = Label(self.__rightButtonsFrame, text="", bg='gray92')
            space.pack(side='bottom')
            self.__allLabels.append(space)

    def change_mode_button(self):
        changeModeButton = Button(self.__leftButtonsFrame,
                                  text='Dark/Light Mode',
                                  height=1,
                                  width=15, font=("Ariel", 10, 'bold'),
                                  bg='white',
                                  command=lambda: self.dark_light_switch())
        changeModeButton.pack(side='top')
        self.__allButton.append(changeModeButton)

    def grid_entry(self):
        entryLabelFrame = LabelFrame(self.__middleTopFrame,
                                     text='Program Input',
                                     fg='black', bg='gray91',
                                     font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(entryLabelFrame)
        entryLabel = Label(entryLabelFrame, text='Enter Sequence:',
                           bg='gray91',
                           fg='black', font=("Ariel", 9, 'bold'))
        self.__allLabels.append(entryLabel)
        entryPlace = Entry(entryLabelFrame,
                           textvariable=self.__givenSequence, bd=2)
        self.__allEntry.append(entryPlace)
        submitButton = Button(entryLabelFrame, text='Submit',
                              height=1,
                              width=15, font=("Ariel", 10, 'bold'), bg='white',
                              command=lambda: self.submit_input())
        self.__allButton.append(submitButton)

        entryLabelFrame.pack(side='left', padx=7, pady=7)
        entryLabel.pack(side='top')
        entryPlace.pack(side='top')

        for index in range(1):
            space = Label(entryLabelFrame, text="", bg='gray91')
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

        main_model.create_model(self.__givenSequence.get(), 10,
                                self.__locationToSave.get(),
                                self.__beadRadiusSize.get(),
                                self.__sphereRadiusSize.get(),
                                self.__kbsValue.get(), 5, self.__kInSize.get(),
                                0.1)

    def dark_light_switch(self):

        if self.__lightMode:
            self.__titleFrame.configure(background='gray20')
            self.__leftButtonsFrame.configure(background='gray17')
            self.__rightButtonsFrame.configure(background='gray17')
            self.__middleTopFrame.configure(background='gray18')
            for label in self.__allLabels:
                if label['bg'] == 'gray98':
                    label.config(bg='gray20')
                if label['bg'] == 'gray92':
                    label.config(bg='gray17')
                if label['bg'] == 'gray91':
                    label.config(bg='gray18')
                if label['bg'] == 'gray94':
                    label.config(bg='gray22')
                label.config(fg='white')

            for entry in self.__allEntry:
                if entry['bg'] == 'gray98':
                    entry.config(bg='gray20')
                if entry['bg'] == 'gray92':
                    entry.config(bg='gray17')
                if entry['bg'] == 'gray91':
                    entry.config(bg='gray18')
                if entry['bg'] == 'gray94':
                    entry.config(bg='gray22')
                entry.config(fg='white')

            for button in self.__allButton:
                button.config(bg='black')
                button.config(fg='white')

            for labelFrame in self.__allLabelFrames:
                if labelFrame['bg'] == 'gray98':
                    labelFrame.config(bg='gray20')
                if labelFrame['bg'] == 'gray92':
                    labelFrame.config(bg='gray17')
                if labelFrame['bg'] == 'gray91':
                    labelFrame.config(bg='gray18')
                if labelFrame['bg'] == 'gray94':
                    labelFrame.config(bg='gray22')
                labelFrame['fg'] = 'white'

            for checkBox in self.__allCheckBoxes:
                if checkBox['bg'] == 'gray98':
                    checkBox.config(bg='gray20')
                if checkBox['bg'] == 'gray92':
                    checkBox.config(bg='gray17')
                if checkBox['bg'] == 'gray91':
                    checkBox.config(bg='gray18')
                if checkBox['bg'] == 'gray94':
                    checkBox.config(bg='gray22')

            self.__lightMode = False
        else:
            self.__titleFrame.configure(background='gray98')
            self.__leftButtonsFrame.configure(background='gray92')
            self.__rightButtonsFrame.configure(background='gray92')
            self.__middleTopFrame.configure(background='gray91')
            for label in self.__allLabels:
                if label['bg'] == 'gray20':
                    label.config(bg='gray98')
                if label['bg'] == 'gray17':
                    label.config(bg='gray92')
                if label['bg'] == 'gray18':
                    label.config(bg='gray91')
                if label['bg'] == 'gray22':
                    label.config(bg='gray94')
                label.config(fg='black')

            for entry in self.__allEntry:
                if entry['bg'] == 'gray20':
                    entry.config(bg='gray98')
                if entry['bg'] == 'gray17':
                    entry.config(bg='gray92')
                if entry['bg'] == 'gray18':
                    entry.config(bg='gray91')
                if entry['bg'] == 'gray22':
                    entry.config(bg='gray94')
                entry.config(fg='black')
            for button in self.__allButton:
                button.config(bg='white')
                button.config(fg='black')
            for labelFrame in self.__allLabelFrames:
                if labelFrame['bg'] == 'gray20':
                    labelFrame.config(bg='gray98')
                if labelFrame['bg'] == 'gray17':
                    labelFrame.config(bg='gray92')
                if labelFrame['bg'] == 'gray18':
                    labelFrame.config(bg='gray91')
                if labelFrame['bg'] == 'gray22':
                    labelFrame.config(bg='gray94')
                labelFrame['fg'] = 'black'
            for checkBox in self.__allCheckBoxes:
                if checkBox['bg'] == 'gray20':
                    checkBox.config(bg='gray98')
                if checkBox['bg'] == 'gray17':
                    checkBox.config(bg='gray92')
                if checkBox['bg'] == 'gray18':
                    checkBox.config(bg='gray91')
                if checkBox['bg'] == 'gray22':
                    checkBox.config(bg='gray94')

            self.__lightMode = True

    def grid_plot_checkboxes(self):
        plot_label = Label(self.__rightButtonsFrame, text='Select Your Plots:',
                           bg='gray92')
        plot_label.pack(side='top')
        self.__allLabels.append(plot_label)
        firstCheckBox = Checkbutton(self.__rightButtonsFrame, text='First Plot'
                                    , variable=self.__firstCheckBoxStatus,
                                    bg='gray92', fg='red')
        firstCheckBox.pack(side='top')
        self.__allCheckBoxes.append(firstCheckBox)

        secondCheckBox = Checkbutton(self.__rightButtonsFrame,
                                     text='Second Plot',
                                     variable=self.__secondCheckBoxStatus,
                                     bg='gray92', fg='red')
        secondCheckBox.pack(side='top')
        self.__allCheckBoxes.append(secondCheckBox)

        thirdCheckBox = Checkbutton(self.__rightButtonsFrame,
                                    text='Third Plot',
                                    variable=self.__thirdCheckBoxStatus,
                                    bg='gray92', fg='red')
        thirdCheckBox.pack(side='top')
        self.__allCheckBoxes.append(thirdCheckBox)

    def grid_scales(self):
        k_in_LabelFrame = LabelFrame(self.__middleTopFrame,
                                     text='Argument 1:',
                                     fg='black', bg='gray91',
                                     font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(k_in_LabelFrame)

        k_out_LabelFrame = LabelFrame(self.__middleTopFrame,
                                      text='Argument 2:',
                                      fg='black', bg='gray91',
                                      font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(k_out_LabelFrame)

        k_in_LabelFrame.pack(side='left')
        k_out_LabelFrame.pack(side='left')

        k_in_label = Label(k_in_LabelFrame, text="K-In:",
                           bg='gray91', fg='black', font=("Ariel", 9, 'bold'))
        k_in_scale = Entry(k_in_LabelFrame,
                           textvariable=self.__kInSize, bd=2)
        k_in_label.pack(side='left')
        k_in_scale.pack(side='left')
        self.__allLabels.append(k_in_label)

        k_out_label = Label(k_out_LabelFrame,
                            text="K-Out:", bg='gray91',
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
                                     fg='black', bg='gray92',
                                     font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(entryLabelFrame)
        entryLabel = Label(entryLabelFrame, text='Enter Location For RMF:',
                           bg='gray92',
                           fg='black', font=("Ariel", 9, 'bold'))
        self.__allLabels.append(entryLabel)
        entryPlace = Entry(entryLabelFrame,
                           textvariable=self.__locationToSave, bd=2)
        self.__allEntry.append(entryPlace)

        entryLabelFrame.pack(side='top', padx=7, pady=7)
        entryLabel.pack(side='top')
        entryPlace.pack(side='top')

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='gray92')
            space.pack(side='top')
            self.__allLabels.append(space)

        bead_radius_LabelFrame = LabelFrame(self.__leftButtonsFrame,
                                            text='Argument 3:',
                                            fg='black', bg='gray92',
                                            font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(bead_radius_LabelFrame)

        bead_radius_LabelFrame.pack(side='top')

        bead_radius_label = Label(bead_radius_LabelFrame,
                                  text="Enter Bead Radius:", bg='gray92',
                                  fg='black', font=("Ariel", 9, 'bold'))

        bead_radius_entry = Entry(bead_radius_LabelFrame,
                                  textvariable=self.__beadRadiusSize, bd=2)

        bead_radius_label.pack()
        bead_radius_entry.pack()
        self.__allLabels.append(bead_radius_label)
        self.__allEntry.append(bead_radius_entry)

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='gray92')
            space.pack(side='top')
            self.__allLabels.append(space)

        sphere_radius_LabelFrame = LabelFrame(self.__leftButtonsFrame,
                                              text='Argument 4:',
                                              fg='black', bg='gray92',
                                              font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(sphere_radius_LabelFrame)

        sphere_radius_LabelFrame.pack(side='top')

        sphere_radius_label = Label(sphere_radius_LabelFrame,
                                    text="Enter Sphere Radius:", bg='gray92',
                                    fg='black', font=("Ariel", 9, 'bold'))

        sphere_radius_scale = Entry(sphere_radius_LabelFrame,
                                    textvariable=self.__sphereRadiusSize, bd=2)
        sphere_radius_label.pack()
        sphere_radius_scale.pack()
        self.__allLabels.append(sphere_radius_label)
        self.__allScales.append(sphere_radius_scale)

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='gray92')
            space.pack(side='top')
            self.__allLabels.append(space)

        kbs_LabelFrame = LabelFrame(self.__leftButtonsFrame,
                                    text='Argument 5:',
                                    fg='black', bg='gray92',
                                    font=("Ariel", 10, 'normal'))
        self.__allLabelFrames.append(kbs_LabelFrame)

        kbs_LabelFrame.pack(side='top')

        kbs_label = Label(kbs_LabelFrame,
                          text="Enter KBS:", bg='gray92',
                          fg='black', font=("Ariel", 9, 'bold'))

        kbs_scale = Entry(kbs_LabelFrame,
                          textvariable=self.__kbsValue, bd=2)
        kbs_label.pack()
        kbs_scale.pack()
        self.__allLabels.append(kbs_label)
        self.__allScales.append(kbs_scale)

        for index in range(4):
            space = Label(self.__leftButtonsFrame, text="", bg='gray92')
            space.pack(side='top')
            self.__allLabels.append(space)


def main():
    root = Tk()
    program = Gui_3D_Bio(root)
    program.root_init()
    program.grid_buttons()
    program.grid_plot_checkboxes()
    program.grid_entry()
    program.grid_scales()
    program.grid_left_side_widgets()
    program.change_mode_button()
    root.title("Hackathon Program")
    root.geometry('800x800')
    root.resizable(False, False)

    seq = program.get_sequence()
    path = program.get_location()
    bead_radius = program.get_bead_radius()
    sphere_radius = program.get_sphere_radius()
    kbs = program.get_kbs()
    k_in = program.get_k_in()
    k_out = program.get_k_out()

    root.mainloop()
