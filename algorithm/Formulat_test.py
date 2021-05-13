from nutrition_requirement import get_lowerbound, get_upperbound, get_nutritional_value 

current_nutrition = {}

def get_food_list():
    return []
def get_nutrient_list():
    return []

def add_food(food):
    """
    Retrieve the nutritional value of each nutrient in the food and add them
    to the dictionary of existing nutritions
    param: food: the current food being considered from the dish
    param: sex, age: the sex and age of the use to get the lower and upperbound 
    return: the dictionary of nutrients after adding a new food 
    """
    for nutrient in current_nutrition:
        value = get_nutritional_value(food, nutrient)
        current_nutrition[nutrient] += value
    return current_nutrition

def remove_food(food):
    """
    Retrieve the nutritional value of each nutrient in the food and remove them
    from the dictionary of existing nutrition if it exceed the upperbound
    param: food: the current food being considered from the dish
    param: sex, age: the sex and age of the use to get the lower and upperbound 
    return: the dictionary of nutrients after adding a new food 
    """
    for nutrient in current_nutrition:
        value = get_nutritional_value(food, nutrient)
        current_nutrition[nutrient] -= value
    return current_nutrition

def check_overflow(current_nutrition, sex, age):
    """
    Checks if after adding a dish it would cause any nutrient to exceed 
    its upperbound
    param: current_nutrition: the list of nutritional values of nutrients the
    meal plan currently has
    param: sex, age: the sex and age of the user to get the lower and upperbound
    of the nutrient
    return: True if there is an overflow in any nutrient in the dictionary,
    False otherwise 
    """
    for nutrient in current_nutrition:
        UB = get_upperbound(sex, age)[nutrient]
        LB = get_lowerbound(sex, age)[nutrient]
        if current_nutrition[nutrient] > UB or current_nutrition[nutrient] == UB:
            return True
    return False

def calculate_nutrition(sex, age):
    """
    Calculates the nutritions from each food of each dish being added into the 
    meal plan
    param: sex, age: the sex and age of the user to get the lower and upperbound
    of the food being added
    return: the dictionary of nutritional values of the nutrients
    """
    # get the list of 100 random dishes
    food_list = get_food_list()
    # find the nutrient in the food and add the value to the current nutrition
    for food in list(food_list):
        current_nutrition = add_food(food, sex, age)          
        # check if any nutrient exceeds the UB
        if check_overflow(current_nutrition, sex, age) == True:
            remove_food(food, sex, age)
        else:
            continue
    return current_nutrition

