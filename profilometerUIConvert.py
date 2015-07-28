# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profilometer.ui'
#
# Created: Tue Jul 28 16:15:15 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_formProfilometer(object):
    def setupUi(self, formProfilometer):
        formProfilometer.setObjectName(_fromUtf8("formProfilometer"))
        formProfilometer.resize(655, 489)
        self.buttonOrigin = QtGui.QPushButton(formProfilometer)
        self.buttonOrigin.setGeometry(QtCore.QRect(20, 350, 81, 41))
        self.buttonOrigin.setObjectName(_fromUtf8("buttonOrigin"))
        self.buttonStartStop = QtGui.QPushButton(formProfilometer)
        self.buttonStartStop.setGeometry(QtCore.QRect(40, 150, 110, 61))
        self.buttonStartStop.setObjectName(_fromUtf8("buttonStartStop"))
        self.frameProfileDisplay = QtGui.QFrame(formProfilometer)
        self.frameProfileDisplay.setGeometry(QtCore.QRect(210, 10, 431, 331))
        self.frameProfileDisplay.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameProfileDisplay.setFrameShadow(QtGui.QFrame.Raised)
        self.frameProfileDisplay.setObjectName(_fromUtf8("frameProfileDisplay"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.frameProfileDisplay)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 411, 311))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.layoutPlot = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.layoutPlot.setMargin(0)
        self.layoutPlot.setObjectName(_fromUtf8("layoutPlot"))
        self.graphicsViewPlot = QtGui.QGraphicsView(self.horizontalLayoutWidget)
        self.graphicsViewPlot.setObjectName(_fromUtf8("graphicsViewPlot"))
        self.layoutPlot.addWidget(self.graphicsViewPlot)
        self.lineProfilometerControlsSubstrteControls = QtGui.QFrame(formProfilometer)
        self.lineProfilometerControlsSubstrteControls.setGeometry(QtCore.QRect(10, 210, 191, 16))
        self.lineProfilometerControlsSubstrteControls.setFrameShape(QtGui.QFrame.HLine)
        self.lineProfilometerControlsSubstrteControls.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineProfilometerControlsSubstrteControls.setObjectName(_fromUtf8("lineProfilometerControlsSubstrteControls"))
        self.labelSubstrateControls = QtGui.QLabel(formProfilometer)
        self.labelSubstrateControls.setGeometry(QtCore.QRect(20, 230, 171, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelSubstrateControls.setFont(font)
        self.labelSubstrateControls.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSubstrateControls.setObjectName(_fromUtf8("labelSubstrateControls"))
        self.groupBoxTravelDirection = QtGui.QGroupBox(formProfilometer)
        self.groupBoxTravelDirection.setGeometry(QtCore.QRect(30, 90, 131, 51))
        self.groupBoxTravelDirection.setObjectName(_fromUtf8("groupBoxTravelDirection"))
        self.layoutWidget = QtGui.QWidget(self.groupBoxTravelDirection)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.layoutTravelDirection = QtGui.QHBoxLayout(self.layoutWidget)
        self.layoutTravelDirection.setMargin(0)
        self.layoutTravelDirection.setObjectName(_fromUtf8("layoutTravelDirection"))
        self.radioButtonX = QtGui.QRadioButton(self.layoutWidget)
        self.radioButtonX.setChecked(True)
        self.radioButtonX.setObjectName(_fromUtf8("radioButtonX"))
        self.layoutTravelDirection.addWidget(self.radioButtonX)
        self.radioButtonY = QtGui.QRadioButton(self.layoutWidget)
        self.radioButtonY.setChecked(False)
        self.radioButtonY.setObjectName(_fromUtf8("radioButtonY"))
        self.layoutTravelDirection.addWidget(self.radioButtonY)
        self.buttonCalibrate = QtGui.QPushButton(formProfilometer)
        self.buttonCalibrate.setGeometry(QtCore.QRect(90, 350, 101, 41))
        self.buttonCalibrate.setObjectName(_fromUtf8("buttonCalibrate"))
        self.layoutWidget1 = QtGui.QWidget(formProfilometer)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 191, 77))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.layoutProfilometerControls = QtGui.QVBoxLayout(self.layoutWidget1)
        self.layoutProfilometerControls.setMargin(0)
        self.layoutProfilometerControls.setObjectName(_fromUtf8("layoutProfilometerControls"))
        self.labelProfilometerControls = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelProfilometerControls.setFont(font)
        self.labelProfilometerControls.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProfilometerControls.setObjectName(_fromUtf8("labelProfilometerControls"))
        self.layoutProfilometerControls.addWidget(self.labelProfilometerControls)
        self.layoutProfilometerSettings = QtGui.QGridLayout()
        self.layoutProfilometerSettings.setObjectName(_fromUtf8("layoutProfilometerSettings"))
        self.labelTravelDistance = QtGui.QLabel(self.layoutWidget1)
        self.labelTravelDistance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTravelDistance.setObjectName(_fromUtf8("labelTravelDistance"))
        self.layoutProfilometerSettings.addWidget(self.labelTravelDistance, 0, 0, 1, 1)
        self.labelStepSize = QtGui.QLabel(self.layoutWidget1)
        self.labelStepSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelStepSize.setObjectName(_fromUtf8("labelStepSize"))
        self.layoutProfilometerSettings.addWidget(self.labelStepSize, 1, 0, 1, 1)
        self.entryBoxStepSize = QtGui.QLineEdit(self.layoutWidget1)
        self.entryBoxStepSize.setObjectName(_fromUtf8("entryBoxStepSize"))
        self.layoutProfilometerSettings.addWidget(self.entryBoxStepSize, 1, 1, 1, 1)
        self.entryBoxTravelDistance = QtGui.QLineEdit(self.layoutWidget1)
        self.entryBoxTravelDistance.setObjectName(_fromUtf8("entryBoxTravelDistance"))
        self.layoutProfilometerSettings.addWidget(self.entryBoxTravelDistance, 0, 1, 1, 1)
        self.layoutProfilometerControls.addLayout(self.layoutProfilometerSettings)
        self.layoutWidget2 = QtGui.QWidget(formProfilometer)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 280, 151, 66))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.layoutButtonsMovementDirections = QtGui.QGridLayout(self.layoutWidget2)
        self.layoutButtonsMovementDirections.setMargin(0)
        self.layoutButtonsMovementDirections.setObjectName(_fromUtf8("layoutButtonsMovementDirections"))
        self.buttonXPositive = QtGui.QPushButton(self.layoutWidget2)
        self.buttonXPositive.setObjectName(_fromUtf8("buttonXPositive"))
        self.layoutButtonsMovementDirections.addWidget(self.buttonXPositive, 0, 0, 1, 1)
        self.buttonYPositive = QtGui.QPushButton(self.layoutWidget2)
        self.buttonYPositive.setObjectName(_fromUtf8("buttonYPositive"))
        self.layoutButtonsMovementDirections.addWidget(self.buttonYPositive, 0, 1, 1, 1)
        self.buttonZPositive = QtGui.QPushButton(self.layoutWidget2)
        self.buttonZPositive.setObjectName(_fromUtf8("buttonZPositive"))
        self.layoutButtonsMovementDirections.addWidget(self.buttonZPositive, 0, 2, 1, 1)
        self.buttonXNegative = QtGui.QPushButton(self.layoutWidget2)
        self.buttonXNegative.setObjectName(_fromUtf8("buttonXNegative"))
        self.layoutButtonsMovementDirections.addWidget(self.buttonXNegative, 1, 0, 1, 1)
        self.buttonYNegative = QtGui.QPushButton(self.layoutWidget2)
        self.buttonYNegative.setObjectName(_fromUtf8("buttonYNegative"))
        self.layoutButtonsMovementDirections.addWidget(self.buttonYNegative, 1, 1, 1, 1)
        self.buttonZNegative = QtGui.QPushButton(self.layoutWidget2)
        self.buttonZNegative.setObjectName(_fromUtf8("buttonZNegative"))
        self.layoutButtonsMovementDirections.addWidget(self.buttonZNegative, 1, 2, 1, 1)
        self.layoutWidget3 = QtGui.QWidget(formProfilometer)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 250, 191, 23))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.layoutMovemetDistance = QtGui.QHBoxLayout(self.layoutWidget3)
        self.layoutMovemetDistance.setMargin(0)
        self.layoutMovemetDistance.setObjectName(_fromUtf8("layoutMovemetDistance"))
        self.labelMovementDistance = QtGui.QLabel(self.layoutWidget3)
        self.labelMovementDistance.setObjectName(_fromUtf8("labelMovementDistance"))
        self.layoutMovemetDistance.addWidget(self.labelMovementDistance)
        self.entryBoxMovementDistance = QtGui.QLineEdit(self.layoutWidget3)
        self.entryBoxMovementDistance.setObjectName(_fromUtf8("entryBoxMovementDistance"))
        self.layoutMovemetDistance.addWidget(self.entryBoxMovementDistance)
        self.entryBoxHeader = QtGui.QPlainTextEdit(formProfilometer)
        self.entryBoxHeader.setGeometry(QtCore.QRect(210, 350, 431, 121))
        self.entryBoxHeader.setOverwriteMode(False)
        self.entryBoxHeader.setObjectName(_fromUtf8("entryBoxHeader"))
        self.buttonSaveData = QtGui.QPushButton(formProfilometer)
        self.buttonSaveData.setGeometry(QtCore.QRect(10, 440, 91, 32))
        self.buttonSaveData.setObjectName(_fromUtf8("buttonSaveData"))
        self.lineProfilometerControlsDataControls = QtGui.QFrame(formProfilometer)
        self.lineProfilometerControlsDataControls.setGeometry(QtCore.QRect(10, 390, 181, 20))
        self.lineProfilometerControlsDataControls.setFrameShape(QtGui.QFrame.HLine)
        self.lineProfilometerControlsDataControls.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineProfilometerControlsDataControls.setObjectName(_fromUtf8("lineProfilometerControlsDataControls"))
        self.labelDataControls = QtGui.QLabel(formProfilometer)
        self.labelDataControls.setGeometry(QtCore.QRect(20, 410, 171, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelDataControls.setFont(font)
        self.labelDataControls.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDataControls.setObjectName(_fromUtf8("labelDataControls"))
        self.buttonPlotData = QtGui.QPushButton(formProfilometer)
        self.buttonPlotData.setGeometry(QtCore.QRect(110, 440, 91, 32))
        self.buttonPlotData.setObjectName(_fromUtf8("buttonPlotData"))

        self.retranslateUi(formProfilometer)
        QtCore.QMetaObject.connectSlotsByName(formProfilometer)
        formProfilometer.setTabOrder(self.entryBoxTravelDistance, self.entryBoxStepSize)
        formProfilometer.setTabOrder(self.entryBoxStepSize, self.radioButtonX)
        formProfilometer.setTabOrder(self.radioButtonX, self.radioButtonY)
        formProfilometer.setTabOrder(self.radioButtonY, self.buttonStartStop)
        formProfilometer.setTabOrder(self.buttonStartStop, self.entryBoxMovementDistance)
        formProfilometer.setTabOrder(self.entryBoxMovementDistance, self.buttonXPositive)
        formProfilometer.setTabOrder(self.buttonXPositive, self.buttonYPositive)
        formProfilometer.setTabOrder(self.buttonYPositive, self.buttonZPositive)
        formProfilometer.setTabOrder(self.buttonZPositive, self.buttonXNegative)
        formProfilometer.setTabOrder(self.buttonXNegative, self.buttonYNegative)
        formProfilometer.setTabOrder(self.buttonYNegative, self.buttonZNegative)
        formProfilometer.setTabOrder(self.buttonZNegative, self.buttonOrigin)
        formProfilometer.setTabOrder(self.buttonOrigin, self.buttonCalibrate)
        formProfilometer.setTabOrder(self.buttonCalibrate, self.entryBoxHeader)
        formProfilometer.setTabOrder(self.entryBoxHeader, self.graphicsViewPlot)

    def retranslateUi(self, formProfilometer):
        formProfilometer.setWindowTitle(_translate("formProfilometer", "Profilometer", None))
        self.buttonOrigin.setText(_translate("formProfilometer", "Origin", None))
        self.buttonStartStop.setText(_translate("formProfilometer", "Start/Stop", None))
        self.labelSubstrateControls.setText(_translate("formProfilometer", "Substrate Controls", None))
        self.groupBoxTravelDirection.setTitle(_translate("formProfilometer", "Travel Direction:", None))
        self.radioButtonX.setText(_translate("formProfilometer", "X", None))
        self.radioButtonY.setText(_translate("formProfilometer", "Y", None))
        self.buttonCalibrate.setText(_translate("formProfilometer", "Calibrate", None))
        self.labelProfilometerControls.setText(_translate("formProfilometer", "Profilometer Controls", None))
        self.labelTravelDistance.setText(_translate("formProfilometer", "Travel Distance(mm):", None))
        self.labelStepSize.setText(_translate("formProfilometer", "Step Size(um):", None))
        self.entryBoxStepSize.setText(_translate("formProfilometer", "0", None))
        self.entryBoxTravelDistance.setText(_translate("formProfilometer", "0", None))
        self.buttonXPositive.setText(_translate("formProfilometer", "+ X", None))
        self.buttonYPositive.setText(_translate("formProfilometer", "+ Y", None))
        self.buttonZPositive.setText(_translate("formProfilometer", "+ Z", None))
        self.buttonXNegative.setText(_translate("formProfilometer", "- X", None))
        self.buttonYNegative.setText(_translate("formProfilometer", "- Y", None))
        self.buttonZNegative.setText(_translate("formProfilometer", "- Z", None))
        self.labelMovementDistance.setText(_translate("formProfilometer", " Distance(mm):", None))
        self.entryBoxMovementDistance.setText(_translate("formProfilometer", "0", None))
        self.entryBoxHeader.setPlainText(_translate("formProfilometer", "Enter Header Text Here", None))
        self.buttonSaveData.setText(_translate("formProfilometer", "Save Data", None))
        self.labelDataControls.setText(_translate("formProfilometer", "Data Controls", None))
        self.buttonPlotData.setText(_translate("formProfilometer", "Plot Data", None))

