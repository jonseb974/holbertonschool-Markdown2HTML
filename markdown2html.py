#!/usr/bin/python3
''' Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
'''


def convert_markdown_to_html(input_file, output_file):
    # open read input file, read all lines
    with open(input_file, "r") as f:
        lines = f.readlines()

    # open write output file
    with open(output_file, "w") as f:
        # For each line of the file
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
                f.write("<ul>\n")  # start a new unordered list
                while line.startswith("-"):
                    line = line[1:].strip()  # remove '-' and whitespaces
                    f.write(f"<li>{line}</li>\n")  # add line as a list item
                    try:
                        line = lines.pop(0)  # get the next line
                    except IndexError:
                        break  # end of file
                f.write("</ul>\n")  # end the unordered list
            else:  # If line do not start with # or -, write it in output
                f.write(line)
