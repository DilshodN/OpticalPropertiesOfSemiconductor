# def importFile(self):
#     filename = filedialog.askopenfilename()
#     self.experimentalFreq, self.experimentalOpticalDensity = parser.parseASCII(filename)
#
#
# def plotExperimentalData(self):
#     fig = Figure(figsize=(7, 5), dpi=100)
#
#     plotter = fig.add_subplot(111)
#     plotter.plot(self.experimentalFreq, self.experimentalOpticalDensity)
#     plotter.set_xlabel(r'Frequency [sm^(-1)]')
#     plotter.set_ylabel(r'Optical density')
#
#     canvas = FigureCanvasTkAgg(fig, master=self)
#     canvas.draw()
#     canvas.get_tk_widget().pack()

from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Load the UI Page
        uic.loadUi('./qtUI/mainWindow.ui', self)

        self.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [30, 32, 34, 32, 33, 31, 29, 32, 35, 45])

    def plot(self, hour, temperature):
        self.graphWidget.plot(hour, temperature)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
