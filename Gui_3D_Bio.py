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
        self.__lightMode = True
        self.__allButton = []
        self.__allEntry = []
        self.__allLabels = []
        self.__allLabelFrames = []

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

        changeModeButton = Button(self.__leftButtonsFrame,
                                  text='Dark/Light Mode',
                                  height=1,
                                  width=15, font=("Ariel", 10, 'bold'),
                                  bg='white',
                                  command=lambda: self.dark_light_switch())
        changeModeButton.pack(side='top')

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

        entryLabelFrame.pack(padx=7, pady=7)
        entryLabel.pack(side='top')
        entryPlace.pack(side='top')

        for index in range(1):
            space = Label(entryLabelFrame, text="", bg='gray91')
            space.pack(side='top')
            self.__allLabels.append(space)

        submitButton.pack(side='top')

    def submit_input(self):
        firstArgument = self.__firstArgument.get()
        print(firstArgument)

    def dark_light_switch(self):

        if self.__lightMode:
            self.__titleFrame.configure(background='gray20')
            self.__leftButtonsFrame.configure(background='gray17')
            self.__rightButtonsFrame.configure(background='gray17')
            self.__middleTopFrame.configure(background='gray18')
            self.__middleBottomFrame.configure(background='gray22')
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
            self.__lightMode = False
        else:
            self.__titleFrame.configure(background='gray98')
            self.__leftButtonsFrame.configure(background='gray92')
            self.__rightButtonsFrame.configure(background='gray92')
            self.__middleTopFrame.configure(background='gray91')
            self.__middleBottomFrame.configure(background='gray94')
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
            self.__lightMode = True


def main():
    root = Tk()
    program = Gui_3D_Bio(root)
    program.root_init()
    program.grid_buttons()
    program.grid_entry()
    root.title("Hackathon Program")
    root.geometry('800x800')
    root.resizable(False, False)
    root.mainloop()
