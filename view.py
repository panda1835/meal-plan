import tkinter as tk
from tkinter import ttk

TITLEFONT = ("Time New Roman", 15)
class View(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self):
        
        # __init__ function for class Tk
        tk.Tk.__init__(self)
        self.geometry("500x300")
        self.state("zoomed")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # creating a container
        container = tk.Frame(self)
        container.grid(column = 0, row = 0)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (create_nutrition_plan, create_body_condition, create_plan_period):

            frame = F(container, self)

            # initializing frame of that object from
            # create_nutrition_plan, create_body_condition, #create_plan_period respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(create_nutrition_plan)

        

    # to display the current frame passed as
    # parameter
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class create_nutrition_plan(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = "white")

        # title of the frame
        title = tk.Label(parent, text = "Nutrition Plan Standard ", 
        font = TITLEFONT, bg = "white")

        # the combobox
        valuelist = [1,2,3]
        nutrition_plan = tk.StringVar()
        combo_box = ttk.Combobox(parent, width = 15, values = valuelist, 
        textvariable = nutrition_plan)
        combo_box.current(1)
        
        # the back & next buttons
        back_but = tk.Button(parent, text = "Back", bg = "Green", relief = "flat")
        next_but = tk.Button(parent, text ="Next", bg = "Green", relief = "flat", 
        command = lambda : controller.show_frame(create_body_condition))
        
        # make all elements visible by using grid
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, columnspan = 3, pady = 10, ipadx = 0)
        combo_box.grid (column = 1, row = 2, pady = 30)
        back_but.grid(column = 0, row = 3, padx = 15, pady = 10)
        next_but.grid(column = 2, row = 3, padx = 15, pady = 10)


class create_body_condition(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = "white")

        #title of the frame
        title = tk.Label(parent,text = "Your body condition", font = TITLEFONT, 
        bg = "white")

        # the height-weight-age titles and entries
        height = tk.Label(parent, text = "Height", bg = "white")
        height_entry = ttk.Entry(parent, width = 10)
        weight = tk.Label(parent, text = "Weight", bg = "white")
        weight_entry = ttk.Entry(parent, width = 10)
        age = tk.Label(parent, text = "Age", bg = "white")
        age_entry = ttk.Entry(parent, width = 10)

        #the back & next buttons
        back_but = tk.Button(parent, text = "Back", bg = "Green", relief = "flat", 
        command = lambda : controller.show_frame(create_nutrition_plan))
        next_but = tk.Button(parent, text ="Next", bg = "Green", relief = "flat", 
        command = lambda : controller.show_frame(create_plan_period))

        # make all elements visible by using grid
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, columnspan = 3, pady = 10)
        height.grid(column = 0, row = 1, padx = 5, pady = 5)
        height_entry.grid(column = 0, row = 2, padx = 10, pady = 10)
        age.grid(column = 1, row = 1, padx = 10, pady = 10)
        age_entry.grid(column = 1, row = 2, padx = 10, pady = 10)
        weight.grid(column = 2, row = 1, padx = 10, pady = 10)
        weight_entry.grid(column = 2, row = 2, padx = 10, pady = 10)
        back_but.grid(column = 0, row = 3, padx = 10, pady = 10)
        next_but.grid(column = 2, row = 3, padx = 10, pady = 10)

class create_plan_period(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = "white")

        # the title of the frame
        title = tk.Label(parent,text = "Set plan period", font = TITLEFONT, 
        bg = "white")

        # the combobox
        valuelist = ["Weekly"]
        plan_period = tk.StringVar()
        combo_box = ttk.Combobox(parent, width = 15, values = valuelist, 
        textvariable = plan_period)
        combo_box.current(0)

        #the back & next buttons
        back_but = tk.Button(parent, text = "Back", bg = "Green", relief = "flat", 
        command = lambda : controller.show_frame(create_body_condition))
        next_but = tk.Button(parent, text ="Next", bg = "Green", relief = "flat")
        
        # make all elements visible by using grid
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, columnspan = 3, pady = 10)
        combo_box.grid (column = 1, row = 2, pady = 30)
        back_but.grid(column = 0, row = 3, padx = 15, pady = 10)
        next_but.grid(column = 2, row = 3, padx = 15, pady = 10)



view = View()
view.mainloop()

