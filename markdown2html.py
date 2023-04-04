#!/usr/bin/env python3
""" task_0 Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
"""
import sys
import os


if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <inputfile.md> <outputfile.html>",
        file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# TODO: Convert the Markdown file to HTML and write to the output file

sys.exit(0)
