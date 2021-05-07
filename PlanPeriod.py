"""
This class creates an interface for user to input the period for planning meal
"""
import tkinter as tk
from tkinter import ttk
TITLEFONT = ("Time New Roman", 15)

class PlanPeriod(tk.Frame):
    def __init__(self, parent, main_view):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = "white")
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)

        # the title of the frame
        title = tk.Label(parent,text = "Set plan period", font = TITLEFONT, 
        bg = "white")

        # the combobox
        valuelist = ["Weekly"]
        self.plan_period = tk.StringVar()
        combo_box = ttk.Combobox(parent, width = 15, values = valuelist, 
        textvariable = self.plan_period)
        combo_box.current(0)

        #the back & next buttons
        backbtn = tk.Button(parent, text = "Back", bg = "Green", relief = "flat", 
        command = lambda : main_view.show_frame(main_view.frame_UserDefinedMeal))
        savebtn = tk.Button(parent, text ="Save", bg = "Green", relief = "flat", 
        command = lambda : self.save_database(main_view))

        # make all elements visible by using grid
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, columnspan = 3, pady = 10)
        combo_box.grid (column = 1, row = 2, pady = 30)
        backbtn.grid(column = 0, row = 3, padx = 15, pady = 10)
        savebtn.grid(column = 2, row = 3, padx = 15, pady = 10)
    
    def save_database(self, main_view):
        info = {'nutrition_standard': "", 'height': 0, 'weight': 0, 'age': 0,'plan_period': "weekly"}
        info['nutrition_standard'] = main_view.user_info["Nutrition"].nutrition_plan.get()
        info['height'] = main_view.user_info["Body"].height_info.get()
        info['weight'] = main_view.user_info["Body"].weight_info.get()
        info['age'] = main_view.user_info["Body"].age_info.get()
        info['plan_period]'] = main_view.user_info["Plan"].plan_period.get()
        main_view.controller.save_user_info(info)
        
        list_defined_meal = []
        for meal in main_view.user_defined_meal:
            defined_meal = {}
            defined_meal['meal_name'] = meal.name.get()
            defined_meal['start_time'] = meal.start_time.get()
            defined_meal['end_time'] = meal.end_time.get()
            defined_meal['set_of_dishes'] = meal.set_of_dishes.get()
            defined_meal['nutritious_restriction'] = meal.nutritious_restriction.get()
            defined_meal['regular'] = meal.reg.get()
            defined_meal['flexible'] = meal.flex.get()
            list_defined_meal.append(defined_meal)
        main_view.controller.save_user_defined_meal(list_defined_meal)
        main_view.show_frame(main_view.frame_Recipe)
        main_view.show_frame(main_view.frame_MainUI)
