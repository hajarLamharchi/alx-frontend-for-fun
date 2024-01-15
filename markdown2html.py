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
    headers = []
    with open(argv[1], 'r') as md_file:
        lines = md_file.readlines()
    for line in lines:
        h = 0
        for c in line:
            if c == '#':
                h += 1
        headers.append(h)
    L = []
    l1 = []
    l2 = []
    for i in range(0, len(lines)):
        if lines[i][0] == '#':
            if i == len(lines) - 1:
                L.append('<h{}>{}<h{}>'.format(headers[i],
                                               lines[i][headers[i]+1:],
                                               headers[i]))
            else:
                L.append('<h{}>{}<h{}>'.format(headers[i],
                                               lines[i][headers[i]+1:-1],
                                               headers[i]))
        elif lines[i][0] == '-':
            if i == len(lines) - 1:
                l1.append('<li>{}</li>'.format(lines[i][2:]))
            else:
                l1.append('<li>{}</li>'.format(lines[i][2:-1]))
        elif lines[i][0] == '*':
            if i == len(lines) - 1:
                l2.append('<li>{}</li>'.format(lines[i][2:]))
            else:
                l2.append('<li>{}</li>'.format(lines[i][2:-1]))
    if l1 != []:
        L.append('<ul>')
        for i in l1:
            L.append(i)
        L.append('</ul>')

    elif l2 != []:
        L.append('<ol>')
        for i in l2:
            L.append(i)
        L.append('</ol>')
    print(L)
    with open(argv[2], 'a') as html_file:
        html_file.writelines('\n'.join(L))
    exit(0)
