from tkinter import *
import tkinter as tk


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

        self.__firstArgument = tk.StringVar()
        self.__firstCheckBoxStatus = tk.IntVar()
        self.__secondCheckBoxStatus = tk.IntVar()
        self.__thirdCheckBoxStatus = tk.IntVar()
        self.__lightMode = True
        self.__allButton = []
        self.__allEntry = []
        self.__allLabels = []
        self.__allLabelFrames = []
        self.__informativeLabels = []
        self.__allCheckBoxes = []
        self.__allScales = []

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
        rightButton = Button(self.__rightButtonsFrame, text='right button',
                             height=1,
                             width=15, font=("Ariel", 10, 'bold'), bg='white')
        rightButton.pack(side='top')
        leftButton = Button(self.__leftButtonsFrame, text='left button',
                            height=1,
                            width=15, font=("Ariel", 10, 'bold'), bg='white')
        leftButton.pack(side='top')

        for index in range(1):
            space = Label(self.__leftButtonsFrame, text="", bg='gray92')
            space.pack(side='bottom')
            self.__allLabels.append(space)

        for index in range(1):
            space = Label(self.__rightButtonsFrame, text="", bg='gray92')
            space.pack(side='bottom')
            self.__allLabels.append(space)

        self.__allButton.append(rightButton)
        self.__allButton.append(leftButton)

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
        entryLabel = Label(entryLabelFrame, text='Insert Input:',
                           bg='gray91',
                           fg='black', font=("Ariel", 9, 'bold'))
        self.__allLabels.append(entryLabel)
        entryPlace = Entry(entryLabelFrame,
                           textvariable=self.__firstArgument, bd=2)
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
        firstArgument = self.__firstArgument.get()
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
        firstCheckBox = Checkbutton(self.__leftButtonsFrame, text='First Plot',
                                    variable=self.__firstCheckBoxStatus,
                                    bg='gray92', fg='red')
        firstCheckBox.pack(side='top')
        self.__allCheckBoxes.append(firstCheckBox)

        secondCheckBox = Checkbutton(self.__leftButtonsFrame,
                                     text='Second Plot',
                                     variable=self.__secondCheckBoxStatus,
                                     bg='gray92', fg='red')
        secondCheckBox.pack(side='top')
        self.__allCheckBoxes.append(secondCheckBox)

        thirdCheckBox = Checkbutton(self.__leftButtonsFrame, text='Third Plot',
                                    variable=self.__thirdCheckBoxStatus,
                                    bg='gray92', fg='red')
        thirdCheckBox.pack(side='top')
        self.__allCheckBoxes.append(thirdCheckBox)

    def grid_scales(self):
        k_in_label = Label(self.__middleTopFrame, text="K-In:",
                           bg='gray91', fg='black', font=("Ariel", 9, 'bold'))
        k_in_scale = Scale(self.__middleTopFrame, from_=0, to=100,
                           orient=HORIZONTAL)
        k_in_scale.set(50)
        k_in_label.pack(side='left')
        k_in_scale.pack(side='left')
        self.__allLabels.append(k_in_label)

        k_out_label = Label(self.__middleTopFrame,
                            text="K-Out:", bg='gray91',
                            fg='black', font=("Ariel", 9, 'bold'))

        k_out_scale = Scale(self.__middleTopFrame, from_=0, to=100,
                            orient=HORIZONTAL)
        k_out_scale.set(50)
        k_out_label.pack(side='left')
        k_out_scale.pack(side='left')
        self.__allLabels.append(k_out_label)

        self.__allScales.append(k_in_scale)
        self.__allScales.append(k_out_scale)


def main():
    root = Tk()
    program = Gui_3D_Bio(root)
    program.root_init()
    program.grid_buttons()
    program.grid_plot_checkboxes()
    program.grid_entry()
    program.grid_scales()
    program.change_mode_button()
    root.title("Hackathon Program")
    root.geometry('800x800')
    root.resizable(False, False)
    root.mainloop()
