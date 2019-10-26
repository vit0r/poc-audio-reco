# -*- coding: utf-8 -*-
"""
POC speech recognition google API
"""

import sys
import datetime
import argparse
import audioop
import pyaudio

import numpy as np
import speech_recognition as speech_rec

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread

from main_ui import Ui_MainWindow

__version__ = '2.0.1'
__author__ = 'Vitor Nascimento de Araujo'


class Main(Ui_MainWindow, QThread):
    """Main calss App"""

    _CHANNELS = 1

    def __init__(self, dialog):
        """Init CLASS"""

        # ui args
        super(Main, self).__init__()
        self.setupUi(dialog)

        # pyaudio init
        self.py_audio = pyaudio.PyAudio()

        # data process args
        self.data = np.array([])
        self.rms = 0

        # init speech api
        self.speech_rec = speech_rec.Recognizer()

        # parse args
        self.args = self.args_parser()

        # get values from default input device
        self.input_device = self.py_audio.get_default_input_device_info()

    @classmethod
    def args_parser(cls):
        """Parse args from terminal"""
        parser = argparse.ArgumentParser(
            prog='POC', description='POC rec sound')
        parser.add_argument('--lang', default='pt_BR',
                            required=False, type=str, help='--lang pt_BR')
        parser.add_argument('--silence', default=30,
                            required=False, type=int, help='--silence 30')
        parser.add_argument('--log', default=False,
                            required=True, type=bool, help='--log True')
        parser.add_argument('--apikey', default=None,
                            required=False, type=str, help='key-google-speech')
        return parser.parse_args()

    def callback(self, in_data, frame_count, time_info, flag):
        """Receive data from audio device"""

        self.rms = audioop.rms(in_data, 1)
        self.data = np.append(self.data, np.fromstring(in_data, dtype=np.float))
        if self.args.log:
            info = u'{}\n{}\n{}\n{}\n\n'.format(self.rms, frame_count, time_info, flag)
            self.labelLogger.setText(info)
        return in_data, pyaudio.paContinue

    def build_audio_data(self):
        """to string byte audio from numpy array and create data audio"""
        frame_data = self.data.tostring()
        audio_data = speech_rec.AudioData(
            frame_data=frame_data, sample_rate=int(self.input_device['defaultSampleRate']),
            sample_width=pyaudio.paInt24)
        return audio_data

    def send_to_speech(self):
        """Send audio data from speech api"""
        text = ''
        audio_data = self.build_audio_data()
        try:
            text = self.speech_rec.recognize_google(
                audio_data, key=self.args.apikey, language=self.args.lang, show_all=False)
        except speech_rec.UnknownValueError as err:
            self.labelLogger.setText('NotUnderstand {}'.format(err))
        except speech_rec.RequestError as err:
            self.labelLogger.setText('ReqError {}'.format(err))
        except ValueError as err:
            self.labelLogger.setText('Error {}'.format(err))
        finally:
            if text:
                self.data = np.array([])
                self.plainTextEdit.clearFocus()
                date_receiver = datetime.datetime.now().strftime(u'%d/%m/%y às %H:%M')
                self.plainTextEdit.appendPlainText(
                    u'{}\nReceived in {}'.format(text, date_receiver))
                self.plainTextEdit.setFocus()

    def run(self):
        """Main thread => run all app"""
        stream = self.py_audio.open(format=pyaudio.paInt32,
                                    channels=self._CHANNELS,
                                    rate=int(self.input_device['defaultSampleRate']),
                                    output=False,
                                    input=True,
                                    stream_callback=self.callback)
        stream.start_stream()
        while stream.is_active():
            if self.rms < self.args.silence:
                self.send_to_speech()



if __name__ == '__main__':
    APP = QtWidgets.QApplication(sys.argv)
    WINDOW = QtWidgets.QMainWindow()
    PROGRAM = Main(WINDOW)
    PROGRAM.start()
    WINDOW.show()
    sys.exit(APP.exec_())
