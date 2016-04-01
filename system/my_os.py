#!/usr/bin/python

import os
from subprocess import call
from os.path import expanduser


def call_with_message(command, message):
    print message

    return_code = call(command)

    if return_code == 0:
        print message + " done\n"
    else:
        print message + " failed\n"

    return return_code == 0


class Cd:
    """Context manager for changing the current working directory"""

    def __init__(self, newPath):
        self.newPath = expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)
        print "Entering {} ...\n".format(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)
        print "Entering {} ...\n".format(self.savedPath)
