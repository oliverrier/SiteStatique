from markdown2 import Markdown
import re
import os
import argparse

links = [(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'), r'\1')]

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-directory", type = str, help = "Directory where your Markdown files are")
parser.add_argument("-o", "--output-directory", type = str, help = "Directory in which you wish to place your HTML files")
arguments = parser.parse_args()
markdownDirectory = arguments.input_directory
htmlDirectory = arguments.output_directory

def convertMDToHTML():
    markdownFilesList = os.listdir(markdownDirectory)
    for markdownFile in markdownFilesList:
        with open(f'{markdownDirectory}/{markdownFile}', 'r') as fileToConvert:
            if markdownFile == markdownFilesList[0]:
                baseFileName = 'index'
            else:
                baseFileName = markdownFile[:-3]
            textToConvert = fileToConvert.read()
            textToConvert = textToConvert.replace('  ##', '##')
            HTMLFile = open(htmlDirectory + '/' + baseFileName + '.html', "w+")
            link = Markdown(extras=["link-patterns","cuddled-lists", "target-blank-links"], link_patterns=links)
            convertedFile = link.convert(textToConvert)
            HTMLFile.write(convertedFile)
            HTMLFile.close()

convertMDToHTML()