#!/usr/bin/python3
"""This script takes 2 files as argumrnts
    first argument: markdown file
    second argument: html file"""

from sys import argv, stderr
import os


if (len(argv) < 2):
    print ('Usage: ./markdown2html.py README.md README.html', file=stderr)
    exit(1)
elif (not os.path.exists(argv[1])):
    print ('Missing {}'.format(argv[1]), file=stderr)
    exit(1)
else:
    exit(0)
