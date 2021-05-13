import PyPDF2
import csv

reader = PyPDF2.PdfFileReader("G:/Programming/Meal-Plan/pdf_extract/VTN_FCT_2007.pdf", strict = False)
num_of_pages = reader.numPages
print('Number of pages: ' + str(num_of_pages))

writer = PyPDF2.PdfFileWriter() # writing PDF File out

for page in range(231, 286):  
    writer.addPage(reader.getPage(page))

output_filename = 'G:/Programming/Meal-Plan/pdf_extract/group_5.pdf'

with open(output_filename, 'wb') as output: 
    writer.write(output) 

