import os
import sys
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

def read_html(file_path):
    """Read and parse an HTML file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_html(file_path, content):
    """Write HTML content to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def find_common_html(files):
    """Identify the common HTML patterns across multiple files."""
    if not files:
        return None, None

    # Read all files
    file_contents = [read_html(file) for file in files]

    # Find the common text using SequenceMatcher
    common_text = file_contents[0]
    for content in file_contents[1:]:
        matcher = SequenceMatcher(None, common_text, content)
        match = matcher.find_longest_match(0, len(common_text), 0, len(content))
        if match.size > 0:
            common_text = common_text[match.a:match.a + match.size]
        else:
            common_text = ""
            break

    # Parse common structure with BeautifulSoup for proper formatting
    common_soup = BeautifulSoup(common_text, 'html.parser') if common_text else None
    return common_soup, common_text

def cut_common_parts(files, common_text):
    """Cut common parts from files without modifying their indentation."""
    for file in files:
        original_content = read_html(file)
        # Remove the common text
        updated_content = original_content.replace(common_text, "")
        write_html(file, updated_content)

def main():
    """Main function to extract and cut common HTML parts."""
    if len(sys.argv) < 3:
        print("Usage: python find-common-html.py output_file.html input1.html input2.html ...")
        return

    output_file = sys.argv[1]
    html_files = sys.argv[2:]

    # Validate input files
    for file in html_files:
        if not os.path.exists(file) or not file.endswith(".html"):
            print(f"Error: '{file}' is not a valid HTML file.")
            return

    # Find common parts
    common_soup, common_text = find_common_html(html_files)

    if not common_soup or not common_text:
        print("No common parts found.")
        return

    # Save common parts to the output file
    write_html(output_file, common_soup.prettify(formatter="html"))
    print(f"Common parts saved to {output_file}.")

    # Remove common parts from the original files
    cut_common_parts(html_files, common_text)
    print("Common parts removed from the original files.")

if __name__ == "__main__":
    main()