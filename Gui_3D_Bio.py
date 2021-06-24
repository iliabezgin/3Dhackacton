from tkinter import *
import tkinter as tk

# import main_model
# import plots
# from PIL import ImageTk, Image


def quit_program():
    quit()


# def pop_up_plot_window(path):
#     window = tk.Toplevel()
#     window.wm_title("Plot")
#     window.configure(background='grey')
#
#     img = ImageTk.PhotoImage(Image.open(path))
#     image_label = Label(window, image=img)
#     image_label.photo = img
#     image_label.pack()


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

    def normalLabelCreateAndPack(self, frame, side, text, font, bg, fg):
        title = Label(frame, text=text, font=font, bg=bg, fg=fg)
        title.pack(side=side)
        self._allLabels.append(title)
        return title

    def informativeLabelCreateAndPack(self, frame, text, fg, bg, font, side):
        invalidInputLabel = Label(frame, text=text, fg=fg, bg=bg, font=font)
        invalidInputLabel.pack(side=side)
        self._informativeLabels.append(invalidInputLabel)

        return invalidInputLabel

    def buttonCreateAndPack(self, frame, text, height, width, font, bg, command, side):
        button = Button(frame, text=text, height=height, width=width, font=font, bg=bg, command=command)
        button.pack(side=side)
        self._allButton.append(button)
        return button

    def labelFrameCreation(self, frame, text, fg, bg, font, side):
        labelFrame = LabelFrame(frame, text=text, fg=fg, bg=bg, font=font)
        self._allLabelFrames.append(labelFrame)
        labelFrame.pack(side=side)

        return labelFrame

    def entryCreateAndPack(self, frame, textVariable, bd, side):
        entryPlace = Entry(frame, textvariable=textVariable, bd=bd)
        self._allEntry.append(entryPlace)
        entryPlace.pack(side=side)

        return entryPlace

    def checkBoxCreateAndPack(self, frame, text, variable, bg, fg, font, side):
        checkBox = Checkbutton(frame, text=text, variable=variable, bg=bg, fg=fg, font=font)
        checkBox.pack(side=side)
        self._allCheckBoxes.append(checkBox)

        return checkBox

    def spaceCreation(self, frame, amount, side, bg):
        for index in range(amount):
            space = Label(frame, text="", bg=bg)
            space.pack(side=side)
            self._allLabels.append(space)

    def titleCreation(self):
        self.normalLabelCreateAndPack(self._titleFrame, 'top', 'Membraneless Organelles Final Project',
                                      ("Linux Libertine Mono O", 15, 'bold'), 'light blue', 'black')

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
                                 lambda: self.darkLightSwitch(), 'top')

        self.spaceCreation(self._leftButtonsFrame, 3, 'top', 'light blue')

        self.buttonCreateAndPack(self._leftButtonsFrame, 'Exit', 1, 15, ("Ariel", 10, 'bold'), 'white',
                                 lambda: quit(), 'top')

    def gridEntry(self):
        entryLabelFrame = self.labelFrameCreation(self._middleTopFrame, 'Program Input', 'black', 'light blue',
                                                  ("Ariel", 10, 'normal'), 'left')

        self.normalLabelCreateAndPack(entryLabelFrame, 'top', 'Enter Sequence:', ("Ariel", 9, 'bold'),
                                      'light blue', 'black')

        self.entryCreateAndPack(entryLabelFrame, self._givenSequence, 2, 'top')

        self.spaceCreation(entryLabelFrame, 1, 'top', 'light blue')

        self.buttonCreateAndPack(entryLabelFrame, 'Start Simulation', 1, 15, ("Ariel", 10, 'bold'),
                                 'white', lambda: self.submitInput(), 'top')

    def checkValidity(self):
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

    def submitInput(self):
        random_init_flag = False
        random_diff_type = False

        for label in self._informativeLabels:
            label.pack_forget()

        if not self.checkValidity():
            self.informativeLabelCreateAndPack(self._middleBottomFrame,
                                               'Invalid Input Given. Hint: Negative Argument',
                                               'blue', 'grey93', ("Ariel", 10, 'normal'), 'top')
            return

        self.informativeLabelCreateAndPack(self._middleBottomFrame, 'Running Simulation!', 'blue', 'grey93',
                                           ("Ariel", 10, 'normal'), side='top')

        if self._randomInitCheckBoxStatus.get() == 1:
            random_init_flag = True

        if self._diffChainsCheckBoxStatus.get() == 1:
            random_diff_type = True

        # T_ns, E, D, chains_on_iteration = main_model.create_model(self._givenSequence.get(), self._chainsNumber.get(),
        #                                                           self._locationToSave.get(),
        #                                                           self._beadRadiusSize.get(),
        #                                                           self._sphereRadiusSize.get(),
        #                                                           self._kbsValue.get(), self._aminoAmount.get(),
        #                                                           self._kInSize.get(), self._kOutSize.get(),
        #                                                           random_init_flag, random_diff_type)
        #
        # if self._firstCheckBoxStatus.get() == 1:
        #     self.informativeLabelCreateAndPack(self._middleBottomFrame, 'Generating Energy Over Time Plot...',
        #                                        'blue', 'grey93', ("Ariel", 9, 'normal'), 'top')
        #     plots.simulation_energy_over_time(E, T_ns, 1)
        #     pop_up_plot_window("energy_graph.png")
        #
        # if self._secondCheckBoxStatus.get() == 1:
        #     self.informativeLabelCreateAndPack(self._middleBottomFrame, 'Generating End To End Over Time Plot...',
        #                                        'blue', 'grey93', ("Ariel", 9, 'normal'), 'top')
        #     plots.end_to_end_distances_over_time(D, T_ns, 1)
        #     pop_up_plot_window("distances_graph.png")
        #
        # if self._thirdCheckBoxStatus.get() == 1:
        #     self.informativeLabelCreateAndPack(self._middleBottomFrame,
        #                                        'Generating Distribution Of Energy Over Time Plot...', 'blue', 'grey93',
        #                                        ("Ariel", 9, 'normal'), 'top')
        #     plots.distribution_of_energy_over_time(E, T_ns, 1)
        #     pop_up_plot_window("dist_of_E.png")
        #
        # if self._fourthCheckBoxStatus.get() == 1:
        #     self.informativeLabelCreateAndPack(self._middleBottomFrame,
        #                                        'Generating Distribution Of Distances Over Time Plot...', 'blue',
        #                                        'grey93', ("Ariel", 9, 'normal'), 'top')
        #     plots.distribution_of_dist_over_time(D)
        #     pop_up_plot_window("dist_of_D.png")
        #
        # if self._fifthCheckBoxStatus.get() == 1:
        #     self.informativeLabelCreateAndPack(self._middleBottomFrame, 'Generating Distribution Of Bead Locations...',
        #                                        'blue', 'grey93', ("Ariel", 9, 'normal'), 'top')
        #     plots.distribution_of_beads_locations(chains_on_iteration, T_ns, 1)
        #     pop_up_plot_window("variance_of_centers.png")

        self.informativeLabelCreateAndPack(self._middleBottomFrame, 'Simulating is Over, Check Out Your Plots', 'blue',
                                           'grey93', ("Ariel", 10, 'normal'), 'top')

    def configureFramesToDark(self):
        self._titleFrame.configure(background='gray20')
        self._leftButtonsFrame.configure(background='gray20')
        self._rightButtonsFrame.configure(background='gray20')
        self._middleTopFrame.configure(background='gray20')
        self._lowBorder.configure(background='gray20')

    def configureWidgetsToDark(self):

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

    def configureFramesToLight(self):
        self._titleFrame.configure(background='light blue')
        self._leftButtonsFrame.configure(background='light blue')
        self._rightButtonsFrame.configure(background='light blue')
        self._middleTopFrame.configure(background='light blue')
        self._lowBorder.configure(background='light blue')

    def configureWidgetsToLight(self):

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

    def darkLightSwitch(self):

        if self._lightMode:
            self.configureFramesToDark()
            self.configureWidgetsToDark()
            self._lightMode = False

        else:
            self.configureFramesToLight()
            self.configureWidgetsToLight()
            self._lightMode = True

    def gridPlotCheckboxes(self):

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Select Your Plots:', ("Ariel", 9, 'normal'),
                                      bg='light blue', fg='black')

        self.spaceCreation(self._rightButtonsFrame, 1, 'top', 'light blue')

        self.checkBoxCreateAndPack(self._rightButtonsFrame, 'Energy Over Time', self._firstCheckBoxStatus,
                                   'light blue', 'red', ("Ariel", 7, 'normal'), 'top')

        self.checkBoxCreateAndPack(self._rightButtonsFrame, 'End to End Distances', self._secondCheckBoxStatus,
                                   'light blue', 'red', ("Ariel", 7, 'normal'), 'top')

        self.checkBoxCreateAndPack(self._rightButtonsFrame, 'Energy Distribution', self._thirdCheckBoxStatus,
                                   'light blue', 'red', ("Ariel", 7, 'normal'), 'top')

        self.checkBoxCreateAndPack(self._rightButtonsFrame, 'Location Distribution', self._fourthCheckBoxStatus,
                                   'light blue', 'red', ("Ariel", 7, 'normal'), 'top')

        self.checkBoxCreateAndPack(self._rightButtonsFrame, 'Beads Location', self._fifthCheckBoxStatus, 'light blue',
                                   'red', ("Ariel", 7, 'normal'), 'top')

    def gridArguments(self):
        kInLabelFrame = self.labelFrameCreation(self._middleTopFrame, 'Argument 1:', 'black', 'light blue',
                                                ("Ariel", 10, 'normal'), 'left')

        kOutLabelFrame = self.labelFrameCreation(self._middleTopFrame, 'Argument 2:', 'black', 'light blue',
                                                 ("Ariel", 10, 'normal'), 'left')

        self.normalLabelCreateAndPack(kInLabelFrame, 'left', "K-In:", ("Ariel", 9, 'bold'), 'light blue', 'black')

        self.entryCreateAndPack(kInLabelFrame, self._kInSize, 2, 'left')

        self.normalLabelCreateAndPack(kOutLabelFrame, 'left', "K-Out:", ("Ariel", 9, 'bold'), 'light blue', 'black')

        self.entryCreateAndPack(kOutLabelFrame, self._kOutSize, 2, 'left')

    def gridLeftSideWidgets(self):

        entryLabelFrame = self.labelFrameCreation(self._leftButtonsFrame, 'Output Save Location', 'black', 'light blue',
                                                  ("Ariel", 10, 'normal'), 'top')

        self.normalLabelCreateAndPack(entryLabelFrame, 'top', 'Enter Name For RMF:', ("Ariel", 9, 'bold'), 'light blue',
                                      'black')

        self.entryCreateAndPack(entryLabelFrame, self._locationToSave, 2, 'top')

        self.spaceCreation(self._leftButtonsFrame, 1, 'top', 'light blue')

        beadRadiusLabelFrame = self.labelFrameCreation(self._leftButtonsFrame, 'Argument 3:', 'black', 'light blue',
                                                       ("Ariel", 10, 'normal'), 'top')

        self.normalLabelCreateAndPack(beadRadiusLabelFrame, 'top', "Enter Bead Radius:", ("Ariel", 9, 'bold'),
                                      'light blue', 'black')

        self.entryCreateAndPack(beadRadiusLabelFrame, self._beadRadiusSize, 2, 'top')

        self.spaceCreation(self._leftButtonsFrame, 1, 'top', 'light blue')

        sphereRadiusLabelFrame = self.labelFrameCreation(self._leftButtonsFrame, 'Argument 4:', 'black', 'light blue',
                                                         ("Ariel", 10, 'normal'), 'top')

        self.normalLabelCreateAndPack(sphereRadiusLabelFrame, 'top', "Enter Sphere Radius:", ("Ariel", 9, 'bold'),
                                      'light blue', 'black')

        self.entryCreateAndPack(sphereRadiusLabelFrame, self._sphereRadiusSize, 2, 'top')

        self.spaceCreation(self._leftButtonsFrame, 1, 'top', 'light blue')

        kbsLabelFrame = self.labelFrameCreation(self._leftButtonsFrame, 'Argument 5:', 'black', 'light blue',
                                                ("Ariel", 10, 'normal'), 'top')

        self.normalLabelCreateAndPack(kbsLabelFrame, 'top', "Enter KBS:", ("Ariel", 9, 'bold'),
                                      'light blue', 'black')

        self.entryCreateAndPack(kbsLabelFrame, self._kbsValue, 2, 'top')

        self.spaceCreation(self._leftButtonsFrame, 1, 'top', 'light blue')

        chainsNumberLabelFrame = self.labelFrameCreation(self._leftButtonsFrame, 'Argument 6:', 'black', 'light blue',
                                                         ("Ariel", 10, 'normal'), 'top')

        self.normalLabelCreateAndPack(chainsNumberLabelFrame, 'top', "Enter Number Of Chains:", ("Ariel", 9, 'bold'),
                                      'light blue', 'black')

        self.entryCreateAndPack(chainsNumberLabelFrame, self._chainsNumber, 2, 'top')

        self.spaceCreation(self._leftButtonsFrame, 1, 'top', 'light blue')

        aminoNumberLabelFrame = self.labelFrameCreation(self._leftButtonsFrame, 'Argument 7:', 'black', 'light blue',
                                                        ("Ariel", 10, 'normal'), 'top')

        self.normalLabelCreateAndPack(aminoNumberLabelFrame, 'top', "Amino Acid Number:", ("Ariel", 9, 'bold'),
                                      'light blue', 'black')

        self.entryCreateAndPack(aminoNumberLabelFrame, self._aminoAmount, 2, 'top')

        self.spaceCreation(self._leftButtonsFrame, 1, 'top', 'light blue')

    def gridInstructions(self):

        self.spaceCreation(self._rightButtonsFrame, 2, 'top', 'light blue')

        randomInitLabelFrame = self.labelFrameCreation(self._rightButtonsFrame, 'Argument 8:', 'black', 'light blue',
                                                       ("Ariel", 10, 'normal'), 'top')

        self.checkBoxCreateAndPack(randomInitLabelFrame, 'Is Centered?', self._randomInitCheckBoxStatus,
                                   'light blue', 'red', ("Ariel", 7, 'normal'), 'top')

        self.spaceCreation(self._rightButtonsFrame, 1, 'top', 'light blue')

        self.spaceCreation(self._rightButtonsFrame, 2, 'top', 'light blue')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Quick Instructions:', ("Ariel", 10, 'normal'),
                                      'light blue', 'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Step One:', ("Ariel", 10, 'normal'),
                                      'light blue', 'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Fill All The Arguments 1-8',
                                      ("Ariel", 7, 'normal'), 'light blue', 'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Step Two:',
                                      ("Ariel", 10, 'normal'), 'light blue', 'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Fill Your File Name',
                                      ("Ariel", 7, 'normal'), 'light blue', 'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Step Three:',
                                      ("Ariel", 10, 'normal'), 'light blue', 'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Fill Your Sequence',
                                      ("Ariel", 7, 'normal'), 'light blue', 'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Step Four:',
                                      ("Ariel", 10, 'normal'), 'light blue', 'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Press "Start Simulator"',
                                      ("Ariel", 7, 'normal'), 'light blue', 'black')

        self.spaceCreation(self._rightButtonsFrame, 1, 'top', 'light blue')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Enjoy!', ("Ariel", 10, 'normal'), 'light blue',
                                      'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Ilia Bezgin', ("Ariel", 6, 'normal'),
                                      'light blue', 'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Rina Karnauch', ("Ariel", 6, 'normal'),
                                      'light blue', 'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Roy Maman', ("Ariel", 6, 'normal'),
                                      'light blue', 'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'Ofek Kaveh', ("Ariel", 6, 'normal'),
                                      'light blue', 'black')

        self.normalLabelCreateAndPack(self._rightButtonsFrame, 'top', 'By:', ("Ariel", 6, 'normal'),
                                      'light blue', 'black')


def gui_buttons_and_design_init(program):
    program.mainFramesInit()
    program.gridPlotCheckboxes()
    program.gridEntry()
    program.gridArguments()
    program.gridLeftSideWidgets()
    program.gridInstructions()
    program.changeModeButton()


def main():
    root = Tk()
    program = Gui_3D_Bio(root)
    gui_buttons_and_design_init(program)
    root.title("Hackathon Program")
    root.geometry('800x800')
    root.resizable(False, False)

    root.mainloop()
