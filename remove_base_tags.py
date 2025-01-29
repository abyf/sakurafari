import sys
import re

def read_file(file_path):
    """Reads the content of a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()

def extract_tags(content):
    """Extracts all HTML tags from content as a set of cleaned tag strings."""
    tag_pattern = re.compile(r"<[^>]+>")  # Match anything that looks like an HTML tag
    return set(tag_pattern.findall("".join(content)))  # Extract unique tags

def remove_matched_tags(target_lines, base_tags):
    """Removes tags from target_lines if they match any tag in base_tags."""
    updated_lines = []
   
    for line in target_lines:
        modified_line = line
        for tag in base_tags:
            modified_line = modified_line.replace(tag, "")  # Remove tag but preserve indentation
        updated_lines.append(modified_line)
   
    return updated_lines

def write_file(file_path, content):
    """Writes content back to the file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_base_tags.py base.html target.html")
        sys.exit(1)

    base_file = sys.argv[1]
    target_file = sys.argv[2]

    base_content = read_file(base_file)
    target_content = read_file(target_file)

    base_tags = extract_tags(base_content)
    updated_target = remove_matched_tags(target_content, base_tags)

    write_file(target_file, updated_target)

    print(f"Tags from {base_file} have been removed from {target_file} while preserving indentation.")