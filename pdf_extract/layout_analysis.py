from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

# title_list = [] 
# title_formatted_list = [] 
# nutrient_name = [] # ["water"] 
# nutrient_list = {} # {"nutrient": ["mg", int amount]} 

box_general = [] 
box_sugar = [] 
box_micronutrients = [] 

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
        i+= 1 
        if i in range(109, 117): 
            box_general.append(element.get_text().rstrip('\n'))
        if i in range(133, 140): 
            box_sugar.append(element.get_text().rstrip('\n'))
        if i in range(117, 133): 
            box_micronutrients.append(element.get_text().rstrip('\n'))
        if i in range(140, 153): 
            box_micronutrients.append(element.get_text().rstrip('\n'))

nutrient_list = box_general + box_sugar + box_micronutrients

