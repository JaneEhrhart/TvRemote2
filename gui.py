# Form implementation generated from reading ui file 'TvRemote004.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TvRemote(object):
    def setupUi(self, TvRemote):
        TvRemote.setObjectName("TvRemote")
        TvRemote.resize(590, 695)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TvRemote.sizePolicy().hasHeightForWidth())
        TvRemote.setSizePolicy(sizePolicy)
        TvRemote.setMinimumSize(QtCore.QSize(590, 695))
        TvRemote.setMaximumSize(QtCore.QSize(590, 695))
        self.centralwidget = QtWidgets.QWidget(parent=TvRemote)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(70, 80, 151, 411))
        self.line.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(10)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(340, 80, 151, 401))
        self.line_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(10)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(150, 450, 271, 71))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_3.setLineWidth(10)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(140, 50, 271, 71))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_4.setLineWidth(10)
        self.line_4.setMidLineWidth(1)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setObjectName("line_4")
        self.powerButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.powerButton.setGeometry(QtCore.QRect(310, 100, 93, 28))
        self.powerButton.setObjectName("powerButton")
        self.volumeAddButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.volumeAddButton_2.setGeometry(QtCore.QRect(160, 200, 93, 28))
        self.volumeAddButton_2.setObjectName("volumeAddButton_2")
        self.volumeMinButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.volumeMinButton_3.setGeometry(QtCore.QRect(160, 240, 93, 28))
        self.volumeMinButton_3.setObjectName("volumeMinButton_3")
        self.channelAddButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channelAddButton_4.setGeometry(QtCore.QRect(290, 200, 93, 28))
        self.channelAddButton_4.setObjectName("channelAddButton_4")
        self.channelMinButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channelMinButton_5.setGeometry(QtCore.QRect(290, 240, 93, 28))
        self.channelMinButton_5.setObjectName("channelMinButton_5")
        self.muteButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.muteButton_6.setGeometry(QtCore.QRect(170, 280, 61, 28))
        self.muteButton_6.setObjectName("muteButton_6")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(430, 80, 151, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(430, 220, 71, 31))
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(430, 260, 91, 31))
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(430, 180, 81, 31))
        self.plainTextEdit_4.setReadOnly(True)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(490, 180, 41, 31))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.channelndicator = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.channelndicator.setGeometry(QtCore.QRect(500, 220, 41, 31))
        self.channelndicator.setObjectName("channelndicator")
        self.volumeIndicator = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.volumeIndicator.setGeometry(QtCore.QRect(500, 260, 41, 31))
        self.volumeIndicator.setObjectName("volumeIndicator")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(430, 300, 91, 31))
        self.plainTextEdit_6.setReadOnly(True)
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.muteIndicator = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.muteIndicator.setGeometry(QtCore.QRect(480, 300, 41, 31))
        self.muteIndicator.setObjectName("muteIndicator")
        TvRemote.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=TvRemote)
        self.statusbar.setObjectName("statusbar")
        TvRemote.setStatusBar(self.statusbar)

        self.retranslateUi(TvRemote)
        QtCore.QMetaObject.connectSlotsByName(TvRemote)

    def retranslateUi(self, TvRemote):
        _translate = QtCore.QCoreApplication.translate
        TvRemote.setWindowTitle(_translate("TvRemote", "TvRemote"))
        self.powerButton.setText(_translate("TvRemote", "Power"))
        self.volumeAddButton_2.setText(_translate("TvRemote", "Volume +"))
        self.volumeMinButton_3.setText(_translate("TvRemote", "Volume -"))
        self.channelAddButton_4.setText(_translate("TvRemote", "Channel +"))
        self.channelMinButton_5.setText(_translate("TvRemote", "Channel -"))
        self.muteButton_6.setText(_translate("TvRemote", "Mute"))
        self.plainTextEdit.setPlainText(_translate("TvRemote", "Max Channel = 3\n"
"Min Channel = 0\n"
"\n"
"Max Volume = 2\n"
"Min Volume = 0\n"
"\n"
""))
        self.plainTextEdit_2.setPlainText(_translate("TvRemote", "Channel ="))
        self.plainTextEdit_3.setPlainText(_translate("TvRemote", "Volume ="))
        self.plainTextEdit_4.setPlainText(_translate("TvRemote", "Power ="))
        self.plainTextEdit_5.setPlainText(_translate("TvRemote", "off"))
        self.channelndicator.setPlainText(_translate("TvRemote", "0"))
        self.volumeIndicator.setPlainText(_translate("TvRemote", "0"))
        self.plainTextEdit_6.setPlainText(_translate("TvRemote", "Mute ="))
        self.muteIndicator.setPlainText(_translate("TvRemote", "off"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TvRemote = QtWidgets.QMainWindow()
    ui = Ui_TvRemote()
    ui.setupUi(TvRemote)
    TvRemote.show()
    sys.exit(app.exec())
