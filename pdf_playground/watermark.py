#A PDF Watermark Program
#Import a very powerful PDF library

import PyPDF2

template = PyPDF2.PdfReader(open("super.pdf", "rb"))
watermark = PyPDF2.PdfReader(open("wtr.pdf", "rb"))
output = PyPDF2.PdfWriter()

#loops through and adds the watermark to each page
for i in range(len(template.pages)):
      page = template.pages[i]
      #starts with the first page, page 0
      page.merge_page(watermark.pages[0])
      output.add_page(page)
      #A new file for the watermarked document
      with open("watermarked.pdf", "wb") as file:
            output.write(file)