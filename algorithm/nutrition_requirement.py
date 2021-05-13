import re
import sqlite3 


nutrition = {"VitaminA": "", "VitaminC": "", "VitaminD": "", "VitaminE": "", "VitaminK": "", "VitaminB1": "", "VitaminB2": "", "VitaminPP": "",
"VitaminB6": "", "Folat": "", "VitaminB12": "", "VitaminB5": "", "VitaminH": "",
"Calci": "", "Dong" : "", "Sat":"", "Magie":"", "Mangan":"", "Phospho": "", "Selen": "", "Kem": "", "Natri": ""} 

children_1_3_lower = '''13 300	15	15	6	30*	0.5	0.5	6	0.5	150	0.9   2*	8*
						700	340	7	80	1.2*	460	20	3	1.0*	
'''

children_4_8_lower = '''400	25	15	7	55*	0.6	0.6	8	0.6	200	1.2	3*	12*"
                        1,000	440	10	130	1.5*	500	30	5	1.2*	
'''

males_9_13_lower = ''' 600	45	15	11	60* 0.9	0.9	12	1.0	300	1.8	4* 
					    1,300	700	8	240	 1.9*	1,250	40	8	1.5*		
'''

males_14_18_lower = '''900	75	15	15	75*	1.2	1.3	16	1.3	400	2.4	5*
                        1,300	890	11	410	2.2*	1,250	55	11	1.5*	
'''

males_19_30_lower = '''900	90	15	15	120*	1.2	1.3	16	1.3	400	2.4	5*	30*
                        1,000	900	18	310	1.8*	700	55	8	1.5*	
''' 

males_31_50_lower =	'''900 90	15	15	120*	1.2	1.3	16	1.3	400	2.4	5*	30* 
                        1,000	900	18	320	1.8*	700	55	8	1.5*
'''

males_51_70_lower = '''900	90	15	15	120*	1.2	1.3	16	1.7	400	2.4	5*	30*
                        1,200	900	8	320	1.8*	700	55	8	1.3*
                        ''' 

males_70_lower = '''900 90	20	15	120*	1.2	1.3	16	1.7	400	2.4	5*	30*
                    1,200	900	8	320	1.8*	700	55	8	1.2*	''' 
										
females_9_13_lower = '''600	45	15	11	60* 0.9	0.9	12	1.0	300	1.8	4*	20*
					1,300	700	8	240 	1.6*	1,250	40	8	1.5*	
                    '''

females_14_18_lower = '''700	65	15	15	75*	1.0	1.0	14	1.2	400	2.4	5*	25*
                    1,300	890	15	360	1.6*	1,250	55	9	1.5*'''

females_19_30_lower = '''700	75	15	15	90*	1.1	1.1	14	1.3	400	2.4	5*	30*
                    1,000	900	18	310	1.8*	700	55	8	1.5*''' 

females_31_50_lower = '''700	75	15	15	90*	1.1	1.1	14	1.3	400	2.4	5*	30*
                    1,000	900	18	320	1.8*	700	55	8	1.5*''' 

females_51_70_lower = '''700	75	15	15	90*	1.1	1.1	14	1.5	400	2.4	5*	30*
                    1,200	900	8	320	1.8*	700	55	8	1.3*''' 

females_70_lower =  '''700	75	20	15	90*	1.1	1.1	14	1.5	400	2.4	5*	30*
                    1,200	900	8	320	1.8*	700	55	8	1.2*''' 


def get_lowerbound(sex, age): 
    '''
    Return the minimum nutrition that a person have to consume base on his age and sex 
    Param: 
        sex (str): the gender of the user 
        age (int): the age of the user 
    Return: 
        nutrition (dict): a collection data of nutrition 
    '''
    
    if sex == "male": 
        if 1 <= age <=3: nutrition_status = children_1_3_lower 
        elif 4 <= age <= 8: nutrition_status = children_4_8_lower
        elif 9 <= age <= 13: nutrition_status = males_9_13_lower
        elif 14 <= age <= 18: nutrition_status = males_14_18_lower 
        elif 19 <= age <= 30: nutrition_status = males_19_30_lower
        elif 31 <= age <= 50: nutrition_status = males_31_50_lower 
        elif 51 <= age <= 70: nutrition_status = males_51_70_lower 
        elif age > 70: nutrition_status = males_70_lower 
    elif sex == "female":
        if 1 <= age <=3: nutrition_status = children_1_3_lower 
        elif 4 <= age <= 8: nutrition_status = children_4_8_lower
        elif 9 <= age <= 13: nutrition_status = females_9_13_lower
        elif 14 <= age <= 18: nutrition_status = females_14_18_lower 
        elif 19 <= age <= 30: nutrition_status = females_19_30_lower
        elif 31 <= age <= 50: nutrition_status = females_31_50_lower 
        elif 51 <= age <= 70: nutrition_status = females_51_70_lower 
        elif age > 70: nutrition_status = females_70_lower 
    

    nutrition_status = re.sub(r'\*', '', nutrition_status)
    nutrition_status = re.sub(r'\,', '', nutrition_status)
    nutrition_status = nutrition_status.split()

    for nutrient, amount in zip(nutrition, nutrition_status): 
        nutrition[nutrient] = amount 
    
    return nutrition

def test_lowerbound():
    '''
    Test the function get_lowerbound whether it functions or not 
    '''
    sex = input("Enter the gender: ")
    age = int(input("Enter the age: "))
    print(get_lowerbound(sex, age))


children_1_3_upper = '''	
600	400	63	200	ND	ND	ND	10	30	300	ND	ND	ND	
2,500	1,000	40	65	2	3	90	7	1.5
'''

children_4_8_upper = '''
900	650	75	300	ND	ND	ND	15	40	400	ND	ND	ND
2,500	3,000	40	110	3	3	150	12	1.9
'''

males_9_13_upper = ''' 
1,700	1,200	100	600	ND	ND	ND	20	60	600	ND	ND	ND	
3,000	5,000	40	350	6	4	280	23	2.2

'''

males_14_18_upper = '''
2,800	1,800	100	800	ND	ND	ND	30	80	800	ND	ND	ND
3,000	8,000	45	350	9	4	400	34	2.3
'''

males_19_30_upper = '''
3,000	2,000	100	1,000	ND	ND	ND	35	100	1,000	ND	ND	ND
2,500	10,000	45	350	11	4	400	40	2.3
''' 

males_31_50_upper =	'''
3,000	2,000	100	1,000	ND	ND	ND	35	100	1,000	ND	ND	ND
2,500	10,000	45	350	11	4	400	40	2.3
'''

males_51_70_upper = '''
3,000	2,000	100	1,000	ND	ND	ND	35	100	1,000	ND	ND	ND
2,000	10,000	45	350	11	4	400	40	2.3
''' 

males_70_upper = '''
3,000	2,000	100	1,000	ND	ND	ND	35	100	1,000	ND	ND	ND
2,000	10,000	45	350	11	3	400	40	2.3
''' 
										
females_9_13_upper = '''
1,700	1,200	100	600	ND	ND	ND	20	60	600	ND	ND	ND
3,000	5,000	40	350	6	4	280	23	2.2

'''

females_14_18_upper = '''
2,800	1,800	100	800	ND	ND	ND	30	80	800	ND	ND	ND	
3,000	8,000	45	350	9	4	400	34	2.3	
'''

females_19_30_upper = '''
3,000	2,000	100	1,000	ND	ND	ND	35	100	1,000	ND	ND	ND
2,500	10,000	45	350	11	4	400	40	2.3
''' 

females_31_50_upper = '''
3,000	2,000	100	1,000	ND	ND	ND	35	100	1,000	ND	ND	ND
2,500	10,000	45	350	11	4	400	40	2.3
''' 

females_51_70_upper = '''
3,000	2,000	100	1,000	ND	ND	ND	35	100	1,000	ND	ND	ND
2,000	10,000	45	350	11	4	400	40	2.3
''' 

females_70_upper =  '''
3,000	2,000	100	1,000	ND	ND	ND	35	100	1,000	ND	ND	ND
2,000	10,000	45	350	11	3	400	40	2.3
''' 

def get_upperbound(sex, age):
    '''
    Return the maximun nutrition that a person can consume base on his age and sex 
    Param: 
        sex (str): the gender of the user 
        age (int): the age of the user 
    Return: 
        nutrition (dict): a collection data of nutrition 

    '''
    if sex == "male": 
        if 1 <= age <=3: nutrition_status = children_1_3_upper
        elif 4 <= age <= 8: nutrition_status = children_4_8_upper
        elif 9 <= age <= 13: nutrition_status = males_9_13_upper
        elif 14 <= age <= 18: nutrition_status = males_14_18_upper 
        elif 19 <= age <= 30: nutrition_status = males_19_30_upper
        elif 31 <= age <= 50: nutrition_status = males_31_50_upper 
        elif 51 <= age <= 70: nutrition_status = males_51_70_upper 
        elif age > 70: nutrition_status = males_70_upper 
    elif sex == "female":
        if 1 <= age <=3: nutrition_status = children_1_3_upper 
        elif 4 <= age <= 8: nutrition_status = children_4_8_upper
        elif 9 <= age <= 13: nutrition_status = females_9_13_upper
        elif 14 <= age <= 18: nutrition_status = females_14_18_upper 
        elif 19 <= age <= 30: nutrition_status = females_19_30_upper
        elif 31 <= age <= 50: nutrition_status = females_31_50_upper 
        elif 51 <= age <= 70: nutrition_status = females_51_70_upper 
        elif age > 70: nutrition_status = females_70_upper 
    

    nutrition_status = re.sub(r'\*', '', nutrition_status)
    nutrition_status = re.sub(r'\,', '', nutrition_status)
    nutrition_status = nutrition_status.split()

    for nutrient, amount in zip(nutrition, nutrition_status): 
        nutrition[nutrient] = amount 
    
    return nutrition

def test_upperbound(): 
    ''' 
    Test the get_upperbound function whether it functions or not 
    ''' 
    sex = input("Enter the gender: ")
    age = int(input("Enter the age: "))
    print(get_upperbound(sex, age))


def get_nutritional_value(meal, nutrition): 
    '''
    Connect to the database to extract the amount of a nutrition from a meal
    Param: 
        meal (str): name of the meal 
        nutrition (int): amount of the nutrition
    Return: 
        (int): the amount of the nutrition 

    '''
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