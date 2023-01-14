from PyQt5 import QtCore, QtGui, QtWidgets
from Tok_functions import InputVariables


class Ui_Dialog(object):
    def __init__(self):
        self.data = None

    def setupUi(self, Dialog, k):
        self.k = k
        self.dialog = Dialog
        Dialog.resize(957, 172)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 942, 154))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)

        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setText(f'{InputVariables.Ni[0]}')
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)

        self.textEdit_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_2.setText(f'{InputVariables.mi[0]}')
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 1, 1, 1, 1)

        self.textEdit_3 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_3.setText(f'{InputVariables.ei[0]}')
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")

        self.gridLayout.addWidget(self.textEdit_3, 1, 2, 1, 1)

        self.textEdit_4 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_4.setText(f'{InputVariables.vi[0]}')
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")

        self.gridLayout.addWidget(self.textEdit_4, 1, 3, 1, 1)

        self.textEdit_5 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_5.setText(f'{InputVariables.Gamma_i[0]}')
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")

        self.gridLayout.addWidget(self.textEdit_5, 1, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.returnVariables)
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setVariables(self, settings: InputVariables, k):
        self.textEdit.setText(f'{settings.Ni[k]}')
        self.textEdit_2.setText(f'{settings.mi[k]}')
        self.textEdit_3.setText(f'{settings.ei[k]}')
        self.textEdit_4.setText(f'{settings.vi[k]}')
        self.textEdit_5.setText(f'{settings.Gamma_i[k]}')

    def returnVariables(self):
        to_ret = self.textEdit.toPlainText(), self.textEdit_2.toPlainText(), self.textEdit_3.toPlainText(), \
                 self.textEdit_4.toPlainText(), self.textEdit_5.toPlainText()
        self.data = to_ret
        self.dialog.close()
        return to_ret

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", f"K={self.k}"))
        self.label_5.setText(_translate("Dialog", "Затухание колебаний [см^-1]"))
        self.label.setText(_translate("Dialog", "Концентрация cв.з. [см^-3]"))
        self.label_3.setText(_translate("Dialog", "Эффективный з.э. [m * 4.8 * 1e-10]"))
        self.label_2.setText(_translate("Dialog", "Масса св.з. [а. е. м.]"))
        self.label_4.setText(_translate("Dialog", "Частота колебаний [см^-1]"))

    def errorMessage(self, text='Error'):
        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.showMessage(text)


class KSettingsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None, k=1):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self, k)
