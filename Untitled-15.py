import docx
doc = docx.Document('1.docx')

def getFullText():
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

t = getFullText()
if 'cocoa' in t:
    print('has cocoa text')

i = t.index('iOS')
print(i)