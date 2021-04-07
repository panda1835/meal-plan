from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.mainloop()

    def save_user_info(self, user_info):
        pass