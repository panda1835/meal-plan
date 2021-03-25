import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    def __init__(self):
        '''
        Constructor 
        '''
        super().__init__() # call init of tk.Tk parents
        #self.controller = controller
        self.geometry("500x300")
        self.create_nutrition_plan()
        

    def main(self):
        self.mainloop()
    
    def create_body_condition(self):
        '''
        Put the element here
        '''
        parent = tk.Frame(self)
        title = tk.Label(parent,text = "Your body condition")

        height = tk.Label(parent, text = "Height")
        height_entry = tk.Entry(parent)
      
        weight = tk.Label(parent, text = "Weight")
        weight_entry = tk.Entry(parent)
        
        age = tk.Label(parent, text = "Age")
        age_entry = tk.Entry(parent)

        
        height.grid(column = 0, row = 1, padx = 5, pady = 5)
        height_entry.grid(column = 0, row = 2, padx = 10, pady = 10)
        age.grid(column = 1, row = 1, padx = 10, pady = 10)
        age_entry.grid(column = 1, row = 2, padx = 10, pady = 10)
        weight.grid(column = 2, row = 1, padx = 10, pady = 10)
        weight_entry.grid(column = 2, row = 2, padx = 10, pady = 10)
        back_but = tk.Button(parent, text = "Back", bg = "Green", command = self.create_nutrition_plan)
        next_but = tk.Button(parent, text ="Next", bg = "Green")
        
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, pady = 10)
        back_but.grid(column = 0, row = 3, padx = 10, pady = 10)
        next_but.grid(column = 2, row = 3, padx = 10, pady = 10)

    def create_nutrition_plan(self):
        '''
        Put the elements here
        '''
        parent = tk.Frame(self)
        title = tk.Label(parent,text = "Nutrition Plan Standard ")
        valuelist = [1,2,3]
        nutrition_plan = tk.StringVar()
        combo_box = ttk.Combobox(parent, values = valuelist, textvariable = nutrition_plan)
        combo_box.current(1)
        back_but = tk.Button(parent, text = "Back", bg = "Green")
        next_but = tk.Button(parent, text ="Next", bg = "Green", command = self.create_body_condition)
        
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, pady = 10)
        combo_box.grid (column = 1, row = 2, pady = 10)
        back_but.grid(column = 0, row = 3, padx = 10, pady = 10)
        next_but.grid(column = 2, row = 3, padx = 10, pady = 10)


#controller = Controller()
view = View()
view.main()

