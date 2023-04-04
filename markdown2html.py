#!/usr/bin/python3
""" task_0 Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
    README.md README.html
"""

import sys  # import the sys module
import os  # import os module


def convert_markdown_to_html(input_file, output_file):
    pass


# Check if the script is executed directly (not imported)
if __name__ == "main":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py READMe.md README.html",
        file=sys.stderr)
        sys.exit(1)
    input_file = sys.argv[1]  # Get the filename
    output_file = sys.argv[2]  # Output name

    if not os.path.isfile(input_file):  # Check if file exists.
        print(f"Missing {input_file}", file=sys.stderr)  # error message
        sys.exit(1)  # exit with non-zero status code

    convert_markdown_to_html(input_file, output_file)  # Convert to html
    sys.exit(0)  # exit with zero-status code if success
