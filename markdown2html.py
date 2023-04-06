#!/usr/bin/python3
"""Convert Markdown file to HTML"""

import argparse
import os
import sys
import re


def markdown_to_html(input_file, output_file):
    """Converts a Markdown file to HTML"""
    try:
        with open(
            input_file, "r"
                  ) as md_file, open(output_file, "w") as html_file:
            md_text = md_file.read()
            # convert headers
            md_text = re.sub(r'###### (.+)', r'<h6>\1</h6>', md_text)
            md_text = re.sub(r'##### (.+)', r'<h5>\1</h5>', md_text)
            md_text = re.sub(r'#### (.+)', r'<h4>\1</h4>', md_text)
            md_text = re.sub(r'### (.+)', r'<h3>\1</h3>', md_text)
            md_text = re.sub(r'## (.+)', r'<h2>\1</h2>', md_text)
            md_text = re.sub(r'# (.+)', r'<h1>\1</h1>', md_text)
            # convert bold and italic
            md_text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', md_text)
            md_text = re.sub(r'__(.+?)__', r'<strong>\1</strong>', md_text)
            md_text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', md_text)
            md_text = re.sub(r'_(.+?)_', r'<em>\1</em>', md_text)
            # convert lists
            md_text = re.sub(r'^\* (.+)', r'<li>\1</li>', md_text, flags=re.M)
            md_text = re.sub(
                r'^(\* .+\n)+', r'<ul>\n\g<0></ul>', md_text, flags=re.M
                            )
            md_text = re.sub(
                r'^[0-9]+\. (.+)', r'<li>\1</li>', md_text, flags=re.M
                            )
            md_text = re.sub(
                r'^([0-9]+\. .+\n)+', r'<ol>\n\g<0></ol>', md_text, flags=re.M
                            )
            # convert links
            md_text = re.sub(
                r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', md_text
                            )
            # convert paragraphs
            md_text = re.sub(
                r'^([^\n].+\n)+', r'<p>\g<0></p>', md_text, flags=re.M
                            )
            # write to file
            html_file.write(md_text)
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Markdown file to HTML"
                                    )
    parser.add_argument("input_file", help="The input Markdown file")
    parser.add_argument("output_file", help="The output HTML file")
    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        print(f"Error: {args.input_file} does not exist")
        sys.exit(1)

    markdown_to_html(args.input_file, args.output_file)

    sys.exit(0)
