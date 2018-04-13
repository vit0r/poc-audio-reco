# -*- coding: utf-8 -*-
"""
POC speech recognition google API
"""

import datetime
import speech_recognition as sr
import argparse

__version__ = '3.0.0'
__author__ = 'Vitor Nascimento de Araujo'


class Main(object):

    def __init__(self):
        self.speech_rec = sr.Recognizer()
        self.args = self.__args_parser()

    @classmethod
    def __args_parser(cls):
        parser = argparse.ArgumentParser(
            prog='POC', description='POC rec sound')
        parser.add_argument('--lang', default='pt_BR',
                            required=False, type=str, help='--lang pt_BR')
        parser.add_argument('--limit', default=10,
                            required=False, type=int, help='--limit 15')
        parser.add_argument('--log', default=False,
                            required=False, type=bool, help='--log True')
        parser.add_argument('--duration', default=1,
                            required=False, type=int, help='--duration 20')
        parser.add_argument('--apikey', default=None,
                            required=False, type=str, help='key-google-speech')
        return parser.parse_args()

    def run(self):
        while True:
            text = ''
            try:
                with sr.Microphone() as source:
                    self.speech_rec.adjust_for_ambient_noise(source, duration=self.args.duration)
                    audio = self.speech_rec.listen(source, phrase_time_limit=self.args.limit)
                text = self.speech_rec.recognize_google(audio, key=self.args.apikey, language=self.args.lang,
                                                        show_all=False)
            except sr.UnknownValueError as err:
                print('NotUnderstand {}'.format(err))
            except sr.RequestError as err:
                print('ReqError {}'.format(err))
            except ValueError as err:
                print('Error {}'.format(err))
            finally:
                if text:
                    date_receiver = datetime.datetime.now().strftime(u'%d/%m/%y às %H:%M')
                    print('{}\nReceived in {}'.format(text, date_receiver))
