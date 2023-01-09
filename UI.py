# tkinter
import tkinter as tk
from tkinter import filedialog

# calculations & plot
import matplotlib
import numpy as np

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

# Our files
import parser


class App(tk.Tk):
    def __init__(self, height=800, width=600):
        super().__init__()
        # Tkinter
        self.title("Optical Properties of Semiconductor")
        self.geometry(f'{height}x{width}')

        # self.canvas = tk.Canvas(self, width=width, height=height, bg='white')
        # self.canvas.pack()
        # Buttons
        importFileButton = tk.Button(self, text='Import file', command=self.importFile)
        importFileButton.pack()

        drawExperimentalData = tk.Button(self, text='Plot data', command=self.plotExperimentalData)
        drawExperimentalData.pack()
        # Data
        self.experimentalFreq = None
        self.experimentalOpticalDensity = None

    def importFile(self):
        filename = filedialog.askopenfilename()
        self.experimentalFreq, self.experimentalOpticalDensity = parser.parseASCII(filename)

    def plotExperimentalData(self):
        fig = Figure(figsize=(7, 5), dpi=100)

        plotter = fig.add_subplot(111)
        plotter.plot(self.experimentalFreq, self.experimentalOpticalDensity)
        plotter.set_xlabel(r'Frequency [sm^(-1)]')
        plotter.set_ylabel(r'Optical density')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()


app = App()

app.mainloop()
