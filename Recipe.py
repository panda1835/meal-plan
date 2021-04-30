import tkinter as tk
from tkinter import ttk
TITLEFONT = ("Time New Roman", 15)

class Recipe(tk.Frame):
    def __init__(self, content, parent, main_view):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = 'white')
        parent.grid(column = 0, row = 0)

        self.frame_Ours = FrameOurRecipeForYou(content)
        self.frame_Yours = FrameYourRecipe(content)
        self.frame_Create = FrameCreateYourRecipe(content)

        self.show_frame(self.frame_Ours)

        # current_plan_btn_content = tk.Button(content, text ="Current Plan Option", bg = "white", relief = "flat")
        # new_plan_btn_content = tk.Button(content, text ="New Plan Option", bg = "white", relief = "flat")
        # current_plan_btn_content.pack(side = 'left')
        # new_plan_btn_content.pack(side = 'left')



        ours_btn = tk.Button(parent, text = "Our Recipe for you", bg = "white", relief = "flat",
        command = lambda:self.show_frame(self.frame_Ours))
        ours_btn.pack(side  = "left")
        
        yours_btn = tk.Button(parent, text = "Your Recipe", bg = "white", relief = "flat",
        command = lambda:self.show_frame(self.frame_Yours))
        yours_btn.pack(side  = "left")
        
        create_btn = tk.Button(parent, text = "Create your own Recipe", bg = "white", relief = "flat",
        command = lambda:self.show_frame(self.frame_Create))
        create_btn.pack(side  = "left")

    def show_frame(self, current_frame):
        current_frame.tkraise()

class FrameOurRecipeForYou(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = 'white')
        parent.grid(column = 0, row = 0)
        
        title = tk.Label(parent, text = "Our recipe for you")  
        title.grid(column = 0, row = 1)      


class FrameYourRecipe(tk.Frame):
    def __init__(self, parent):
        print("yours")

        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = 'white')
        parent.grid(column = 0, row = 0)
        
        title = tk.Label(parent, text = "Our recipe for you")  
        title.pack()    

class FrameCreateYourRecipe(tk.Frame):
    def __init__(self, parent):
        print("create")

        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = 'white')
        parent.grid(column = 0, row = 0) 
        
        # recipe_label = tk.Label(parent, text = "Name of dish", padyx=5, pady=5, justify ="left")
        # recipe = tk.StringVar()
        # recipe_entry = ttk.Entry(parent, textvariable = recipe)

        # serving_size_label = tk.Label(parent, text = "Serving size", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        # serving_size = tk.IntVar()
        # serving_size_entry = ttk.Entry(parent, textvariable = serving_size)

        # cooking_time_label = tk.Label(parent, text = "Cooking time", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        # cooking_time = tk.IntVar()
        # cooking_time_entry = ttk.Entry(parent, textvariable = cooking_time)

        # tag_label = tk.Label(parent, text = "Tag", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        # #valuelist = [CreateSubUserDefinedMeal(name)]
        # tag = tk.StringVar()
        # valuelist = [1,2,3]
        # tag_combo = ttk.Combobox(parent, width = 5, values = valuelist, textvariable = tag)

        # ingredient_label = tk.Label(parent, text = "Ingredients", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        # # add
        # # name_entry = ttk.Entry(parent)

        # steps_taken_label = tk.Label(parent, text = "Ingredients", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        # steps_taken = tk.StringVar()
        # steps_taken_entry = ttk.Entry(parent, textvariable = steps_taken)

        # recipe_label.grid(column=0, row=0)
        # recipe_entry.grid(column=1, row=0)
        # serving_size_label.grid(column=0, row=1)
        # serving_size_entry.grid(column=1, row=1)
        # cooking_time_label.grid(column=0, row=2)
        # cooking_time_entry.grid(column=1, row=2)
        # tag_label.grid(column=0, row=3)
        # tag_combo.grid(column=1, row=3)
        # ingredient_label.grid(column=0, row=4)
        # steps_taken_label.grid(column=0, row=5)
        # steps_taken_entry.grid(column=1, row=5) 