#!/usr/bin/python3
""" task_0 Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file Second argument is
    the output file name :README.md README.html
    Improve markdown2html, parsing Headings Markdown syntax for generating HTML
"""

import sys  # import the sys module
import os  # import os module
import markdown


def convert_markdown_to_html(input_file, output_file):
    with open(input_file, "r") as f:
        md_text = f.read()
    html_text = markdown.markdown(md_text)
    with open(output_file, "w") as f:
        f.write(html_text)


if __name__ == "__main__":
    # Check if the number of command-line arguments is correct
    if len(sys.argv) < 3:
        # Print an error message to STDERR and exit with a non-zero status code
        print(
            "Usage: ./markdown2html.py README.md README.html",
            file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        # Print an error message to STDERR and exit with a non-zero status code
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to HTML and write to output_file
    convert_markdown_to_html(input_file, output_file)

    # Exit with a zero status code to indicate success
    sys.exit(0)
