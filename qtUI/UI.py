from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlibwidget import MatplotlibWidget
import sys
import numpy as np
import ASCIIparser as parser
import Tok_functions
from GraphicsPlotter import GraphicPlotter, Graphics
from dialog_UI import KSettingsDialog
import csv

listOfTypes = [Graphics.REAL_PART_DIELECTRIC,
               Graphics.IMAG_PART_DIELECTRIC,
               Graphics.REAL_PART_REFRACTION,
               Graphics.IMAG_PART_REFLECTION,
               Graphics.R12,
               Graphics.PHASE_12,
               Graphics.ALPHA,
               Graphics.OPTICAL_DENS_SIMPLE,
               Graphics.TRANSPARENCY,
               Graphics.OPTICAL_DENS_HARD]


class Ui_MainWindow(object):
    def __init__(self):
        self.dataDict = {1: None, 2: None, 3: None, 4: None,
                         5: None, 6: None, 7: None, 8: None,
                         9: None, 10: None, 11: None}

        self.dataNormDict = {1: None, 2: None, 3: None, 4: None,
                             5: None, 6: None, 7: None, 8: None,
                             9: None, 10: None, 11: None}

        self.graphicsDict = {1: None, 2: None, 3: None, 4: None,
                             5: None, 6: None, 7: None, 8: None,
                             9: None, 10: None, 11: None}

        self.graphicsNormDict = {1: None, 2: None, 3: None, 4: None,
                                 5: None, 6: None, 7: None, 8: None,
                                 9: None, 10: None, 11: None}

        self.settings = Tok_functions.InputVariables()

        self.plotter = GraphicPlotter(self.settings)

        self.imported = False

        self.updateDataGraphs()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 689)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 689))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 751, 551))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.matplotlibLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.matplotlibLayout.setContentsMargins(0, 0, 0, 0)
        self.matplotlibLayout.setObjectName("matplotlibLayout")
        self.MatplotlibWidget = MatplotlibWidget(self.gridLayoutWidget_2)
        self.MatplotlibWidget.setObjectName("MatplotlibWidget")
        self.matplotlibLayout.addWidget(self.MatplotlibWidget, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(770, 10, 491, 651))
        self.widget.setObjectName("widget")
        self.rhsLayout = QtWidgets.QVBoxLayout(self.widget)
        self.rhsLayout.setContentsMargins(0, 0, 0, 0)
        self.rhsLayout.setObjectName("rhsLayout")
        self.GraphicNormLabelLayout = QtWidgets.QHBoxLayout()
        self.GraphicNormLabelLayout.setObjectName("GraphicNormLabelLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.GraphicNormLabelLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.GraphicNormLabelLayout.addWidget(self.label_2)
        self.rhsLayout.addLayout(self.GraphicNormLabelLayout)
        self.EnumCheckBoxesLayout = QtWidgets.QHBoxLayout()
        self.EnumCheckBoxesLayout.setObjectName("EnumCheckBoxesLayout")
        self.enumLayout = QtWidgets.QVBoxLayout()
        self.enumLayout.setObjectName("enumLayout")
        self.label_num1 = QtWidgets.QLabel(self.widget)
        self.label_num1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_num1.setObjectName("label_num1")
        self.enumLayout.addWidget(self.label_num1)
        self.label_num2 = QtWidgets.QLabel(self.widget)
        self.label_num2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_num2.setObjectName("label_num2")
        self.enumLayout.addWidget(self.label_num2)
        self.label_num3 = QtWidgets.QLabel(self.widget)
        self.label_num3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_num3.setObjectName("label_num3")
        self.enumLayout.addWidget(self.label_num3)
        self.label_num4 = QtWidgets.QLabel(self.widget)
        self.label_num4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_num4.setObjectName("label_num4")
        self.enumLayout.addWidget(self.label_num4)
        self.label_num5 = QtWidgets.QLabel(self.widget)
        self.label_num5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_num5.setObjectName("label_num5")
        self.enumLayout.addWidget(self.label_num5)
        self.label_num6 = QtWidgets.QLabel(self.widget)
        self.label_num6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_num6.setObjectName("label_num6")
        self.enumLayout.addWidget(self.label_num6)
        self.label_num7 = QtWidgets.QLabel(self.widget)
        self.label_num7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_num7.setObjectName("label_num7")
        self.enumLayout.addWidget(self.label_num7)
        self.label_num8 = QtWidgets.QLabel(self.widget)
        self.label_num8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_num8.setObjectName("label_num8")
        self.enumLayout.addWidget(self.label_num8)
        self.label_num9 = QtWidgets.QLabel(self.widget)
        self.label_num9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_num9.setObjectName("label_num9")
        self.enumLayout.addWidget(self.label_num9)
        self.label_num10 = QtWidgets.QLabel(self.widget)
        self.label_num10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_num10.setObjectName("label_num10")
        self.enumLayout.addWidget(self.label_num10)
        self.label_num11 = QtWidgets.QLabel(self.widget)
        self.label_num11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_num11.setObjectName("label_num11")
        self.enumLayout.addWidget(self.label_num11)
        self.EnumCheckBoxesLayout.addLayout(self.enumLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_1 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout.addWidget(self.checkBox_8)
        self.checkBox_9 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout.addWidget(self.checkBox_9)
        self.checkBox_10 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout.addWidget(self.checkBox_10)
        self.checkBox_11 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.checkBox_11.setFont(font)
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout.addWidget(self.checkBox_11)
        self.EnumCheckBoxesLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_norm_1 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_norm_1.setText("")
        self.checkBox_norm_1.setObjectName("checkBox_norm_1")
        self.verticalLayout_2.addWidget(self.checkBox_norm_1)
        self.checkBox_norm_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_norm_2.setText("")
        self.checkBox_norm_2.setObjectName("checkBox_norm_2")
        self.verticalLayout_2.addWidget(self.checkBox_norm_2)
        self.checkBox_norm_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_norm_3.setText("")
        self.checkBox_norm_3.setObjectName("checkBox_norm_3")
        self.verticalLayout_2.addWidget(self.checkBox_norm_3)
        self.checkBox_norm_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_norm_4.setText("")
        self.checkBox_norm_4.setObjectName("checkBox_norm_4")
        self.verticalLayout_2.addWidget(self.checkBox_norm_4)
        self.checkBox_norm_5 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_norm_5.setText("")
        self.checkBox_norm_5.setObjectName("checkBox_norm_5")
        self.verticalLayout_2.addWidget(self.checkBox_norm_5)
        self.checkBox_norm_6 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_norm_6.setText("")
        self.checkBox_norm_6.setObjectName("checkBox_norm_6")
        self.verticalLayout_2.addWidget(self.checkBox_norm_6)
        self.checkBox_norm_7 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_norm_7.setText("")
        self.checkBox_norm_7.setObjectName("checkBox_norm_7")
        self.verticalLayout_2.addWidget(self.checkBox_norm_7)
        self.checkBox_norm_8 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_norm_8.setText("")
        self.checkBox_norm_8.setObjectName("checkBox_norm_8")
        self.verticalLayout_2.addWidget(self.checkBox_norm_8)
        self.checkBox_norm_9 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_norm_9.setText("")
        self.checkBox_norm_9.setObjectName("checkBox_norm_9")
        self.verticalLayout_2.addWidget(self.checkBox_norm_9)
        self.checkBox_norm_10 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_norm_10.setText("")
        self.checkBox_norm_10.setObjectName("checkBox_norm_10")
        self.verticalLayout_2.addWidget(self.checkBox_norm_10)
        self.checkBox_norm_11 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_norm_11.setText("")
        self.checkBox_norm_11.setObjectName("checkBox_norm_11")
        self.verticalLayout_2.addWidget(self.checkBox_norm_11)
        self.EnumCheckBoxesLayout.addLayout(self.verticalLayout_2)
        self.rhsLayout.addLayout(self.EnumCheckBoxesLayout)
        self.ParamsLayout = QtWidgets.QHBoxLayout()
        self.ParamsLayout.setObjectName("ParamsLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.n0Label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.n0Label.setFont(font)
        self.n0Label.setObjectName("n0Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.n0Label)
        self.n0LineEdit = QtWidgets.QLineEdit(self.widget)
        self.n0LineEdit.setText("")
        self.n0LineEdit.setObjectName("n0LineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.n0LineEdit)
        self.m0Label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.m0Label.setFont(font)
        self.m0Label.setObjectName("m0Label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.m0Label)
        self.m0LineEdit = QtWidgets.QLineEdit(self.widget)
        self.m0LineEdit.setObjectName("m0LineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.m0LineEdit)
        self.gamma0Label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.gamma0Label.setFont(font)
        self.gamma0Label.setObjectName("gamma0Label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.gamma0Label)
        self.gamma0LineEdit = QtWidgets.QLineEdit(self.widget)
        self.gamma0LineEdit.setObjectName("gamma0LineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gamma0LineEdit)
        self.e_infLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.e_infLabel.setFont(font)
        self.e_infLabel.setObjectName("e_infLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.e_infLabel)
        self.e_infLineEdit = QtWidgets.QLineEdit(self.widget)
        self.e_infLineEdit.setObjectName("e_infLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.e_infLineEdit)
        self.kLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.kLabel.setFont(font)
        self.kLabel.setObjectName("kLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.kLabel)
        self.dLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.dLabel.setFont(font)
        self.dLabel.setObjectName("dLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.dLabel)
        self.dLineEdit = QtWidgets.QLineEdit(self.widget)
        self.dLineEdit.setObjectName("dLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.dLineEdit)
        self.nmLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.nmLabel.setFont(font)
        self.nmLabel.setObjectName("nmLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.nmLabel)
        self.nmLineEdit = QtWidgets.QLineEdit(self.widget)
        self.nmLineEdit.setObjectName("nmLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.nmLineEdit)
        self.kLineEdit = QtWidgets.QLineEdit(self.widget)
        self.kLineEdit.setObjectName("kLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.kLineEdit)
        self.ParamsLayout.addLayout(self.formLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.ParamsLayout.addLayout(self.verticalLayout_3)
        self.rhsLayout.addLayout(self.ParamsLayout)
        self.confirmSettingsBtn = QtWidgets.QPushButton(self.widget)
        self.confirmSettingsBtn.setObjectName("confirmSettingsBtn")
        self.rhsLayout.addWidget(self.confirmSettingsBtn)
        self.FreqsLayout = QtWidgets.QHBoxLayout()
        self.FreqsLayout.setObjectName("FreqsLayout")
        self.label_10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.FreqsLayout.addWidget(self.label_10)
        self.minFreqLineEdit = QtWidgets.QLineEdit(self.widget)
        self.minFreqLineEdit.setObjectName("minFreqLineEdit")
        self.FreqsLayout.addWidget(self.minFreqLineEdit)
        self.label_11 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.FreqsLayout.addWidget(self.label_11)
        self.maxFreqLineEdit = QtWidgets.QLineEdit(self.widget)
        self.maxFreqLineEdit.setObjectName("maxFreqLineEdit")
        self.FreqsLayout.addWidget(self.maxFreqLineEdit)
        self.label_12 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.FreqsLayout.addWidget(self.label_12)
        self.rhsLayout.addLayout(self.FreqsLayout)
        self.label_13 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("PT Mono")
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.rhsLayout.addWidget(self.label_13)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(0, 570, 761, 91))
        self.widget1.setObjectName("widget1")
        self.ButtonsLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.ButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonsLayout.setObjectName("ButtonsLayout")
        self.axesNorm = QtWidgets.QPushButton(self.widget1)
        self.axesNorm.setObjectName("axesNorm")
        self.ButtonsLayout.addWidget(self.axesNorm)
        self.ImExLayout = QtWidgets.QHBoxLayout()
        self.ImExLayout.setObjectName("ImExLayout")
        self.importBtn = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.importBtn.setFont(font)
        self.importBtn.setObjectName("importBtn")
        self.ImExLayout.addWidget(self.importBtn)
        self.paramsBtn = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.paramsBtn.setFont(font)
        self.paramsBtn.setObjectName("paramsBtn")
        self.ImExLayout.addWidget(self.paramsBtn)
        self.exportBtn = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.exportBtn.setFont(font)
        self.exportBtn.setObjectName("exportBtn")
        self.ImExLayout.addWidget(self.exportBtn)
        self.ButtonsLayout.addLayout(self.ImExLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setCheckable(False)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.checkBoxesGraphicsList = [self.checkBox_1, self.checkBox_2, self.checkBox_3,
                                       self.checkBox_4, self.checkBox_5, self.checkBox_6,
                                       self.checkBox_7, self.checkBox_8, self.checkBox_9,
                                       self.checkBox_10, self.checkBox_11]

        self.checkBoxesNormList = [self.checkBox_norm_1, self.checkBox_norm_2, self.checkBox_norm_3,
                                   self.checkBox_norm_4, self.checkBox_norm_5, self.checkBox_norm_6,
                                   self.checkBox_norm_7, self.checkBox_norm_8, self.checkBox_norm_9,
                                   self.checkBox_norm_10, self.checkBox_11]

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Графики"))
        self.label_2.setText(_translate("MainWindow", "Нормировка"))
        self.label_num1.setText(_translate("MainWindow", "1"))
        self.label_num2.setText(_translate("MainWindow", "2"))
        self.label_num3.setText(_translate("MainWindow", "3"))
        self.label_num4.setText(_translate("MainWindow", "4"))
        self.label_num5.setText(_translate("MainWindow", "5"))
        self.label_num6.setText(_translate("MainWindow", "6"))
        self.label_num7.setText(_translate("MainWindow", "7"))
        self.label_num8.setText(_translate("MainWindow", "8"))
        self.label_num9.setText(_translate("MainWindow", "9"))
        self.label_num10.setText(_translate("MainWindow", "10"))
        self.label_num11.setText(_translate("MainWindow", "11"))
        self.checkBox_1.setText(_translate("MainWindow", "Реальная часть диэлектрической проницаемости ε’(ν)"))
        self.checkBox_2.setText(_translate("MainWindow", "Мнимая часть диэлектрической проницаемости ε’’(ν)"))
        self.checkBox_3.setText(_translate("MainWindow", "Реальная часть показателя преломления n(ν)"))
        self.checkBox_4.setText(_translate("MainWindow", "Мнимая часть показателя преломления k(ν)"))
        self.checkBox_5.setText(_translate("MainWindow", "Коэффициент отражения по интенсивности R12(ν)"))
        self.checkBox_6.setText(_translate("MainWindow", "Фаза коэффициента отражения по амплитуде 𝜑12(𝜈)"))
        self.checkBox_7.setText(_translate("MainWindow", "Коэффициент поглощения (в обратных сантиметрах) 𝛼(𝜈)"))
        self.checkBox_8.setText(_translate("MainWindow", "Оптическая плотность плёнки (без учёта интерференции) D(ν)"))
        self.checkBox_9.setText(_translate("MainWindow", "Пропускание плёнки T(ν)"))
        self.checkBox_10.setText(_translate("MainWindow", "Оптическая плотность плёнки (с учётом интерференции) A(ν)"))
        self.checkBox_11.setText(_translate("MainWindow", "Импортированный экспериментальный спектр"))
        self.n0Label.setText(_translate("MainWindow", "N0"))
        self.m0Label.setText(_translate("MainWindow", "m"))
        self.gamma0Label.setText(_translate("MainWindow", "Gamma0"))
        self.e_infLabel.setText(_translate("MainWindow", "eps_inf"))
        self.kLabel.setText(_translate("MainWindow", "K"))
        self.dLabel.setText(_translate("MainWindow", "d"))
        self.nmLabel.setText(_translate("MainWindow", "Nm"))
        self.label_4.setText(_translate("MainWindow", "Концентрация с.н.з. (прим. \'1e10\') [см^-3]"))
        self.label_3.setText(_translate("MainWindow", "Масса с.н.з. (m * 9.1e-28)"))
        self.label_5.setText(_translate("MainWindow", "Затухание колебаний c.з. [см^-1]"))
        self.label_6.setText(_translate("MainWindow", "Д.п. для частот много больше фононных"))
        self.label_7.setText(_translate("MainWindow", "Количество мод (от 0 до 10)"))
        self.label_8.setText(_translate("MainWindow", "Толщина пленки [нм]"))
        self.label_9.setText(_translate("MainWindow", "Комплекский показ. прел. (прим. \'1+2j\' )"))
        self.confirmSettingsBtn.setText(_translate("MainWindow", "Применить"))
        self.label_10.setText(_translate("MainWindow", "Пределы частот:"))
        self.label_11.setText(_translate("MainWindow", "до"))
        self.label_12.setText(_translate("MainWindow", "[см^-1]"))
        self.label_13.setText(_translate("MainWindow", "Дилшод Нозимов и Андрей Токарев, 2023"))
        self.axesNorm.setText(_translate("MainWindow", "Отнормировать оси"))
        self.importBtn.setText(_translate("MainWindow", "Импортировать файл"))
        self.paramsBtn.setText(_translate("MainWindow", "Параметры мод"))
        self.exportBtn.setText(_translate("MainWindow", "Экспортировать в файл"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.n0LineEdit.setText(f"{self.settings.N0:.2e}")
        self.m0LineEdit.setText(f"{self.settings.m}")
        self.gamma0LineEdit.setText(f"{self.settings.Gamma0}")
        self.e_infLineEdit.setText(f"{self.settings.eps_inf}")
        self.dLineEdit.setText(f"{self.settings.d:.2e}")
        self.nmLineEdit.setText(f"{self.settings.Nm.real}+{self.settings.Nm.imag}j")
        self.kLineEdit.setText(f"{self.settings.K}")
        self.minFreqLineEdit.setText(f"{self.settings.freq_min}")
        self.maxFreqLineEdit.setText(f"{self.settings.freq_max}")

        self.importBtn.clicked.connect(self.importFileHandler)

        self.checkBox_1.toggled.connect(self.checkboxHandler1)
        self.checkBox_2.toggled.connect(self.checkboxHandler2)
        self.checkBox_3.toggled.connect(self.checkboxHandler3)
        self.checkBox_4.toggled.connect(self.checkboxHandler4)
        self.checkBox_5.toggled.connect(self.checkboxHandler5)
        self.checkBox_6.toggled.connect(self.checkboxHandler6)
        self.checkBox_7.toggled.connect(self.checkboxHandler7)
        self.checkBox_8.toggled.connect(self.checkboxHandler8)
        self.checkBox_9.toggled.connect(self.checkboxHandler9)
        self.checkBox_10.toggled.connect(self.checkboxHandler10)
        self.checkBox_11.toggled.connect(self.checkboxHandler11)
        self.checkBox_norm_1.toggled.connect(self.checkboxHandler1)
        self.checkBox_norm_2.toggled.connect(self.checkboxHandler2)
        self.checkBox_norm_3.toggled.connect(self.checkboxHandler3)
        self.checkBox_norm_4.toggled.connect(self.checkboxHandler4)
        self.checkBox_norm_5.toggled.connect(self.checkboxHandler5)
        self.checkBox_norm_6.toggled.connect(self.checkboxHandler6)
        self.checkBox_norm_7.toggled.connect(self.checkboxHandler7)
        self.checkBox_norm_8.toggled.connect(self.checkboxHandler8)
        self.checkBox_norm_9.toggled.connect(self.checkboxHandler9)
        self.checkBox_norm_10.toggled.connect(self.checkboxHandler10)
        self.checkBox_norm_11.toggled.connect(self.checkboxHandler11)

        self.paramsBtn.clicked.connect(self.settingsKButtonHandler)
        self.confirmSettingsBtn.clicked.connect(self.confirmSettingsBtnHandler)
        self.exportBtn.clicked.connect(self.exportBtnHandler)
        self.axesNorm.clicked.connect(self.normAxesBtnHandler)

        self.MatplotlibWidget.canvas.axes.grid()
        self.MatplotlibWidget.canvas.axes.set_xlabel("Частота [см^-1]")

    def updateDataGraphs(self):
        self.plotter.set_settings(self.settings)
        for i in range(10):
            self.dataDict[i + 1] = self.plotter.get_plot_data(listOfTypes[i])
            self.dataNormDict[i + 1] = self.plotter.get_plot_data(listOfTypes[i], True)

    def updateGraphs(self):
        for i in range(1, 11):
            if self.graphicsDict[i] is not None:
                self.removePlot(i)
                self.plot(*(self.dataDict[i]), i)

            if self.graphicsNormDict[i] is not None:
                self.removeNormPlot(i)
                self.plotNorm(*(self.dataNormDict[i]), i)
        self.MatplotlibWidget.canvas.draw()

    def plot(self, x, y, label):
        graphDetails = self.MatplotlibWidget.canvas.axes.plot(x, y, label=label)

        self.MatplotlibWidget.canvas.axes.legend()

        self.MatplotlibWidget.canvas.draw()

        self.graphicsDict[label] = graphDetails

    def plotNorm(self, x, y, label):
        graphDetails = self.MatplotlibWidget.canvas.axes.plot(x, y, label=str(label) + " norm")

        self.MatplotlibWidget.canvas.axes.set_ylim([0, 1])

        self.MatplotlibWidget.canvas.axes.legend()

        self.MatplotlibWidget.canvas.draw()

        self.graphicsNormDict[label] = graphDetails

    def removePlot(self, idx):
        if self.graphicsDict[idx] is None:
            return
        line = self.graphicsDict[idx].pop(0)
        line.remove()

        self.MatplotlibWidget.canvas.axes.legend()

        self.MatplotlibWidget.canvas.draw()
        self.graphicsDict[idx] = None

    def removeNormPlot(self, idx):
        if self.graphicsNormDict[idx] is None:
            return
        line = self.graphicsNormDict[idx].pop(0)
        line.remove()

        self.MatplotlibWidget.canvas.axes.legend()

        self.MatplotlibWidget.canvas.draw()
        self.graphicsNormDict[idx] = None

    def writeDataToDict(self, data, idx):
        self.dataDict[idx] = data

    def writeDataToNormDict(self, data, idx):
        self.dataNormDict[idx] = data

    def importFileHandler(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget)
        if filename == '':
            return
        try:
            importData = parser.parseASCII(filename)
        except Exception:
            self.errorMessage('You must choose ASCII file')
            return

        if importData is None:
            self.errorMessage('Invalid format of file')

        self.writeDataToDict(importData, 11)
        self.imported = True

        x, y = importData
        y_norm = Tok_functions.normalize(y)
        self.writeDataToNormDict((x, y_norm), 11)

    def checkboxHandler1(self):
        if not self.checkBox_1.isChecked() and not self.checkBox_norm_1.isChecked():
            if self.graphicsDict[1] is not None:
                self.removePlot(1)
            return
        elif self.checkBox_1.isChecked() and not self.checkBox_norm_1.isChecked():
            if self.graphicsNormDict[1] is not None:
                self.removeNormPlot(1)
            self.plot(*(self.dataDict[1]), 1)
        elif not self.checkBox_1.isChecked() and self.checkBox_norm_1.isChecked():
            if self.graphicsNormDict[1] is None:
                return
            else:
                self.removeNormPlot(1)
        else:
            if self.graphicsDict[1] is not None:
                self.removePlot(1)
            self.plotNorm(*(self.dataNormDict[1]), 1)

    def checkboxHandler2(self):
        if not self.checkBox_2.isChecked() and not self.checkBox_norm_2.isChecked():
            if self.graphicsDict[2] is not None:
                self.removePlot(2)
            return
        elif self.checkBox_2.isChecked() and not self.checkBox_norm_2.isChecked():
            if self.graphicsNormDict[2] is not None:
                self.removeNormPlot(2)
            self.plot(*(self.dataDict[2]), 2)
        elif not self.checkBox_2.isChecked() and self.checkBox_norm_2.isChecked():
            if self.graphicsNormDict[2] is None:
                return
            else:
                self.removeNormPlot(2)
        else:
            if self.graphicsDict[2] is not None:
                self.removePlot(2)
            self.plotNorm(*(self.dataNormDict[2]), 2)

    def checkboxHandler3(self):
        if not self.checkBox_3.isChecked() and not self.checkBox_norm_3.isChecked():
            if self.graphicsDict[3] is not None:
                self.removePlot(3)
            return
        elif self.checkBox_3.isChecked() and not self.checkBox_norm_3.isChecked():
            if self.graphicsNormDict[3] is not None:
                self.removeNormPlot(3)
            self.plot(*(self.dataDict[3]), 3)
        elif not self.checkBox_3.isChecked() and self.checkBox_norm_3.isChecked():
            if self.graphicsNormDict[3] is None:
                return
            else:
                self.removeNormPlot(3)
        else:
            if self.graphicsDict[3] is not None:
                self.removePlot(3)
            self.plotNorm(*(self.dataNormDict[3]), 3)

    def checkboxHandler4(self):
        if not self.checkBox_4.isChecked() and not self.checkBox_norm_4.isChecked():
            if self.graphicsDict[4] is not None:
                self.removePlot(4)
            return
        elif self.checkBox_4.isChecked() and not self.checkBox_norm_4.isChecked():
            if self.graphicsNormDict[4] is not None:
                self.removeNormPlot(4)
            self.plot(*(self.dataDict[4]), 4)
        elif not self.checkBox_4.isChecked() and self.checkBox_norm_4.isChecked():
            if self.graphicsNormDict[4] is None:
                return
            else:
                self.removeNormPlot(4)
        else:
            if self.graphicsDict[4] is not None:
                self.removePlot(4)
            self.plotNorm(*(self.dataNormDict[4]), 4)

    def checkboxHandler5(self):
        if not self.checkBox_5.isChecked() and not self.checkBox_norm_5.isChecked():
            if self.graphicsDict[5] is not None:
                self.removePlot(5)
            return
        elif self.checkBox_5.isChecked() and not self.checkBox_norm_5.isChecked():
            if self.graphicsNormDict[5] is not None:
                self.removeNormPlot(5)
            self.plot(*(self.dataDict[5]), 5)
        elif not self.checkBox_5.isChecked() and self.checkBox_norm_5.isChecked():
            if self.graphicsNormDict[5] is None:
                return
            else:
                self.removeNormPlot(5)
        else:
            if self.graphicsDict[5] is not None:
                self.removePlot(5)
            self.plotNorm(*(self.dataNormDict[5]), 5)

    def checkboxHandler6(self):
        if not self.checkBox_6.isChecked() and not self.checkBox_norm_6.isChecked():
            if self.graphicsDict[6] is not None:
                self.removePlot(6)
            return
        elif self.checkBox_6.isChecked() and not self.checkBox_norm_6.isChecked():
            if self.graphicsNormDict[6] is not None:
                self.removeNormPlot(6)
            self.plot(*(self.dataDict[6]), 6)
        elif not self.checkBox_6.isChecked() and self.checkBox_norm_6.isChecked():
            if self.graphicsNormDict[6] is None:
                return
            else:
                self.removeNormPlot(6)
        else:
            if self.graphicsDict[6] is not None:
                self.removePlot(6)
            self.plotNorm(*(self.dataNormDict[6]), 6)

    def checkboxHandler7(self):
        if not self.checkBox_7.isChecked() and not self.checkBox_norm_7.isChecked():
            if self.graphicsDict[7] is not None:
                self.removePlot(7)
            return
        elif self.checkBox_7.isChecked() and not self.checkBox_norm_7.isChecked():
            if self.graphicsNormDict[7] is not None:
                self.removeNormPlot(7)
            self.plot(*(self.dataDict[7]), 7)
        elif not self.checkBox_7.isChecked() and self.checkBox_norm_7.isChecked():
            if self.graphicsNormDict[7] is None:
                return
            else:
                self.removeNormPlot(7)
        else:
            if self.graphicsDict[7] is not None:
                self.removePlot(7)
            self.plotNorm(*(self.dataNormDict[7]), 7)

    def checkboxHandler8(self):
        if not self.checkBox_8.isChecked() and not self.checkBox_norm_8.isChecked():
            if self.graphicsDict[8] is not None:
                self.removePlot(8)
            return
        elif self.checkBox_8.isChecked() and not self.checkBox_norm_8.isChecked():
            if self.graphicsNormDict[8] is not None:
                self.removeNormPlot(8)
            self.plot(*(self.dataDict[8]), 8)
        elif not self.checkBox_8.isChecked() and self.checkBox_norm_8.isChecked():
            if self.graphicsNormDict[8] is None:
                return
            else:
                self.removeNormPlot(8)
        else:
            if self.graphicsDict[8] is not None:
                self.removePlot(8)
            self.plotNorm(*(self.dataNormDict[8]), 8)

    def checkboxHandler9(self):
        if not self.checkBox_9.isChecked() and not self.checkBox_norm_9.isChecked():
            if self.graphicsDict[9] is not None:
                self.removePlot(9)
            return
        elif self.checkBox_9.isChecked() and not self.checkBox_norm_9.isChecked():
            if self.graphicsNormDict[9] is not None:
                self.removeNormPlot(9)
            self.plot(*(self.dataDict[9]), 9)
        elif not self.checkBox_9.isChecked() and self.checkBox_norm_9.isChecked():
            if self.graphicsNormDict[9] is None:
                return
            else:
                self.removeNormPlot(9)
        else:
            if self.graphicsDict[9] is not None:
                self.removePlot(9)
            self.plotNorm(*(self.dataNormDict[9]), 9)

    def checkboxHandler10(self):
        if not self.checkBox_10.isChecked() and not self.checkBox_norm_10.isChecked():
            if self.graphicsDict[10] is not None:
                self.removePlot(10)
            return
        elif self.checkBox_10.isChecked() and not self.checkBox_norm_10.isChecked():
            if self.graphicsNormDict[10] is not None:
                self.removeNormPlot(10)
            self.plot(*(self.dataDict[10]), 10)
        elif not self.checkBox_10.isChecked() and self.checkBox_norm_10.isChecked():
            if self.graphicsNormDict[10] is None:
                return
            else:
                self.removeNormPlot(10)
        else:
            if self.graphicsDict[10] is not None:
                self.removePlot(10)
            self.plotNorm(*(self.dataNormDict[10]), 10)

    def checkboxHandler11(self):
        # 0 0 – no graphs
        # 1 0 - graph
        # 0 1 - no graph
        # 1 1 - norm graph
        # data is available
        if not self.imported:
            return
            # 0 0
        if not self.checkBox_11.isChecked() and not self.checkBox_norm_11.isChecked():
            # from 10
            if self.graphicsDict[11] is not None:
                self.removePlot(11)
            # from 01
            return
            # 1 0
        elif self.checkBox_11.isChecked() and not self.checkBox_norm_11.isChecked():
            # from 11
            if self.graphicsNormDict[11] is not None:
                self.removeNormPlot(11)
            # from 00
            self.plot(*(self.dataDict[11]), 11)
            # 0 1
        elif not self.checkBox_11.isChecked() and self.checkBox_norm_11.isChecked():
            # from 00
            if self.graphicsNormDict[11] is None:
                return
                # from 11
            else:
                self.removeNormPlot(11)
        # 1 1
        else:
            # from 10
            if self.graphicsDict[11] is not None:
                self.removePlot(11)
            self.plotNorm(*(self.dataNormDict[11]), 11)

    def settingsKButtonHandler(self):
        for k in range(self.settings.K):
            dlg = KSettingsDialog(MainWindow, k=(k + 1))
            dlg.exec()
            try:
                if 0 > float(dlg.ui.data[0]) > 1e23:
                    dlg.ui.errorMessage("Ni should be between 0 and 1e23")
                self.settings.Ni[k] = float(dlg.ui.data[0])

                if 1 > float(dlg.ui.data[1]) > 300:
                    dlg.ui.errorMessage("mi should be between 1 and 300")
                self.settings.mi[k] = float(dlg.ui.data[1])

                self.settings.ei[k] = float(dlg.ui.data[2])
                self.settings.vi[k] = float(dlg.ui.data[3])
                self.settings.Gamma_i[k] = float(dlg.ui.data[4])
            except ValueError or IndexError:
                dlg.close()
                self.errorMessage("Invalid Input")
                break
            except TypeError:
                break
        self.updateGraphs()

    def confirmSettingsBtnHandler(self):
        try:
            if 0 > float(self.n0LineEdit.text()) > 10e+22:
                self.errorMessage("N0 should be between 0 and 10e+22")

            self.settings.N0 = float(self.n0LineEdit.text())

            if float(self.m0LineEdit.text()) < 0:
                self.errorMessage("m should be > 0")

            self.settings.m = float(self.m0LineEdit.text())

            self.settings.Gamma0 = float(self.gamma0LineEdit.text())

            if 0 > float(self.e_infLineEdit.text()) > 100:
                self.errorMessage("eps_inf should be between 0 and 100")
            self.settings.eps_inf = float(self.e_infLineEdit.text())

            if 0 > int(self.kLineEdit.text()) > 10:
                self.errorMessage("K should be between 0 and 10")

            self.settings.K = int(self.kLineEdit.text())

            self.settings.Ni = np.zeros(self.settings.K)
            self.settings.mi = np.ones(self.settings.K)
            self.settings.ei = np.ones(self.settings.K)
            self.settings.vi = np.ones(self.settings.K) * 1100
            self.settings.Gamma_i = np.ones(self.settings.K) * 30

            self.settings.d = float(self.dLineEdit.text())

            self.settings.Nm = complex(self.nmLineEdit.text())

            self.settings.freq_min = float(self.minFreqLineEdit.text())

            self.settings.freq_max = float(self.maxFreqLineEdit.text())

            self.updateDataGraphs()

            self.updateGraphs()
            self.MatplotlibWidget.canvas.draw()

            self.normAxesBtnHandler()
        except ValueError:
            self.errorMessage("Invalid Input")

    def countNonNones(self):
        count = 0
        for elem in self.graphicsDict.values():
            if elem is not None:
                count += 1
        return count

    def findNotNoneIdx(self):
        value_list = list(self.graphicsDict.values())

        values = [item for item in value_list if item is not None]
        assert len(values) == 1
        idx = value_list.index(values[0])
        return idx

    def exportBtnHandler(self):
        count = self.countNonNones()
        if count == 0:
            self.errorMessage("No graphs to save")
            return
        elif count != 1:
            self.errorMessage("Must choose only 1 graph")
            return

        name, _ = QtWidgets.QFileDialog.getSaveFileName(self.centralwidget, 'Save File')
        file = open(name, 'w')

        x, y = self.dataDict.get(self.findNotNoneIdx() + 1)
        writer = csv.writer(file)
        writer.writerows(zip(x, y))
        file.close()

    def normAxesBtnHandler(self):
        indices = []
        for i in range(1, 12):
            if self.graphicsDict[i] is not None:
                indices.append(i)
        mins = []
        maxs = []
        if len(indices) == 0:
            return

        for idx in indices:
            mins.append(np.min(self.dataDict[idx][1]))
            maxs.append(np.max(self.dataDict[idx][1]))

        gmin, gmax = np.min(mins), np.max(maxs)

        if any(self.graphicsNormDict.values()):
            gmin = gmin if gmin < 0 else 0
            gmax = gmax if gmax > 1 else 1
        if abs(gmin - gmax) < 1e-7:
            delta = 0.1 * gmin
            gmin = gmin - delta
            gmax = gmax + delta
        delta = gmax - gmin
        self.MatplotlibWidget.canvas.axes.set_ylim([gmin - delta * 0.1, gmax + delta * 0.1])
        self.MatplotlibWidget.canvas.draw()

    def errorMessage(self, text='Error'):
        error_dialog = QtWidgets.QErrorMessage(self.centralwidget)
        error_dialog.showMessage(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
