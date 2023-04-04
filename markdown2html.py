#!/usr/bin/env python3
""" task_0 Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
    <inputfile.md> <outputfile.html>
"""
import sys
import os

if __name__ == 'main':
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

# input_file = sys.argv[1]
# output_file = sys.argv[2]

if not os.path.isfile(sys.argv[1]):
    print("Missing {}".format(sys.argv[1]), file=sys.stderr)
    exit(1)

# TODO: Convert the Markdown file to HTML and write to the output file

exit(0)
