# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../resources/ui/gui_crest.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CrestDialog(object):
    def setupUi(self, CrestDialog):
        CrestDialog.setObjectName("CrestDialog")
        CrestDialog.resize(400, 320)
        CrestDialog.setMinimumSize(QtCore.QSize(400, 320))
        CrestDialog.setMaximumSize(QtCore.QSize(400, 320))
        font = QtGui.QFont()
        font.setFamily("Arial")
        CrestDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CrestDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(CrestDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(CrestDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(CrestDialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_implicit = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_implicit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_implicit.setChecked(True)
        self.radioButton_implicit.setObjectName("radioButton_implicit")
        self.horizontalLayout_2.addWidget(self.radioButton_implicit)
        self.radioButton_user = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_user.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_user.setObjectName("radioButton_user")
        self.horizontalLayout_2.addWidget(self.radioButton_user)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(CrestDialog)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(CrestDialog)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 1, 1, 1)
        self.label = QtWidgets.QLabel(CrestDialog)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/crest_banner.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(CrestDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 10, 0, 1, 2)
        self.lineEdit_client_id = QtWidgets.QLineEdit(CrestDialog)
        self.lineEdit_client_id.setObjectName("lineEdit_client_id")
        self.gridLayout.addWidget(self.lineEdit_client_id, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(CrestDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(CrestDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 2)
        self.lineEdit_client_secret = QtWidgets.QLineEdit(CrestDialog)
        self.lineEdit_client_secret.setObjectName("lineEdit_client_secret")
        self.gridLayout.addWidget(self.lineEdit_client_secret, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(CrestDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 2)

        self.retranslateUi(CrestDialog)
        self.buttonBox.accepted.connect(CrestDialog.accept)
        self.buttonBox.rejected.connect(CrestDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CrestDialog)

    def retranslateUi(self, CrestDialog):
        _translate = QtCore.QCoreApplication.translate
        CrestDialog.setWindowTitle(_translate("CrestDialog", "CREST Configuration"))
        self.label_5.setText(_translate("CrestDialog", "<html><head/><body><p><span style=\" font-weight:600;\">CREST Client Details</span></p></body></html>"))
        self.groupBox.setTitle(_translate("CrestDialog", "Mode"))
        self.radioButton_implicit.setText(_translate("CrestDialog", "Implicit"))
        self.radioButton_user.setText(_translate("CrestDialog", "User-supplied details"))
        self.label_4.setText(_translate("CrestDialog", "<html><head/><body><p><a href=\"https://developers.eveonline.com/applications/\"><span style=\" text-decoration: underline; color:#0000ff;\">Get credentials</span></a></p></body></html>"))
        self.label_6.setText(_translate("CrestDialog", "<html><head/><body><p><a href=\"https://github.com/farshield/shortcircuit/blob/master/README.md#about-crest\"><span style=\" text-decoration: underline; color:#0000ff;\">Need more help?</span></a></p></body></html>"))
        self.label_2.setText(_translate("CrestDialog", "Client ID:"))
        self.label_3.setText(_translate("CrestDialog", "Client Secret:"))

from . import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CrestDialog = QtWidgets.QDialog()
    ui = Ui_CrestDialog()
    ui.setupUi(CrestDialog)
    CrestDialog.show()
    sys.exit(app.exec_())

