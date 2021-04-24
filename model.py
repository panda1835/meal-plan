import sqlite3
import json
import random

class Model:
    connection  = sqlite3.connect('mealplan.db')
    cursor = connection.cursor() 
    
    #the meal_list has to be string because sqlite cannot store list datatype
    #then using the json library to deserialize the meal list into string type

    command_createUserInfo = '''
        CREATE TABLE IF NOT EXISTS 
        UserInfo(nutrition_standard TEXT, height INTEGER, weight INTEGER, age INTEGER, meal_list TEXT)
    ''' 

    command_createUserDefinedMeal = ''' 
        CREATE TABLE IF NOT EXISTS
        UserDefinedMeal(name TEXT, start_time TEXT, end_time TEXT, 
                        set_of_dishes TEXT, nutritious_retriction TEXT, 
                        regular BOOLEAN, flexible BOOLEAN)
    ''' 

    command_createRecipe = '''
        CREATE TABLE IF NOT EXISTS
        Recipe(recipe_name TEXT, serving_size INTEGER, cooking_time INTEGER, tag TEXT,
                ingredient_name TEXT, amount INT, nutrition_name TEXT,
                energy INTEGER, steps_taken TEXT)
    '''

    cursor.execute(command_createUserInfo)
    cursor.execute(command_createUserDefinedMeal) 
    cursor.execute(command_createRecipe)

    connection.commit()

    def __init__(self):
        pass

    def set_user_info(nutrition_standard, height, weight, age, meal_list,):
        """
        Store user info from surveys to database
        @param
        ???username:String???
        nutrition_standard: String
        height: Int
        weight: Int
        age: Int
        meal_list: List<String>
        Database: UserInfo
        @column
        nutrition_standard: String
        height: Int
        weight: Int
        age: Int
        meal_list: List<String>
        """
        meal_list = json.dumps(meal_list) #convert into str type
        Model.cursor.execute('''INSERT INTO UserInfo
                        VALUES (?, ?, ?, ?, ?)''',
                        (nutrition_standard, height, weight, age, meal_list)) 

        Model.connection.commit()

    def get_user_info():
        Model.cursor.execute(''' SELECT * FROM UserInfo ''' )  
        data = Model.cursor.fetchall()
        Model.connection.commit()

        return data 

    def set_user_nutritious_restriction():
        """
        To be determined
        """
        pass

    def get_user_nutritious_restriction():
        """
        To be determined
        """
        pass

    def set_user_defined_meal(meal_name, time, set_of_dishes,
                            nutritious_restriction, regular, flexible,):

        """
        Store user defined meal to database
        @param
        name: String
        time: [Int, Int, Int, Int]
        set_of_dishes: List<String> 
        nutritious_restriction: To be determined
        regular: Bool
        flexible: Bool
        Database: UserDefinedMeal
        @column
        name: String
        start_time: String (ex "12:00")
        end_time: String (ex "12:00")
        set_of_dishes: String 
        nutritious_restriction: To be determined #string
        regular: Bool
        flexible: Bool
        """        
        start_time = str(time[0]) + ":" + str(time[1])
        end_time = str(time[2]) + ":" + str(time[3])

        set_of_dishes = json.dumps(set_of_dishes) #serialize list datatype

        Model.cursor.execute('''INSERT INTO UserDefinedMeal
                        VALUES (?, ?, ?, ?, ?, ?, ?)''',
                        (meal_name, start_time, end_time, set_of_dishes,
                        nutritious_restriction, regular,flexible)) 

        Model.connection.commit() 
        

    def get_user_defined_meal_names():
        # return list of Meal Names in UserDefinedMeal db
        Model.cursor.execute(''' SELECT name FROM UserDefinedMeal ''' )  
        data = Model.cursor.fetchall()
        Model.connection.commit()

        return data


    def get_user_defined_meal(meal_name):

        Model.cursor.execute('''SELECT * FROM UserDefinedMeal
                                WHERE name = (?)''', (meal_name,))
        data = Model.cursor.all()
        Model.connection.commit()

        return data

    def set_recipe(recipe_name, serving_size, cooking_time, tag,
                    ingredients, nutritions, steps_taken):
        """
        Store new recipe to database
        @param
        recipe_name: String
        serving_size: Int
        cooking_time: Int                 # i think this need to be float
        tag: String
        ingredients: (String, Int)
        nutritions: (String, Int)         # i think this need to be float
        steps_taken: String
        
        Database: Recipe
        @column
        recipe_name: String
        serving_size: Int
        cooking_time: Int
        tag: String
        ingredient_name: String
        amount: Int
        nutrition_name: String
        energy: Int
        steps_taken: String
        """
        ingredient_name = ingredients[0]
        amount = ingredients[1]  
        nutrition_name = nutritions[0] 
        energy = nutritions[1]  

        Model.cursor.execute('''INSERT INTO Recipe
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (recipe_name, serving_size, cooking_time, tag, 
                        ingredient_name, amount,
                        nutrition_name, energy,
                        steps_taken))
        
        Model.connection.commit()

    def get_recipe_names():
        # return list of Recipe Names in Recipe db
        Model.cursor.execute(''' SELECT recipe_name FROM Recipe''')
        data = Model.cursor.fetchall()
        Model.connection.commit() 

        return data 

    def get_recipe(name):#
        # return Recipe object whose name is name
        Model.cursor.execute(''' SELECT * FROM Recipe 
                                WHERE recipe_name = (?) ''', (name,))
        data = Model.cursor.fetchone()
        Model.connection.commit()
        return data

 
    def set_mealplan(period, # the period of the plan
                free_time_to_cook, 
                nutritious_restriction, 
                recipes_list,  
                precooked_meals, 
                fixed_meals): 

        # get recipe_list and its cooking time 
        Model.cursor.execute('''SELECT recipe_name, cooking_time  
                                FROM Recipe''') 
        food =  Model.cursor.fetchall()

        # update nutritous_retriction in database UserDefinedMeal 
        Model.cursor.execute(''' UPDATE retrictious_restriction r 
                    SET r.retrictious_restriction = ? 
                ''', nutritious_restriction) 

        # get nutritous_retriction 
        Model.cursor.execute('''SELECT nutritous_retriction FROM UserDefinedMeal''') 
        nutritious_restriction = Model.cursor.fetchone() #str type
        json.loads(nutritious_restriction) # convert to list  

        meal_plan = [] 
        meal_plan += fixed_meals + precooked_meals 
        for nutrient in nutritious_restriction:
            nutritious_restriction[nutrient] -= fixed_meals.nutrient 

        while not nutritious_restriction.isEmpty(): 
            for row in random.choice(food):  
                for recipe, time_cooking in row:  
                    if time_cooking < free_time_to_cook:  
                        meal_plan.append(recipe)             
        return meal_plan 

    def get_mealplan(self, period):
        pass