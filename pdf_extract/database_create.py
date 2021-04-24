import re 
import sqlite3 
from layout_analysis import nutrient_list 

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

def insert_data(food): 
    string_value = (len(nutrient_list)+1)*'?,'  
    command_insertTable = "INSERT INTO {} VALUES ({})".format(string_NutrientCommand, string_value.rstrip(','))
    print(command_insertTable)
    nutrient_list.insert(0, food)
    nutrient_tuple = tuple(nutrient_list)
    cursor.execute(command_insertTable, nutrient_tuple)
    connection.commit() 

# due with this
# def insert_data(id, nutrient_list): 
#     for i in range(1, 44)):
#         command_insertTable = "INSERT INTO NutrientData({f_id}, {f_nutrient}) VALUES(?, ?)".format(f_id = id, f_nutrient = string_NutrientData[i])
#         c.execute(command_insertTable, ) 

def test_insert(): 
    cursor.execute("SELECT * FROM NutrientData")
    data = cursor.fetchall() 
    connection.commit()
    print(data)

insert_data("ga") 
test_insert() 