import tkinter as tk
from tkinter import ttk

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
        for F in (NutritionPlan, BodyCondition, PlanPeriod, UserDefinedMeal):

            frame = F(container, self)

            # initializing frame of that object from
            # NutritionPlan, BodyCondition, #PlanPeriod respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")
        
        self.user_info["Nutrition"] = self.frames[NutritionPlan]
        self.user_info["Body"] = self.frames[BodyCondition]
        self.user_info["Plan"] = self.frames[PlanPeriod]

        self.show_frame(NutritionPlan)

    # to display the current frame passed as
    # parameter
    
    def show_frame(self, current_frame):
        frame = self.frames[current_frame]
        frame.tkraise()





        

