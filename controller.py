from model import Model
from view import View
class Controller:
    def __init__(self):
        self.view = View(self)

    def main(self):
        self.view.mainloop()

    def save_user_info(self, user_info):
        info = {'nutrition_standard': "", 'height': 0, 'weight': 0, 'age': 0,'plan_period': "weekly"}
        info['nutrition_standard'] = user_info["Nutrition"].nutrition_plan.get()
        info['height'] = user_info["Body"].height_info.get()
        info['weight'] = user_info["Body"].weight_info.get()
        info['age'] = user_info["Body"].age_info.get()
        info['plan_period]'] = user_info["Plan"].plan_period.get()
        Model.set_user_info(info)
        
    def get_user_info(self):
        return Model.get_user_info()
        
    def get_user_defined_meal(self):
        return Model.get_user_defined_meal_names()

    def save_user_defined_meal(self, user_defined_meal):
        list_defined_meal = []
        for meal in user_defined_meal:
            defined_meal = {}
            defined_meal['meal_name'] = meal.name.get()
            defined_meal['start_time'] = meal.start_time.get()
            defined_meal['end_time'] = meal.end_time.get()
            defined_meal['set_of_dishes'] = meal.set_of_dishes.get()
            defined_meal['nutritious_restriction'] = meal.nutritious_restriction.get()
            defined_meal['regular'] = meal.reg.get()
            defined_meal['flexible'] = meal.flex.get()
            list_defined_meal.append(defined_meal)
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