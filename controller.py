from model import Model
from view import View
class Controller:
    def __init__(self):
        # self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.mainloop()
        # self.view.main() 

    def save_user_info(self, user_info):
        info = {'nutrition_standard': "", 'height': 0, 'weight': 0, 'age': 0,'plan_period': "weekly"}
        info['nutrition_standard'] = user_info["Nutrition"].nutrition_plan.get()
        info['height'] = user_info["Body"].height_info.get()
        info['weight'] = user_info["Body"].weight_info.get()
        info['age'] = user_info["Body"].age_info.get()
        info['plan_period]'] = user_info["Plan"].plan_period.get()
        Model.set_user_info(info)
        
    def get_user_defined_meal(self, user_defined_meal):
        return Model.get_user_info()

    def save_user_defined_meal(self, user_defined_meal):
        defined_meal = {}
        for meal in user_defined_meal:
            defined_meal['meal_name'] = [meal.name]
            defined_meal['time'] = [meal.name]
            defined_meal['set_of_dishes'] = [meal.name]
            defined_meal['nutritious_restriction'] = [meal.name]
            defined_meal['regular'] = [meal.name]
            defined_meal['flexible'] = [meal.name]