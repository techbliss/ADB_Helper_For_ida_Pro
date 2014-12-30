__author__ = 'zadow'

import subprocess
import idaapi
import idc
from idc import *
from idaapi import *
import os
import sys


class gonzola(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = "This is a comment"

    help = "ADB"
    wanted_name = "ADB Helper"
    wanted_hotkey = "Alt-F7"

    def init(self):
        idaapi.msg("ADB Plugin is found. \n")
        return idaapi.PLUGIN_OK

    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")

    def AddMenuElements(self):
        idaapi.add_menu_item("Debugger/", "1: adb Restart as Root", "", 0, self.night, ())
        idaapi.add_menu_item("Debugger/", "2: push android server to rooted phone", "", 0, self.sun, ())
        idaapi.add_menu_item("Debugger/", "3: chmod android server 755 ", "", 0, self.rain, ())
        idaapi.add_menu_item("Debugger/", "4: connect to android server ", "", 0, self.shinny, ())
        idaapi.add_menu_item("Debugger/", "5: adb Forward ports for debugging", "", 0, self.day, ())
        idaapi.add_menu_item("Debugger/", "6: adb Logcat", "", 0, self.snows, ())
        idaapi.add_menu_item("Debugger/", "7: adb Logcat to File", "", 0, self.thunder, ())



    def run(self, arg=0):
        idaapi.msg("")

        self.AddMenuElements()


    def night(self):
        subprocess.Popen('adb.exe root')
        print 'Restart abd connection as root'

    def sun(self):
        subprocess.Popen('adb.exe push android_server /data/local/android_server')
        print 'Pushed'

    def rain(self):
        subprocess.Popen('adb.exe shell chmod 755 /data/local/android_server')
        print 'Permissions changed'


    def shinny(self):
        subprocess.Popen('adb.exe shell ./data/local/android_server')
        print 'Should be connected'


    def day(self):
        subprocess.Popen('adb forward tcp:23946 tcp:23946')
        print 'You can Attach or start debugging'

    def snows(self):
        subprocess.Popen('adb logcat')
        print 'Logging'

    def thunder(self):
        file = get_root_filename()
        subprocess.Popen('adb logcat > logcat.txt')

def PLUGIN_ENTRY():
    return gonzola()
