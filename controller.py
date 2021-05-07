from model import Model
from view import View
class Controller:
    def __init__(self):
        self.view = View(self)

    def main(self):
        self.view.mainloop()

    def save_user_info(self, info):
        Model.set_user_info(info)
        
    def get_user_info(self):
        return Model.get_user_info()
        
    def get_user_defined_meal(self):
        return Model.get_user_defined_meal_names()

    def save_user_defined_meal(self, list_defined_meal):
        Model.set_user_defined_meal(list_defined_meal)

    def save_recipe(self, recipe_object):
        recipe = {}
        recipe['recipe_name'] = recipe_object.recipe_name
        recipe['serving_size'] = recipe_object.serving_size
        recipe['cooking_time'] = recipe_object.cooking_time
        recipe['tag'] = recipe_object.tag
        recipe['ingredients'] = recipe_object.ingredients
        recipe['nutritions'] = recipe_object.nutritions
        recipe['steps_taken'] = recipe_object.steps_taken
        Model.set_recipe(recipe)