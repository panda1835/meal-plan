from model import Model

def create():
    Model.set_user_info("fat", 170, 37, 26, ["mom cooking", "anything"])
    Model.set_user_defined_meal("morning", [18,00,20,00], ["chicken soup", "beef rice"],
                                "idk?", False, True)
    Model.set_recipe("chicken soup", 1, 1, "fast food", ("chicken", 1), ("calories", 1), "take two steps")

def test():
    print("__User information__")
    print(Model.get_user_info(), "\n")
    print("__User defined meal__")
    print(Model.get_user_defined_meal_names(), "\n")
    print("__Recipe__")
    print(Model.get_recipe("chicken soup"))

def deleteRecipe():
    Model.cursor.execute("DROP TABLE Recipe")

test()