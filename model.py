class Model:
	def __init__(self):
		'''
		Constructor 
		'''
		pass

	def user_info_to_database(nutrition_standard,
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
    def user_nutritious_restriction_to_database():
        """
        To be determined
        """
        pass

    def user_defined_meal_to_database(name,
                         time,
                         set_of_dishes,
                         nutritious_restriction,
                         regular,
                         flexible)

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

    def recipe_to_database(name,
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

	def mealplan(self, 
                 free_time_to_cook,
                 nutritious_restriction,
                 recipes_list,
                 precooked_meals,
                 fixed_meals):

        """
        Generate new mealplan
        """
		pass
  
