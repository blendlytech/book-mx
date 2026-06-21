import sys

with open('c:/Users/DELL/mx_book/chapters/CHAPTER-3.md', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('"', '')

with open('c:/Users/DELL/mx_book/chapters/CHAPTER-3.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed quotes.")
