#!/bin/sh
# github.com/n0nexist/AndroBrick
# WARNING: DON'T USE THIS SCRIPT WITH YOUR MAIN PHONE
# THIS WILL BREAK YOUR PHONE

import os

if input("ARE YOU SURE YOU WANT TO CONTINUE?\nTHIS SCRIPT WILL BREAK YOUR PHONE. THERE IS NO GOING BACK.\nTHERE IS A VERY HIGH CHANCE THAT HARD RESETTING YOUR PHONE WON'T HELP.\nTYPE 'YES I WANT' TO CONFIRM\n> ") == "YES I WANT":
    print("BRICKING THE PHONE, PLEASE WAIT.\n(YOU ARE STILL IN TIME TO PREVENT TOTAL DESTRUCTION FOR A FEW SECONDS)")
else:
    exit(1)


packages = os.popen("adb shell pm list packages").read().split("\n")
for package in packages:
    package = package.strip().replace("package:","")
    if package != "":
        print(f"Uninstalling '{package}'... ",end="")
        print(os.popen(f"adb shell pm uninstall --user 0 {package}").read())
