class Model:
    def __init__(self):
        '''
        Constructor 
        '''
        pass

    def set_user_info(self, nutrition_standard,
                           height,
                           weight,
                           age,
                           meal_list):
        """
        Store user info from surveys to database
        @param
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

        pass

    def get_user_info(self):

        # return User
        pass

    def set_user_nutritious_restriction(self):
        """
        To be determined
        """
        pass

    def get_user_nutritious_restriction(self):

        # return TBD
        pass

    def set_user_defined_meal(self,name,
                         time,
                         set_of_dishes,
                         nutritious_restriction,
                         regular,
                         flexible):

        """
        Store user defined meal to database
        @param
        name: String
        time: [Int, Int, Int, Int]
        set_of_dishes: List<String>
        nutritious_restriction: To be determined
        regular: Bol
        flexible: Bol

        Database: UserDefinedMeal
        @column
        name: String
        start_time: String (ex "12:00")
        end_time: String (ex "12:00")
        set_of_dishes: String 
        nutritious_restriction: To be determined
        regular: Bol
        flexible: Bol
        """
        
        pass

    def get_user_defined_meal_names(self):
        # return list of Meal Names in UserDefinedMeal db

        pass

    def get_user_defined_meal(self, name):

        # return Meal object whose name is name
        pass
    
    def set_recipe(self, name,
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
        pass 

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
