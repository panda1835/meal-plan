import tkinter as tk
from tkinter import ttk
TITLEFONT = ("Time New Roman", 15)

class Setting(tk.Frame):
    def __init__(self, content, option, main_view, controller):
        tk.Frame.__init__(self, option)
        option = tk.Frame(self, bg = 'white')
        option.grid(column = 0, row = 0)

        self.frame_PersonalInfor = FramePersonalInfor(content, main_view, controller)
        self.frame_PersonalInfor.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_NutriInfor = FrameNutritionalInfor(content, main_view, controller)
        self.frame_NutriInfor.grid(row = 0, column = 0, sticky ="nsew")
        self.frame_MealInfor = FrameMealInfor(content, main_view, controller)
        self.frame_MealInfor.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(self.frame_PersonalInfor)

        personal_btn = tk.Button(option, text = "Personal info", bg = "white", relief = "flat",
        command = lambda:self.show_frame(self.frame_PersonalInfor))
        personal_btn.pack(side  = "left")
         
        nut_btn = tk.Button(option, text = "Nutritional info", bg = "white", relief = "flat", 
        command = lambda:self.show_frame(self.frame_NutriInfor))
        nut_btn.pack(side  = "left")
        
        meal_btn = tk.Button(option, text = "Meal info", bg = "white", relief = "flat",
        command = lambda:self.show_frame(self.frame_MealInfor))
        meal_btn.pack(side  = "left")

    def show_frame(self, current_frame):
        current_frame.tkraise()

class FramePersonalInfor(tk.Frame):
    def __init__(self, parent, main_view, controller):
        tk.Frame.__init__(self, parent)
        button = tk.Frame(self, parent)
        button.grid(column = 0, row = 1)

        parent = tk.Frame(self, bg = 'white')
        parent.grid(column = 0, row = 0)
           

        self.height_info = tk.IntVar()
        self.weight_info = tk.IntVar()
        self.age_info = tk.IntVar()
        
        # get values from database
        user_info = controller.get_user_info()

        height = tk.Label(parent, text = "Height", bg = "white")
        height_entry = ttk.Entry(parent, width = 10, textvariable = self.height_info)
        weight = tk.Label(parent, text = "Weight", bg = "white")
        weight_entry = ttk.Entry(parent, width = 10, textvariable = self.weight_info)
        age = tk.Label(parent, text = "Age", bg = "white")
        age_entry = ttk.Entry(parent, width = 10, textvariable = self.age_info)
        save_btn = ttk.Button(button, text = "Save",
        command = lambda:self.save_user_info(user_info, controller))

        
        height_entry.delete(0, "end")
        height_entry.insert(0, str(user_info[2]))
        age_entry.delete(0, "end")
        age_entry.insert(0, str(user_info[4]))
        weight_entry.delete(0, "end")
        weight_entry.insert(0, str(user_info[3]))

        height.grid(column = 0, row = 1, padx = 5, pady = 5)
        height_entry.grid(column = 0, row = 2, padx = 10, pady = 10)
        age.grid(column = 1, row = 1, padx = 10, pady = 10)
        age_entry.grid(column = 1, row = 2, padx = 10, pady = 10)
        weight.grid(column = 2, row = 1, padx = 10, pady = 10)
        weight_entry.grid(column = 2, row = 2, padx = 10, pady = 10)
        save_btn.grid(column = 0, row = 0)
    
    def save_user_info(self, old_info, controller):
        info = {}
        info['nutrition_standard'] = old_info[0]
        info['height'] = self.height_info.get()
        info['weight'] = self.weight_info.get()
        info['age'] = self.age_info.get()
        info['plan_period'] = old_info[5]
        controller.save_user_info(info)


class FrameNutritionalInfor(tk.Frame):
    def __init__(self, parent, main_view, controller):

        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = 'white')
        parent.grid(column = 0, row = 0)
        
        title = tk.Label(parent, text = "Approximate the amount of calories per day")  
        title.pack()    

class FrameMealInfor(tk.Frame):
    def __init__(self, parent, main_view, controller):

        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = 'white')
        parent.grid(column = 0, row = 0)
        
        title = tk.Label(parent, text = "Your defined meals")  
        title.pack()    