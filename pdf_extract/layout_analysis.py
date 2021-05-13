from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
import re 
import sqlite3 

connection = sqlite3.connect('nutrient_data.db')
cursor = connection.cursor()

raw_NutrientData = '''   
    Food
    Calci (Calcium) 
    Sat (Iron) 
    Magie (Magnesium)
    Mangan (Manganese) 
    Phospho (Phosphorous)
    Natri (Sodium) 
    Kem (Zinc) 
    Dong (Copper) 
    Selen (Selenium) 
    Vitamin C (Ascorbic acid)
    Vitamin B1 (Thiamine)
    Vitamin B2 (Riboflavin) 
    Vitamin PP (Niacin) 
    Vitamin B5 (Pantothenic acid) 
    Vitamin B6 (Pyridoxine) 
    Folat (Folate) 
    Vitamin H (Biotin ) 
    Vitamin B12 (Cyanocobalamine) 
    Vitamin A (Retinol) 
    Vitamin D (Calciferol ) 
    Vitamin E  (Alpha-tocopherol )
    Vitamin K (Phylloquinone) 
'''

string_NutrientData = ""
for element in raw_NutrientData.split("\n"): 
    if element.strip() != '': 
        element = element.replace(" ", "")
        element = re.sub(r"\([^()]*\)", "", element)
        string_NutrientData += element + " TEXT" + ","
string_NutrientData = string_NutrientData.rstrip(",") 
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
    data = cursor.fetchone() 
    connection.commit()
    print(data)

def process_string(word): 
    if '\n' in word: 
        word = word.split("\n")[0]
    
    if re.search("[^0-9|^.]", word):
        word = None

    return word 

def create_database(): 
    box_micronutrients = [] 

    document = open('G:/Programming/Meal-Plan/pdf_extract/group_4.pdf', 'rb')
    #Create resource manager
    rsrcmgr = PDFResourceManager()
    # Set parameters for analysis.
    laparams = LAParams()
    # Create a PDF page aggregator object.
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    

    for page in PDFPage.get_pages(document):
        # box_general = [] 
        # box_sugar = [] 
        box_micronutrients = [] 

        interpreter.process_page(page)
        # receive the LTPage object for the page.
        layout = device.get_result()
        i = 0 
        nutri_index = 0 
        nutri_index_2 = 0 

        for element in layout: 
            i+= 1 
            
            if i == 4: 
                title = element.get_text().rstrip('\n')
                print(title)

            if i in range(117, 133) and i != 122:  
                word = element.get_text().rstrip('\n')
                word = process_string(word)
                box_micronutrients.append(word)

            if i in range(140, 148) and i != 141: 
                word = element.get_text().rstrip('\n')
                word = process_string(word)
                box_micronutrients.append(word)

        nutrient_list = box_micronutrients
        
        
        insert_data(title, nutrient_list)
    
def get_nutrition(meal, nutrition): 
    connection = sqlite3.connect('nutrient_data.db')
    cursor = connection.cursor() 

    cursor.execute('''SELECT * FROM NutrientData
                        WHERE Food = ?''', [meal])
    data = cursor.fetchall()
    connection.commit() 
    if nutrition == "Calci": return data[1]
    if nutrition == "Sat": return data[2] 
    if nutrition == "Magie": return data[3]  
    if nutrition == "Mangan": return data[4]  
    if nutrition == "Phospho": return data[5]
    if nutrition == "Natri": return data[4] 
    if nutrition == "Kem": return data[5]
    if nutrition == "Dong": return data[6]
    if nutrition == "Selen": return data[7]
    if nutrition == "VitaminC": return data[8]
    if nutrition == "VitaminB1": return data[9] 
    if nutrition == "VitaminB2": return data[10]
    if nutrition == "VitaminPP": return data[11]  
    if nutrition == "VitaminB5": return data[12] 
    if nutrition == "VitaminB6": return data[13]
    if nutrition == "Folat": return data[14]
    if nutrition == "VitaminH": return data[15]
    if nutrition == "VitaminB12": return data[16]
    if nutrition == "VitaminA": return data[17]
    if nutrition == "VitaminD": return data[18]
    if nutrition == "VitaminE": return data[19] 
    if nutrition == "VitaminK": return data[20]
