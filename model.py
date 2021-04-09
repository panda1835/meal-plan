import sqlite3
import json
import random

class Model:
    connection  = sqlite3.connect('mealplan.db')
    cursor = connection.cursor() 
    
    #the meal_list has to be string because sqlite cannot store list datatype
    #then using the json library to deserialize the meal list into string type

    command_create_user_info = '''
        CREATE TABLE IF NOT EXISTS 
        UserInfo(ID INTEGER PRIMARY KEY AUTOINCREMENT, nutrition_standard TEXT, height INTEGER, weight INTEGER, age INTEGER, plan_period TEXT)
    ''' 

    command_create_user_defined_meal = ''' 
        CREATE TABLE IF NOT EXISTS
        UserDefinedMeal(meal_name TEXT, start_time TEXT, end_time TEXT, 
                        set_of_dishes TEXT, nutritious_retriction TEXT, 
                        regular BOOLEAN, flexible BOOLEAN)
    ''' 

    command_create_recipe = '''
        CREATE TABLE IF NOT EXISTS
        Recipe(recipe_name TEXT, serving_size INTEGER, cooking_time INTEGER, tag TEXT,
                ingredient_name TEXT, amount FLOAT, nutrition_name TEXT,
                energy FLOAT, steps_taken TEXT)
    '''

    cursor.execute(command_create_user_info)
    cursor.execute(command_create_user_defined_meal) 
    cursor.execute(command_create_recipe)

    connection.commit()

    def __init__(self):
        pass

    def set_user_info(user_info):
        """ 

​	*This function stores the user's information from survey to the meal plan database.* 
​	@parameters:
​				user_info: a dictionary containing the user's basic information
​	@return: none
​    """ 
        nutrition_standard = user_info['nutrition_standard']
        height = user_info['height']
        weight = user_info['weight']
        age = user_info['age']
        plan_period = user_info['plan_period']

        Model.cursor.execute('''INSERT INTO UserInfo(nutrition_standard, height, weight, age, plan_period)
                        VALUES (?, ?, ?, ?, ?)''',
                        (nutrition_standard, height, weight, age, plan_period)) 

        Model.connection.commit()

    def get_user_info():
        """
​	    *This function fetches the latest update of the user's information from the database*
​	    @parameters: none
​	    @return:
                data: a tuple of the user's attributes: nutrition_standard, height, weight, age, plan_period
        """
        Model.cursor.execute(''' SELECT * FROM UserInfo ORDER BY ID DESC LIMIT 1''' )  
        data = Model.cursor.fetchone()
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

    def set_user_defined_meal(defined_meal_list):
        """ 
​       *This function store the user's pre-defined meal to the meal plan database* 
​       @parameters:
                user_defined_meal: a dictionary containing the attributes of a defined meal
​	    @return: none

​       """
        for user_defined_meal in defined_meal_list:
            meal_name = user_defined_meal['meal_name']
            set_of_dishes = user_defined_meal['set_of_dishes']
            nutritious_restriction = user_defined_meal['nutritious_restriction']
            regular = user_defined_meal['regular']
            flexible = user_defined_meal['flexible']
            start_time = user_defined_meal['start_time']
            end_time = user_defined_meal['end_time']

            set_of_dishes = json.dumps(set_of_dishes) #serialize list datatype

            Model.cursor.execute('''INSERT INTO UserDefinedMeal
                            VALUES (?, ?, ?, ?, ?, ?, ?)''',
                            (meal_name, start_time, end_time, set_of_dishes,
                            nutritious_restriction, regular,flexible)) 

            Model.connection.commit() 
        

    def get_user_defined_meal_names():
        """
​	    *This function returns the meal names from the user's defined meals database*
​	    @parameters: none
​	    @return: 
                data: a tuple of user's defined meal attributes:
                    meal_name, start_time, end_time, set_of_dishes, nutritious_restriction, regular, flexible 
​	    """ 
        # return list of Meal Names in UserDefinedMeal db
        Model.cursor.execute(''' SELECT * FROM UserDefinedMeal''' )  
        data = Model.cursor.fetchall()
        Model.connection.commit()

        return data


    def get_user_defined_meal(meal_name):
        """
​	    *This function gets the attributes of the meal from the database based on its name*
​	    @parameters: 
                    meal_name: the name of the meal
​	    @return: a tuple contains the information of meal_name, start_time, end_time, set_of_dishes, nutritious_restriction, regular, flexible 
​	    """ 

        Model.cursor.execute('''SELECT * FROM UserDefinedMeal
                                WHERE meal_name = (?)''', (meal_name,))
        data = Model.cursor.fetchall()
        Model.connection.commit()

        return data

    def set_recipe(recipe):
        """ 
​       *This function stores a new recipe to the recipe database* 
​       @parameters:
                recipe: a dictionary containing the attributes of the recipe
​	    @return: none
​       """ 
        recipe_name = recipe['recipe_name']
        serving_size = recipe['serving_size']
        cooking_time = recipe['cooking_time']
        tag = recipe['tag']
        ingredients = recipe['ingredients']
        nutritions = recipe['nutritions']
        steps_taken = recipe['steps_taken']

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
        """
​	    This function returns a list of recipe names in the Recipe database 
​	    @parameters: none
​	    @return: a tuple contains only recipes’ name in the database 
​	    """
        # return list of Recipe Names in Recipe db
        Model.cursor.execute(''' SELECT recipe_name FROM Recipe''')
        data = Model.cursor.fetchall()
        Model.connection.commit() 

        return data 

    def get_recipe(recipe_name):
        """
    ​	This function returns a recipe object whose name is the recipe name 
    ​	Get the recipe data based on its name, including size of serving, cooking time, ingredient with the amount, and the nutrition with its energy.
    ​	@parameters:
                    name: the name of the recipe
    ​	@return: 
                data: a tuple of recipe attributes based on the name:
                    recipe_name, serving_size, cooking_time, tag, ingredient_name, amount, nutrition_name, energy, steps_taken
        """
        # return Recipe object whose name is name
        Model.cursor.execute(''' SELECT * FROM Recipe 
                                WHERE recipe_name = (?) ''', (recipe_name,))
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
