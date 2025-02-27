import re
import sys

print("Escolha o ficheiro MarkDown para converter")
fileName = sys.stdin.readline()

ficheiro = open(fileName.strip(), "r", encoding="utf8")
html = open(fileName.strip().replace(".md", ".html"), "w", encoding="utf8")

file_text = ficheiro.read()

file_text = re.sub(r"(^# ((.*)))", r"<h1>\2</h1>", file_text, flags=re.M) ##header 1
file_text = re.sub(r"(^## ((.*)))", r"<h2>\2</h2>", file_text, flags=re.M) ##header 2
file_text = re.sub(r"(^### (.*))", r"<h3>\2</h3>", file_text, flags=re.M) ##header 3
file_text = re.sub(r"\*\*(.*)\*\*", r"<b>\1</b>", file_text) ##bold
file_text = re.sub(r"\*([^*]*)\*", r"<i>\1</i>", file_text) ##itálico
file_text = re.sub(r"!\[([^\]]*)\]\(([^\)]*)\)", r'<img src="\2" alt="\1"/>', file_text) ##imagens
file_text = re.sub(r"\[([^\]]*)\]\(([^\)]*)\)", r'<a href="\2">\1</a>', file_text) ##links
file_text = re.sub(r"^(\d+. (.*)(\n\s*(\d+.) .*)*)", r'<ol>\n\1\n</ol>', file_text, flags=re.M) ##list
file_text = re.sub(r"[\d]+\. ([^\n]+)", r'<li>\1</li>', file_text) ##list items

ficheiro.close()
html.write(file_text)