"""
This class creates the main UI which user see first when open the application
"""
import tkinter as tk
from tkinter import ttk
TITLEFONT = ("Time New Roman", 15)

class MainUI(tk.Frame):  
    def __init__(self, parent, main_view):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = "white")
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)

        taskbar = tk.Frame(parent)

        current_plan_btn = tk.Button(taskbar, text ="Current Plan", bg = "white", relief = "flat")
        
        new_plan_btn = tk.Button(taskbar, text ="New Plan", bg = "white", relief = "flat")
        
        recipe_btn = tk.Button(taskbar, text ="Recipe List", bg = "white", relief = "flat")
        
        precooked_btn = tk.Button(taskbar, text ="Precooked dishes", bg = "white", relief = "flat")
        
        setting_btn = tk.Button(taskbar, text ="Settings", bg = "white", relief = "flat")

        parent.grid(column = 0, row = 0)
        taskbar.pack(side="left")
        current_plan_btn.pack(fill="x")
        new_plan_btn.pack(fill="x")
        recipe_btn.pack(fill="x")
        precooked_btn.pack(fill="x")
        setting_btn.pack(fill="x")
         
# class TaskBar(tk.Frame):
#     def __init__(self,)
#         parent = tk.Frame(self, bg = "white", height = rootHeight - 20, width = rootWidth - 20)
        