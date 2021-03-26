import sqlite3
import json

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

    cursor.execute(command_createUserInfo)
    cursor.execute(command_createUserDefinedMeal) 
    cursor.execute(command_createRecipe)

    connection.commit()

    def __init__(self, nutrition_standard, height, weight, age, meal_list,
                meal_name, time, set_of_dishes, nutritious_restriction, regular, flexible):
        
        self.nutrition_standard = nutrition_standard
        self.height = height
        self.weight = weight
        self.age = age
        self.meal_list = meal_list
        self.meal_name = meal_name
        self.time = time
        self.set_of_dishes = set_of_dishes
        self.nutritious_restriction = nutritious_restriction
        self.regular = regular
        self.flexible = flexible

    def set_user_info(self):
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
        self.meal_list = json.dumps(self.meal_list) #convert into str type
        Model.cursor.execute('''INSERT INTO UserInfo
                        VALUES (%s, %s, %s, %s, %s)''',
                        (self.nutrition_standard, self.height, self.weight, self.age, self.meal_list)) 

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

    def set_user_defined_meal(self):

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
        start_time = str(self.time[0]) + ":" + str (self.time[1])
        end_time = str(self.time[2]) + ":" + str(self.time[3])

        self.set_of_dishes = json.dumps(self.set_of_dishes) #serialize list datatype

        Model.cursor.execute('''INSERT INTO UserDefinedMeal
                        VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                        (self.meal_name, start_time, end_time, self.set_of_dishes,
                        self.nutritious_restriction, self.regular, self.flexible)) 

        Model.connection.commit() 
        

    def get_user_defined_meal_names(self):
        # return list of Meal Names in UserDefinedMeal db
        Model.cursor.execute(''' SELECT name FROM UserDefinedMeal ''' )  
        data = Model.connection.fetchall()
        Model.connection.commit()

        return data 


    def get_user_defined_meal(self, meal_name):

        Model.cursor.execute('''SELECT * FROM UserDefinedMeal WHERE name = (%s)''', self.meal_name)
        data = Model.connection.fetchone() 
        Model.connection.commit()

        return data
        
    
    def set_recipe(self, recipe_name,
                        serving_size,
                        cooking_time,
                        tag,
                        ingredients,
                        nutritions,
                        steps_taken):
        """
        Store new recipe to database
        @param
        name: String
        serving_size: Int
        cooking_time: Int
        tag: String
        ingredients: (String, Int)
        nutritions: (String, Int)
        steps_taken: String
        
        Database: Recipe
        @column
        name: String
        serving_size: Int
        cooking_time: Int
        tag: String
        ingredient_name: String
        amount: Int
        nutrition_name: String
        energy: Int
        steps_taken: String
        """
        #self.meal_list = json.dumps(self.meal_list) #convert into str type
        Model.cursor.execute('''INSERT INTO Recipe
                        VALUES (%s, %s, %s, %s)''',
                        (self.name, self.serving_size, self.tag, 
                        self.ingredient_name, self.height, self.weight, self.age, self.meal_list)) 

        Model.connection.commit()

    def get_recipe_names(self):
        # return list of Recipe Names in Recipe db

        pass


    def get_recipe(self, name):

        # return Recipe object whose name is name
        pass

    def set_mealplan(self,
                period, # the period of the plan  
                free_time_to_cook,
                nutritious_restriction,
                recipes_list,
                precooked_meals,
                fixed_meals):

        """
        Generate new mealplan
        """
    pass

    def get_mealplan(self, period):

        """
        get mealplan of a specific period
        """
    pass
