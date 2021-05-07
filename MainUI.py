"""
This class creates the main UI which user see first when open the application
"""
import tkinter as tk
from tkinter import ttk
TITLEFONT = ("Time New Roman", 15)
from CurrentPlan import CurrentPlan
from NewPlan import NewPlan
from Recipe import Recipe
from Setting import Setting
from PrecookedDish import PrecookedDish

class MainUI(tk.Frame):  
    def __init__(self, parent, main_view):
        tk.Frame.__init__(self, parent)
        # parent = tk.Frame(self, bg = "white")
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)

        option = tk.Frame(self, borderwidth = 1, bg = 'green')
        option.grid(column = 1, row = 0)

        taskbar = tk.Frame(self, borderwidth = 1, bg = 'green')
        taskbar.grid(column = 0, row = 1)

        placeholder = tk.Frame(self, borderwidth = 5, bg = 'green')
        placeholder.grid(column = 0, row = 0)

        content = tk.Frame(self, borderwidth = 1, bg = 'green')
        content.grid(column = 1, row = 1)


        # Taskbar
        current_plan_btn = tk.Button(taskbar, text ="Current Plan", bg = "white", relief = "flat",
        command = lambda:self.show_frame(self.frame_CurrentPlan))
        new_plan_btn = tk.Button(taskbar, text ="New Plan", bg = "white", relief = "flat",
        command = lambda:self.show_frame(self.frame_NewPlan))
        recipe_btn = tk.Button(taskbar, text ="Recipe List", bg = "white", relief = "flat",
        command = lambda:self.show_frame(self.frame_Recipe))
        precooked_btn = tk.Button(taskbar, text ="Precooked dishes", bg = "white", relief = "flat",
        command = lambda:self.show_frame(self.frame_PrecookedDish))
        setting_btn = tk.Button(taskbar, text ="Settings", bg = "white", relief = "flat",
        command = lambda:self.show_frame(self.frame_Setting))

        # # Option
        # current_plan_btn_option = tk.Button(option, text ="Current Plan Option", bg = "white", relief = "flat")
        # new_plan_btn_option = tk.Button(option, text ="New Plan Option", bg = "white", relief = "flat")
        # current_plan_btn_option.pack(side = 'left')
        # new_plan_btn_option.pack(side = 'left')
        # current_plan_btn_option1 = tk.Button(option, text ="Current Plan Option", bg = "white", relief = "flat")
        # new_plan_btn_option1 = tk.Button(option, text ="New Plan Option", bg = "white", relief = "flat")
        # current_plan_btn_option1.pack(side = 'left')
        # new_plan_btn_option1.pack(side = 'left')

        # # Content
        # current_plan_btn_content = tk.Button(content, text ="Current Plan Option", bg = "white", relief = "flat")
        # new_plan_btn_content = tk.Button(content, text ="New Plan Option", bg = "white", relief = "flat")
        # current_plan_btn_content.pack(side = 'left')
        # new_plan_btn_content.pack(side = 'left')
        
        current_plan_btn.pack(fill="x")
        new_plan_btn.pack(fill="x")
        recipe_btn.pack(fill="x")
        precooked_btn.pack(fill="x")
        setting_btn.pack(fill="x")

        self.frame_NewPlan = NewPlan(content, option, self, main_view.controller)
        self.frame_NewPlan.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_NewPlan.columnconfigure(0, weight=1)
        self.frame_NewPlan.rowconfigure(0, weight=1)

        self.frame_Recipe = Recipe(content, option, self, main_view.controller)
        self.frame_Recipe.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_Recipe.columnconfigure(0, weight=1)
        self.frame_Recipe.rowconfigure(0, weight=1)

        self.frame_PrecookedDish = PrecookedDish(content, option, self, main_view.controller)
        self.frame_PrecookedDish.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_PrecookedDish.columnconfigure(0, weight=1)
        self.frame_PrecookedDish.rowconfigure(0, weight=1)

        self.frame_Setting = Setting(content, option, self, main_view.controller)
        self.frame_Setting.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_Setting.columnconfigure(0, weight=1)
        self.frame_Setting.rowconfigure(0, weight=1)
    
        self.frame_CurrentPlan = CurrentPlan(content, option, self, main_view.controller)
        self.frame_CurrentPlan.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_CurrentPlan.columnconfigure(0, weight=1)
        self.frame_CurrentPlan.rowconfigure(0, weight=1)

    def show_frame(self, current_frame):
        current_frame.tkraise()