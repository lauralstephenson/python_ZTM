#A PDF Manipulation Program
#Import a very powerful PDF library

import PyPDF2

with open("dummy.pdf", "rb") as file:
  reader = PyPDF2.PdfReader(file)
  page = reader.pages[0]
  page.rotate(90)
  writer = PyPDF2.PdfWriter()
  writer.add_page(page)

# this rotation is in memory only
  with open("tilt.pdf", "wb") as new_file:
    writer.write(new_file)
