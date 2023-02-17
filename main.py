import markdown
# Import Module
import os
from pathlib import Path

# Markdown file folder path
# Change this value as required to the right location
path = "C:\\Users\\Elvis\\Desktop\\Elvis\\pesapal\\Static-Generator\\markdowns"


def read_markdown_file(file_path):
    """
    reads markdown
    :returns html from markdown file
    """
    with open(file_path, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)
        return html


def generate_html(html, filename):
    """generates html document"""
    # with open(f'{filename}', 'w') as f:
    directory = Path(f"generated")
    directory.mkdir(parents=True, exist_ok=True)
    with open(f'{directory}\{filename}', 'w') as f:
        f.write(html)


def run():
    """iterate through all file"""
    for file in os.listdir():
        # Check if file is in .md format or not
        if file.endswith(".md"):
            file_path = f"{path}\{file}"
            # call read md file function
            html_data = read_markdown_file(file_path)
            # generate the html files and saves with the suitable name
            generate_html(html_data, f"{file.rstrip('.md')}.html")

if __name__ == '__main__':
    run()
