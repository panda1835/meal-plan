import tkinter as tk
from tkinter import ttk
from NutritionPlan import NutritionPlan
from BodyCondition import BodyCondition
from PlanPeriod import PlanPeriod
from UserDefinedMeal import UserDefinedMeal
from MainUI import MainUI
# from CurrentPlan import CurrentPlan
# from NewPlan import NewPlan 
# from Recipe import Recipe
# from PrecookedDish import PrecookedDish
# from Setting import Setting


TITLEFONT = ("Time New Roman", 15)
class View(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, controller):
        
        self.controller = controller

        # __init__ function for class Tk
        tk.Tk.__init__(self)
        self.minsize(600,400)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # creating a container
        container = tk.Frame(self)
        container.grid(column = 0, row = 0)

        self.user_info = {}
        self.user_defined_meal = []

        # iterating through a tuple consisting
        # of the different page layouts

        self.frame_NutritionPlan = NutritionPlan(container, self)
        self.frame_NutritionPlan.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_NutritionPlan.columnconfigure(0, weight=1)
        self.frame_NutritionPlan.rowconfigure(0, weight=1)

        self.frame_BodyCondition = BodyCondition(container, self)
        self.frame_BodyCondition.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_BodyCondition.columnconfigure(0, weight=1)
        self.frame_BodyCondition.rowconfigure(0, weight=1)
        
        self.frame_UserDefinedMeal = UserDefinedMeal(container, self)
        self.frame_UserDefinedMeal.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_UserDefinedMeal.columnconfigure(0, weight=1)
        self.frame_UserDefinedMeal.rowconfigure(0, weight=1)

        self.frame_PlanPeriod = PlanPeriod(container, self)   
        self.frame_PlanPeriod.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_PlanPeriod.columnconfigure(0, weight=1)
        self.frame_PlanPeriod.rowconfigure(0, weight=1)

        # self.frame_Recipe = Recipe(container,self)
        # self.frame_Recipe.grid(row = 0, column = 0, sticky = "nsew")
        # self.frame_Recipe.columnconfigure(0, weight=1)
        # self.frame_Recipe.rowconfigure(0, weight=1)

        self.user_info["Body"] = self.frame_BodyCondition
        self.user_info["Nutrition"] = self.frame_NutritionPlan
        self.user_info["Plan"] = self.frame_PlanPeriod
        
        self.show_frame(self.frame_NutritionPlan)

        self.frame_MainUI = MainUI(container, self)
        self.frame_MainUI.grid(row = 0, column = 0, sticky = "nsew")

        # self.frame_CurrentPlan = CurrentPlan(container, self)
        # self.frame_CurrentPlan.grid(row = 0, column = 0, sticky = "nsew")

        # self.frame_NewPlan = NewPlan(container, self)
        # self.frame_NewPlan.grid(row = 0, column = 0, sticky = "nsew")

        # self.frame_Recipe = Recipe(container, self)
        # self.frame_Recipe.grid(row = 0, column = 0, sticky = "nsew")
        
        # self.frame_PrecookedDish = PrecookedDish(container, self)
        # self.frame_PrecookedDish.grid(row = 0, column = 0, sticky = "nsew")

        # self.frame_Setting = Setting(container, self)
        # self.frame_Setting.grid(row = 0, column = 0, sticky = "nsew")


    def show_frame(self, current_frame):
        current_frame.tkraise()





        

