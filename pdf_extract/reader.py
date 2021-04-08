import PyPDF2
import data_func
import csv

reader = PyPDF2.PdfFileReader("G:/Programming/Meal-Plan/pdf_extract/VTN_FCT_2007.pdf", strict = False)
num_of_pages = reader.numPages
print('Number of pages: ' + str(num_of_pages))

writer = PyPDF2.PdfFileWriter() # writing PDF File out

for page in range(14, 15):  
    writer.addPage(reader.getPage(page))

output_filename = 'G:/Programming/Meal-Plan/pdf_extract/demo_page.pdf'

with open(output_filename, 'wb') as output: 
    writer.write(output) 

text = data_func.convert_pdf_to_string('G:/Programming/Meal-Plan/pdf_extract/demo_page.pdf')
text = text.replace('.', '')
text = text.replace('\x0c', '')
table_of_contents_raw = text.split('\n')
for line in table_of_contents_raw: 
    print(line.strip())

# print(" *********************TEXT****************")
# print(text)
# print("**********************TABLE OF CONTEXT***************")
# print(table_of_contents_raw)

"""
title_list = [] 
pagenum_list = [] 
title_formatted_list = [] 

for item in table_of_contents_raw:
    title, pagenum =  data_func.split_to_title_and_pagenum(item)
    if title != None:
        title_list.append(title)
        pagenum_list.append(pagenum)
        title_formatted_list.append(
            data_func.convert_title_to_filename(title))
    
# for page_list, we need to add the last page as well
pagenum_list.append(num_of_pages + 1)

print("*******TITLE LIST*********")
print(title_list)
print("*******PAGENUM LIST*********")
print(pagenum_list)
print("***********TITLE FORMATTED LIST************")
print(title_formatted_list)
"""