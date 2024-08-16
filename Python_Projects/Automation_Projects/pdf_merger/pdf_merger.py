import PyPDF2
import sys
import os


for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger = PyPDF2.PdfMerger()
        merger.append(file)
    merger.write("combiedPDF.pdf")



# Add two or more pdf files to this directory and it will create a merged one with combinedPDF.pdf name