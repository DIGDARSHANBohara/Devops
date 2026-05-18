import docx
import sys

def read_docx(file_path):
    doc = docx.Document(file_path)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

if __name__ == '__main__':
    content = read_docx(sys.argv[1])
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(content)
