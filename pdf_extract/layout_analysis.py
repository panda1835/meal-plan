from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

#####################################################################
import re 
import sqlite3 
#from layout_analysis import nutrient_list 

connection = sqlite3.connect('nutrient_data.db')
cursor = connection.cursor()

raw_NutrientData = '''   
    Food 
    Nước (Water ) 
    Năng lượng (Energy ) 
    Protein 
    Lipid (Fat) 
    Glucid (Carbohydrate) 
    Celluloza (Fiber) 
    Tro (Ash) 
    Đường tổng số (Sugar) 
    Galactoza (Galactose) 
    Maltoza (Maltose)
    Lactoza (Lactose) 
    Fructoza  (Fructose) 
    Glucoza (Glucose) 
    Sacaroza (Sucrose) 
    Calci (Calcium) 
    Sắt (Iron) 
    Magiê (Magnesium)
    Mangan (Manganese) 
    Phospho (Phosphorous)
    Kali (Potassium)
    Natri (Sodium) 
    Kẽm  (Zinc) 
    Đồng (Copper) 
    Selen (Selenium) 
    Vitamin C (Ascorbic acid)
    Vitamin B1 (Thiamine)
    Vitamin B2 (Riboflavin) 
    Vitamin PP (Niacin) 
    Vitamin B5 (Pantothenic acid) 
    Vitamin B6 (Pyridoxine) 
    Folat (Folate) 
    Vitamin B9 (Folic acid) 
    Vitamin H (Biotin ) 
    Vitamin B12 (Cyanocobalamine) 
    Vitamin A (Retinol) 
    Vitamin D (Calciferol ) 
    Vitamin E  (Alpha-tocopherol )
    Vitamin K (Phylloquinone) 
    Beta_caroten 
    Alpha_caroten 
    Beta_cryptoxanthin 
    Lutein_Zeaxanthin 
    Lycopen 
    Purin '''

string_NutrientData = ""
for element in raw_NutrientData.split("\n"): 
    if element.strip() != '': 
        element = element.replace(" ", "")
        element = re.sub(r"\([^()]*\)", "", element)
        string_NutrientData += element + " TEXT" + ", "
string_NutrientData = string_NutrientData.rstrip(", ") 
string_NutrientData = "NutrientData(" + string_NutrientData + ")"

string_NutrientCommand = string_NutrientData.replace("TEXT", "")

def database_initialize(): 
    command_createNutritionData = 'CREATE TABLE IF NOT EXISTS {}'.format(string_NutrientData)
    cursor.execute(command_createNutritionData)
    connection.commit() 

def insert_data(food, food_list):
    string_value = (len(food_list)+1)*'?,'  
    command_insertTable = "INSERT INTO {} VALUES ({})".format(string_NutrientCommand, string_value.rstrip(','))
    food_list.insert(0, food)
    nutrient_tuple = tuple(food_list)
    cursor.execute(command_insertTable, nutrient_tuple)
    connection.commit() 

def test_insert(): 
    cursor.execute("SELECT * FROM NutrientData")
    data = cursor.fetchall() 
    connection.commit()
    print(data)

def process_string(word): 
    if '\n' in word: 
        correct_word = word.split("\n")[0]
        return correct_word 
    elif re.search("[^0-9|^.]", word):
        correct_word = None
        return correct_word


#####################################################################


box_general = [] 
box_sugar = [] 
box_micronutrients = [] 

document = open('G:/Programming/Meal-Plan/pdf_extract/demo_page_2.pdf', 'rb')
#Create resource manager
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
 

for page in PDFPage.get_pages(document):
    box_general = [] 
    box_sugar = [] 
    box_micronutrients = [] 

    interpreter.process_page(page)
    # receive the LTPage object for the page.
    layout = device.get_result()
    i = 0 
    nutri_index = 0 
    nutri_index_2 = 0 

    for element in layout: 
        i+= 1 
        if i == 3: 
            title = element.get_text().rstrip('\n')
            title = process_string(title)

        if i in range(109, 117): 
            word = element.get_text().rstrip('\n')
            word = process_string(word)
            box_general.append(word)

        if i in range(133, 140): 
            word = element.get_text().rstrip('\n')
            word = process_string(word)
            box_sugar.append(word)

        if i in range(117, 133): 
            word = element.get_text().rstrip('\n')
            word = process_string(word)
            box_micronutrients.append(word)

        if i in range(140, 153): 
            word = element.get_text().rstrip('\n')
            word = process_string(word)
            box_micronutrients.append(word)

    nutrient_list = box_general + box_sugar + box_micronutrients
    insert_data(title, nutrient_list)

test_insert() 
