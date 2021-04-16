# Meal-Plan

***Meal-Plan is a digital solution aimed at helping Fulbright students create meal plans in such a way that would accommodate their personal nutritional needs as well as their financial and temporal constraints.***

***In the Meal-Plan Backend, Model.py is the program containing the code that focuses on the computation of Meal-Plan, i.e., processing the user's input and generate the meal plan.***

We will explain the functions used in *Model.py.* The following functions are used:

**def set_user_info(UserInfo):** 

​	""" 

​	*This function stores the user's information from survey to the meal plan database.* 

​	@parameters:

​							UserInfo: a dictionary containing the user's basic information

​    *Database: UserInfo*

​	@column:

​							nutrition_standard: String: the user's standard for nutrition

​    						height: Integers: user's height

​    						weight: Integers: user's weight

​    						age: Integers: user's age

​    						meal_list: List [String]: a list of meals

​	@return: none

​    """ 

**def get_user_info():**

​	"""

​	*This function fetches the latest update of the user's information from the database*

​	@parameters: none

​	@return: data: a list of the user's attributes

​	"""

**def set_user_nutritious_restriction():** 

​    """ 

​    *To be determined* 

​    """ 

​    pass 

 

**def get_user_nutritious_restriction():** 

​    """ 

​    *To be determined* 

​    """ 

​    pass 

 

**def set_user_defined_meal(UserDefinedMeal):** 

​    """ 

​    *This function store the user's pre-defined meal to the meal plan database* 

​    @parameters: 

​    						UserDefinedMeal: a dictionary containing the attributes of a defined meal

​    *Database: UserDefinedMeal* 

​    @column: 

​    						name: String: the name of the meal
​    						start_time: String (ex "12:00"): the meal starting time 
           end_time: String (ex "12:00"): the meal end time
           set_of_dishes: String: the types of dishes in this meal
           nutritious_restriction: To be determined #string
           regular: Boolean: true or false
           flexible: Boolean: true or false

​	@return: none

​    """

**def get_user_defined_meal_names():**

​	"""

​	*This function returns the meal names from the user's defined meals database*

​	@parameters: none

​	@return: data

​	""" 

**def get_user_defined_meal(meal_name):** 

​	"""

​	*This function gets the attributes of the meal from the database based on its name*

​	@parameters: meal_name (string): the name of the meal

​	@return: a tuple contains the information of meal_name, start_time, end_time, set_of_dishes, nutritious_restriction, regular, flexible 

​	""" 

**def set_recipe(Recipe):** 

​    """ 

​    *This function stores a new recipe to the recipe database* 

​    @parameters:

​    						Recipe: a dictionary containing the attributes of the recipe

​    *Database: Recipe* 

​    @column:

   						 recipe_name: String: the name of the recipe

   						 serving_size: Integer: the scale of the serving recipe

  						  cooking_time: Integer: the required to cook this recipe 

 						   tag: String category of the recipe 

​						    ingredient_name: String the ingredients contained in the recipe 

​						    amount: Float: the amount of the ingredient

 						   nutrition_name: String: the name of the nutrition

 						   energy: Float: the amount of energy for that meal

 						   steps_taken: String: method to cook the recipe 

​	@return: none

​    """ 

**def get_recipe_names():** 

​	"""

​	This function returns a list of recipe names in the Recipe database 

​	@parameters: none

​	@return: a tuple contains only recipes’ name in the database 

​	"""

**def get_recipe(name):** 

​	"""

​	This function returns a recipe object whose name is the recipe name 

​	Get the recipe data based on its name, including size of serving, cooking time, ingredient with the amount, and the nutrition with its energy.

​	@parameters: name(String): the name of the recipe

​	@return: a tuple of data contains the information of serving_size , cooking_time , tag, 	ingredient_name, amount , nutrition_name, energy, steps_taken

​	""" 

**def set_mealplan(period, # the period of the plan** 

​        free_time_to_cook, 

​        nutritious_restriction, 

​        recipes_list,  

​        precooked_meals, 

​        fixed_meals): 

 

​    

  def get_mealplan(self, period): 

​    pass 
