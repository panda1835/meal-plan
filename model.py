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
        Recipe(name TEXT, serving_size INTEGER, cooking_time INTEGER, tag TEXT,
                ingredient_name TEXT, amount INT, nutrition_name TEXT
                energy INTEGER, steps_taken TEXT)
    '''

    command_createMealPlan = ''' 
        CREATE TABLE IF NOT EXISTS
        MealPlan()
    ''' 

    cursor.execute(command_createUserInfo)
    cursor.execute(command_createUserDefinedMeal) 
    cursor.execute(command_createRecipe)

    connection.commit()

    def __init__(self):
        pass

    def set_user_info(self, nutrition_standard, height, weight, age, meal_list,):
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
                        VALUES (%s, %s, %s, %s, %s)''',
                        (nutrition_standard, height, weight, age, meal_list)) 

        Model.connection.commit()

    def get_user_info(self):
        Model.cursor.execute(''' SELECT * FROM UserInfo ''' )  
        data = Model.connection.fetchone()

        return data 

    def set_user_nutritious_restriction(self):
        """
        To be determined
        """
        pass

    def get_user_nutritious_restriction(self):
        """
        To be determined
        """
        pass

    def set_user_defined_meal(self, meal_name, time, set_of_dishes,
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
                        VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                        (meal_name, start_time, end_time, set_of_dishes,
                        nutritious_restriction, regular,flexible)) 

        Model.connection.commit() 
        

    def get_user_defined_meal_names(self):
        # return list of Meal Names in UserDefinedMeal db
        Model.cursor.execute(''' SELECT name FROM UserDefinedMeal ''' )  
        data = Model.connection.fetchall()
        Model.connection.commit()

        return data


    def get_user_defined_meal(self, meal_name):

        Model.cursor.execute('''SELECT * FROM UserDefinedMeal
                                WHERE name = (%s)''', meal_name)
        data = Model.connection.fetchone() 
        Model.connection.commit()

        return data
        
    
    def set_recipe(self, recipe_name, serving_size, cooking_time, tag,
                    ingredients, nutritions, steps_taken):
        """
        Store new recipe to database
        @param
        recipe_name: String
        serving_size: Int
        cooking_time: Int
        tag: String
        ingredients: (String, Int)
        nutritions: (String, Int)
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
        ingredient = ingredients[0]
        amount = ingredients[1]  
        nutrition_name = nutritions[0] 
        energy = nutritions[1]  

        Model.cursor.execute('''INSERT INTO Recipe
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                        (recipe_name, serving_size, cooking_time, tag, 
                        ingredient, amount, 
                        nutrition_name, energy,
                        steps_taken))
        
        Model.connection.commit()

    def get_recipe_names(self):
        # return list of Recipe Names in Recipe db
        Model.cursor.execute(''' SELECT recipe_name FROM Recipe''')
        data = Model.connection.fetchall() 
        Model.connection.commit() 

        return data 

    def get_recipe(self, name):#  
        # return Recipe object whose name is name
        Model.cursor.execute(''' SELECT * FROM Recipe 
                                WHERE recipe_name = %s ''', name) 
        data = Model.connection.fetchone()
        Model.connection.commit()
        return data

    def set_mealplan(self,
                period, # the period of the plan  
                free_time_to_cook,
                nutritious_restriction,
                recipes_list,
                precooked_meals,
                fixed_meals):

        meal_plan = []
        meal_plan += fixed_meals + precooked_meals
        for nutrient in nutritious_restriction:
            nutritious_restriction[nutrient] -= fixed_meals.nutrient

        while not nutritious_restriction.isEmpty():
            random_recipe = random.choice(recipes_list)
            if is_suitable(random_recipe, nutritious_restriction):
                meal_plan.add(random_recipe)

	    return mealplan

    def get_mealplan(self, period):
        pass
