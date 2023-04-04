#!/usr/bin/python3
"""
task 0 start a script
"""


import sys  # import the sys module
import os  # import os module


def convert_markdown_to_html(self, markdown_file, html_file):
    """
    Convert markdown to html
    """
    self.markdown_file = markdown_file
    self.html_file = html_file
    pass


# Check if the script is executed directly(not imported)
if __name__ == "main":

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", \
              file=sys.stderr)
        sys.exit(1)
    markdown_file = sys.argv[1]  # Get the filename
    html_file = sys.argv[2]  # Output name

if not os.path.isfile(markdown_file):  # Check if file exists.
    print(f"Missing {markdown_file}", file=sys.stderr)  # error message
    sys.exit(1)  # exit with non-zero status code
convert_markdown_to_html(markdown_file, html_file)
sys.exit(0)
# exit with zero-status code if success
