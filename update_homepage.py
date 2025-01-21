import sys
import re

def update_stylesheets_links(filename):
    with open(filename,'r') as file:
        content = file.read()

    pattern =  r'<link.*?href="([^"]+)".*?>'
    new_content = re.sub(pattern,r'<link rel="stylesheet" href="{% static \'web_sakurafari/\1\' %}">',content)

    with open(filename,'w') as file:
        file.write(new_content.replace("\\'","'"))

def update_javascripts_links(filename):
    with open(filename,'r') as file:
        content = file.read()

    pattern = r'<script src="(.*)"></script>'
    new_content = re.sub(pattern,r'<script src="{% static \'web_sakurafari/\1\' %}"></script>',content)

    with open(filename,'w') as file:
        file.write(new_content.replace("\\'","'"))

def update_images_links(filename):
    with open(filename,'r') as file:
        content = file.read()

    pattern = r'<img\s+src="([^"]+)"(.*?)>'
    new_content = re.sub(pattern,r'<img src="{% static \'web_sakurafari/\1\' %}" \2>',content)

    with open(filename,'w') as file:
        file.write(new_content.replace("\\'","'"))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python  scripty.py <filename>')
        sys.exit(1)
    filename = sys.argv[1]
    update_stylesheets_links(filename)
    update_javascripts_links(filename)
    update_images_links(filename)