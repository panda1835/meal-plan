from model import Model

def create():
    user_info = {'nutrition_standard': "fat", 'height': 170, 'weight': 37,
                'age': 26, 'meal_list': ["dad cooking", "anything"]}

    user_defined_meal = {'meal_name': "morning", 'time': [18,00,20,00],
                        'set_of_dishes': ["chicken soup", "beef rice"],
                        'nutritious_restriction': "idk?", 'regular': False,
                        'flexible': True}

    recipe = {'recipe_name': "chicken soup", 'serving_size': 1,
                'cooking_time': 1, 'tag': "fast food",
                'ingredients': ("chicken", 1.0),
                'nutritions': ("calories", 3.0),
                'steps_taken': "take two steps"}
    
    
    Model.set_user_info(user_info)
    Model.set_user_defined_meal(user_defined_meal)
    Model.set_recipe(recipe)

def test():
    print("__User information__")
    print(Model.get_user_info(), "\n")
    print("__User defined meal__")
    print(Model.get_user_defined_meal_names(), "\n")
    print("__Recipe__")
    print(Model.get_recipe("chicken soup"))

def deleteRecipe():
    Model.cursor.execute("DROP TABLE Recipe")

if __name__ == '__main__':
    create()
    test()