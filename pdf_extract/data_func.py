from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def convert_pdf_to_string(file_path):
	output_string = StringIO()
	with open(file_path, 'rb') as in_file:
	    parser = PDFParser(in_file) # create pdf parser object associated with file object
	    doc = PDFDocument(parser) # create pdf document object storing document structure
	    rsrcmgr = PDFResourceManager() # create pdf resource manager stroce shared resources 
	    device = TextConverter(rsrcmgr, output_string, laparams=LAParams()) # create pdf device object 
	    interpreter = PDFPageInterpreter(rsrcmgr, device) # create pdf interpreter 
	    for page in PDFPage.create_pages(doc): # process page content in the document 
	        interpreter.process_page(page)

	return(output_string.getvalue())

def covert_title_to_filename(title): 
	filename = title.lower() 
	filename = filename.replace(" ", "_")
	return filename

def func_cmyffdnp(title_and_pagenum, i):
    while title_and_pagenum[i].isdigit():
        i -= 1
    return i

def split_to_title_and_pagenum(contents_table): 
	title_pagenum = contents_table.strip() 
	
	title = None 
	pagenum = None 

	if len(title_pagenum) > 0: 
		if title_pagenum[-1].isdigit(): 
			i = -2 
			while(title_pagenum[i].isdigit()): 
				i -= 1 
			title = title_pagenum[:i].strip() 
			pagenum = int(title_pagenum[i:].strip())
	
	return(title, pagenum)