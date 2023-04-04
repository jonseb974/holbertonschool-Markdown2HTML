#!/usr/bin/env python3
""" task_0 Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
"""

import sys
import os
import markdown


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: {} <markdown_file> <output_file>".format(sys.argv[0]),
    file=sys.stderr)
        sys.exit(1)

markdown_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(markdown_file):
    print("Missing {}".format(markdown_file), file=sys.stderr)
    sys.exit(1)

with open(markdown_file, 'r') as md_file:
    markdown_text = md_file.read()

html_text = markdown.markdown(markdown_text)

with open(output_file, 'w') as out_file:
    out_file.write(html_text)

sys.exit(0)
