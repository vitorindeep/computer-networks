#!/usr/bin/python

#Compilar: python compile_refs.py lncs-paper

import subprocess, sys

commands = [
    ['pdflatex', sys.argv[1] + '.tex'],
    ['bibtex', sys.argv[1] + '.aux'],
    ['pdflatex', sys.argv[1] + '.tex'],
    ['pdflatex', sys.argv[1] + '.tex']
]

for c in commands:
    subprocess.call(c)
