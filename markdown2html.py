#!/usr/bin/python3
''' Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
'''
import sys
import os


def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in lines:
            if line.startswith('# '):
                heading_level = 1
                while line.startswith('#', heading_level):
                    heading_level += 1
                heading_text = line[heading_level:].strip()
                f.write(
                    f'<h{heading_level}>{heading_text}</h{heading_level}>\n'
                )
            elif line.startswith('* '):
                f.write('<ul>\n')
                f.write(f'<li>{line[2:].strip()}</li>\n')
            elif line.startswith('*'):
                f.write(f'<li>{line[1:].strip()}</li>\n')
            elif line.startswith('\n'):
                f.write('</ul>\n')
            else:
                f.write(line)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(
            "Usage: ./markdown2html.py README.md README.html", file=sys.stderr
        )
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(input_file, output_file)

    sys.exit(0)
