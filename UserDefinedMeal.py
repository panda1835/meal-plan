"""
This class creates an interface for users to define their meals
"""
import tkinter as tk
from tkinter import ttk
TITLEFONT = ("Time New Roman", 15)

class UserDefinedMeal(tk.Frame):

    def __init__(self, parent, main_view):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = "white")

        container = ttk.Frame(parent)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)
        
        # the title of the frame
        title = tk.Label(parent,text = "Define your meals", font = TITLEFONT, bg = "white")
        addbtn = tk.Button(parent, text = "+", bg = "grey", command = lambda: self.add_sub_defined_meal(scrollable_frame, main_view))
        backbtn = tk.Button(parent, text = "Back", bg = "Green", relief = "flat",
        command = lambda: main_view.show_frame(main_view.frame_BodyCondition))
        nextbtn = tk.Button(parent, text ="Next", bg = "Green", relief = "flat",
        command = lambda: main_view.show_frame(main_view.frame_PlanPeriod))
        
        
        # make all elements visible by using grid
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, columnspan = 3, pady = 10)
        addbtn.grid(column = 2, row = 0)

        container.grid(column = 1, row = 1)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


        backbtn.grid(column = 0, row = 3, padx = 15, pady = 10)
        nextbtn.grid(column = 2, row = 3, padx = 15, pady = 10)


    def add_sub_defined_meal(self, scrollable_frame, main_view):
        new_meal = SubUserDefinedMeal(scrollable_frame, main_view)
        main_view.user_defined_meal.append(new_meal)
        new_meal.pack() 

class SubUserDefinedMeal(tk.Frame):

    def __init__(self, scrollable_frame, main_view):
        tk.Frame.__init__(self, scrollable_frame)
        parent = tk.Frame(self, bg = "white")
        #instantiate wireframe's components and position them within the frame

        self.name = tk.StringVar()
        self.start_time = tk.StringVar()
        self.end_time = tk.StringVar()
        self.set_of_dishes = tk.StringVar()
        self.nutritious_restriction = ''
        self.reg = tk.IntVar()
        self.flex = tk.IntVar()

        del_meal = tk.Button(parent, text = "-", bg ="white", command = lambda: self.delete_meal(main_view), relief = "flat")

        name_label = tk.Label(parent, text = "Name", bg ="white", anchor = "w", justify="left", pady=5, padx=5)
        name_entry = tk.Entry(parent, textvariable = self.name)

        time_label = tk.Label(parent, text = "Time", bg ="white")
        valuelist = ["05:00","05:15","05:30","05:45","06:00","06:15","06:30","06:45","07:00","07:15","07:30","07:45",
                     "08:00","08:15","08:30","08:45","09:00","09:15","09:30","09:45","10:00","10:15","10:30","10:45",
                     "11:00","11:15","11:30","11:45","12:00","12:15","12:30","12:45","13:00","13:15","13:30","13:45",
                     "14:00","14:15","14:30","14:45","15:00","15:15","15:30","15:45","16:00","16:15","16:30","16:45",
                     "17:00","17:15","17:30","17:45","18:00","18:15","18:30","18:45","19:00","19:15","19:30","19:45",
                     "20:00","20:15","20:30","20:45","21:00","21:15","21:30","21:45","22:00","22:15","22:30","22:45"]
        time_start_combo  = ttk.Combobox(parent, width = 5, values = valuelist, textvariable = self.start_time)
        time_end_combo    = ttk.Combobox(parent, width = 5, values = valuelist, textvariable = self.end_time)
        dash_label        = tk.Label(parent, text = "-")
        # time_start_combo.bind("<<ComboboxSelected>>", self.is_checked)
        # time_end_combo.bind("<<ComboboxSelected>>", self.is_checked)
        
        # if isinstance(self.start_time, str):
        #     print(self.start_time) 

        set_dish_label = tk.Label(parent, text = "Set of dishes", bg ="white")
        set_dish_entry = tk.Entry(parent, textvariable = self.set_of_dishes)
        
        nutri_label = tk.Label(parent, text = "Nutritional restriction", bg ="white")
        nutri_entry = tk.Entry(parent, textvariable = self.nutritious_restriction)
        
        #variable to keep track the checkbutton
        regular  = tk.Checkbutton(parent, text ="Regular", variable = self.reg, bg ="white")
        flexible = tk.Checkbutton(parent, text ="Flexible", variable = self.flex, bg ="white")
    
        # make all elements visible by using grid
        parent.grid(column = 0, row = 0)
        del_meal.grid(column = 4, row = 0, sticky = 'E')

        name_label.grid(column = 0, row = 1)
        name_entry.grid(column = 1, row = 1, columnspan = 3)

        time_label.grid(column = 0, row = 2)
        time_start_combo.grid(column = 1, row = 2)
        time_end_combo.grid(column = 3, row = 2)

        dash_label.grid(column = 2, row = 2)

        set_dish_label.grid (column = 0, row = 3)
        set_dish_entry.grid(column = 1, row = 3, columnspan = 3)

        nutri_label.grid(column = 0 , row = 4)
        nutri_entry.grid(column = 1, row = 4, columnspan = 3)

        regular.grid(column = 4, row = 2)
        flexible.grid(column = 4, row =3)

    def delete_meal(self, main_view):
        main_view.user_defined_meal.remove(self)
        self.destroy()

    def check_valid_time(self, start_time, end_time):
        '''
        check if start_time happens before end_time
        '''

        return True

