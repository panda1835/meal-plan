from model import Model
from view import View
class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.mainloop()
        # self.view.main() 

    def save_user_info(self, user_info):
        info = {'nutrition_standard': "", 'height': 0, 'weight': 0, 'age': 0, 'meal_list': ["mom cooking", "anything"]}
        info['nutrition_standard'] = user_info["Nutrition"].nutrition_plan
        print(info)
        self.model.set_user_info(info)
        
    def save_user_defined_meal(self, user_defined_meal):
        pass