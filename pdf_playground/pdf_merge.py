#A PDF Merge  Program
#Import a very powerful PDF library

import PyPDF2
import sys

#this takes the files from the system
#to merge
inputs = sys.argv[1:]
#this combines the list of PDFs
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        #merge everything into this merger object
        merger.append(pdf)
    #writes everything into the super.pdf file
    merger.write("super.pdf")
    
pdf_combiner(inputs)