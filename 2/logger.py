#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import StringIO
import sys

class Logger(object):

    def __init__(self, device, format="%s\n"):
        self.__device = device
        self.__format = format

    def log(self, info):
        self.__device.write(self.__format % info)

    def on(self):
        self.__device = sys.stdout

    def off(self):
        self.__device = StringIO.StringIO()


        