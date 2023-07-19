#!/usr/bin/python

""" 
----------------------------------------------------
"""
import os, sys
import stat

# For the directory of the script being run:

running_directory = os.path.dirname(os.path.abspath(__file__))

#If you mean the current working directory:

working_directory = os.path.abspath(os.getcwd())

# new folder
place_to_save = working_directory + "\\MANOLO"


from subprocess import call
call(['mklink', 'LINK', 'TARGET'], shell=True)