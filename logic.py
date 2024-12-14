from gui import *
from PyQt6.QtWidgets import *

from PyQt6 import QtCore
import csv

class Logic(QMainWindow, Ui_TvRemote):
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MAX_CHANNEL = 3
    MIN_CHANNEL = 0

    def __init__(self)->None:
        """
        Method to define instance variables.
        Method checks for user input upon pressing buttons.
        """

        super().__init__()
        self.setupUi(self)

        self.__status = False
        self.__muted = False
        self.__volume = Logic.MIN_VOLUME
        self.__channel = 0
        self.__hold = 0

        self.powerButton.clicked.connect(lambda : self.power())
        self.volumeAddButton_2.clicked.connect(lambda : self.vol_up())
        self.volumeMinButton_3.clicked.connect(lambda : self.vol_down())
        self.channelAddButton_4.clicked.connect(lambda : self.chan_up())
        self.channelMinButton_5.clicked.connect(lambda : self.chan_down())
        self.muteButton_6.clicked.connect(lambda : self.mute())

    def power(self)->None:
        """
        Method to toggle TV Power on/off.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True
        self.state_check()

    def vol_up(self)->None:
        """
        Method to increase the tv volume.
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__hold
            self.__muted = False

            if self.__volume < Logic.MAX_VOLUME:
                self.__volume += 1
        self.state_check()

    def vol_down(self)->None:
        """
        Method to lower the tv volume.
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__hold
            self.__muted = False
            if self.__volume > Logic.MIN_VOLUME:
                self.__volume -= 1
        self.state_check()

    def chan_up(self)->None:
        """
        Method to increase the tv channel.
        """

        if self.__status:
            if self.__channel < Logic.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Logic.MIN_CHANNEL
        self.state_check()

    def chan_down(self)->None:
        """
        Method to lower the tv channel.
        """
        if self.__status:
            if self.__channel > Logic.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Logic.MAX_CHANNEL
        self.state_check()
    def mute(self)->None:
        """
        Method to toggle mute on/off.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__hold
            else:
                self.__muted = True
                self.__hold = self.__volume
                self.__volume = 0
        self.state_check()


    def state_check(self)->None:
        """
        Sets right hand indicators to their respected values
        """

        self.channelndicator.setPlainText(str(self.__channel))

        if self.__muted:
            mute_str = "on"
        else:
            mute_str = "off"

        self.muteIndicator.setPlainText(mute_str)

        if self.__status:
            power_str = "on"
        else:
            power_str = "off"

        self.plainTextEdit_5.setPlainText(power_str)

        self.volumeIndicator.setPlainText(str(self.__volume))





