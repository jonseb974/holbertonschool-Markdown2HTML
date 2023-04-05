#!/usr/bin/python3
""" task_0 Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file Second argument is
    the output file name :README.md README.html
    Improve markdown2html, parsing Headings Markdown syntax for generating HTML
"""

import sys  # import the sys module
import os  # import os module


def convert_markdown_to_html(input_file, output_file):
    # open read input file, read all lines
    with open(input_file, "r") as f:
        lines = f.readlines()

    # open write output file
    with open(output_file, "w") as f:
        # Foe each line of the file
        for line in lines:
            if line.startswith("#"):  # check if line starts with 1 # or more
                heading_level = 1  # item of level 1
                while line.startswith("#", heading_level):
                    heading_level += 1
                heading_text = line[heading_level:].strip()
                f.write(
                    f'<h{heading_level}>{heading_text}</h{heading_level}>\n'
                    )
            elif line.startswith("-"):  # check if line starts with '-'
                f.write("<ul>\n")  # starts a new unordered list
                while line.startswith("-"):
                    line = line[1:].strip()  # remove "-" an white spaces
                    f.write(f"<li>{line}</li>\n")  # add line as list
                    try:
                        line = lines.pop(0)  # get the next line
                    except IndexError:
                        break  # end of file
                f.write("</ul>\n")  # end of the unordered list
            else:  # If line do not start with #, write it in output
                f.write(line)


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
