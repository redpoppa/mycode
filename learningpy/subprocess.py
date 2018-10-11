#!/usr/bin/env python3
import subprocess

from subprocess import call

call(["ip", "link", "show", "up"])

print("Let's check the state of your network interfaces")

collectedinput = input("What is the name of the interface you would like more info on? Ex. ens3: ")

call(["ip", "addr", "show", "dev", collectedinput])
