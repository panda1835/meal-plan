from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pprint import pprint

title_list = [] 
title_formatted_list = [] 
nutrient_name = [] # ["water"] 
nutrient_list = {} # {"nutrient": ["mg", int amount]} 

document = open('G:/Programming/Meal-Plan/pdf_extract/demo_page.pdf', 'rb')
#Create resource manager
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
for page in PDFPage.get_pages(document):
    interpreter.process_page(page)
    # receive the LTPage object for the page.
    layout = device.get_result()
    i = 0 
    nutri_index = 0 
    nutri_index2 = 0 

    for element in layout:
        i += 1 
        if isinstance(element, LTTextBoxHorizontal): 
            #print(element, "index: ", i)
            pass 
        if i == 3: 
            title = element.get_text().split('\n')
            text = title[1] 
            title_list.append(text)
        if i >= 19 and i<= 63 : 
            nutrient = element.get_text().rstrip("\n")
            nutrient_name.append(nutrient)
            nutrient_list[nutrient] = []
        if i >= 64 and i <= 108: 
            if i == 66: 
                pass 
            unit = element.get_text().strip("\n")
            nutrient_list[nutrient_name[nutri_index]].append(unit) 
            nutri_index += 1 
        if i >= 109 and i <= 153: 
            amount = element.get_text().strip("\n")
            nutrient_list[nutrient_name[nutri_index2]].append(amount)  
            nutri_index2 += 1 

for key, value in nutrient_list.items():
    print(key, value)
           
             

        

