import sys
def getText():
    with open('asciiText', 'r') as f:
        lines = f.readlines()
    return lines

def modifyTags(bigText):
    newLines = []
    for i in range(len(bigText)):
        newLines.append(bigText[i].replace('\n',''))
    return newLines

def makeFile(lines):
    with open('icecream.html', 'w') as myFile:
        for i in range(len(lines)):
            sys.stdout.write(lines[i])
            myFile.write(("<marquee height=25 vspace = 2><pre>" + lines[i] + '</pre></marquee>\n'))
    myFile.close()

makeFile(modifyTags(getText()))