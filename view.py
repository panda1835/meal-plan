import tkinter as tk
from tkinter import ttk
from NutritionPlan import NutritionPlan
from BodyCondition import BodyCondition
from PlanPeriod import PlanPeriod
from UserDefinedMeal import UserDefinedMeal
TITLEFONT = ("Time New Roman", 15)
class View(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, controller):
        
        self.controller = controller

        # __init__ function for class Tk
        tk.Tk.__init__(self)
        self.geometry("500x300")
        self.state("zoomed")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # creating a container
        container = tk.Frame(self)
        container.grid(column = 0, row = 0)

        self.user_info = {}
        self.user_defined_meal = []

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts

        self.frame_NutritionPlan = NutritionPlan(container, self)
        self.frame_NutritionPlan.grid(row = 0, column = 0, sticky ="nsew")
        

        self.frame_BodyCondition = BodyCondition(container, self)
        self.frame_BodyCondition.grid(row = 0, column = 0, sticky ="nsew")
        
        self.frame_UserDefinedMeal = UserDefinedMeal(container, self)
        self.frame_UserDefinedMeal.grid(row = 0, column = 0, sticky ="nsew")

        self.frame_PlanPeriod = PlanPeriod(container, self)   
        self.frame_PlanPeriod.grid(row = 0, column = 0, sticky ="nsew")

        self.user_info["Body"] = self.frame_BodyCondition
        self.user_info["Nutrition"] = self.frame_NutritionPlan
        self.user_info["Plan"] = self.frame_PlanPeriod
        
        self.show_frame(self.frame_NutritionPlan)

    def show_frame(self, current_frame):
        current_frame.tkraise()





        

