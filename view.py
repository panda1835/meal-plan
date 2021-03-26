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
        for F in (CreateNutritionPlan, CreateBodyCondition, CreatePlanPeriod, CreateUserDefinedMeal):

            frame = F(container, self)

            # initializing frame of that object from
            # CreateNutritionPlan, CreateBodyCondition, #CreatePlanPeriod respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(CreateNutritionPlan)

        

    # to display the current frame passed as
    # parameter
    
    def show_frame(self, current_frame):
        frame = self.frames[current_frame]
        frame.tkraise()

class CreateNutritionPlan(tk.Frame):
    '''
    
    '''
    def __init__(self, parent, main_view):
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
        
        # the back & next buttons
        back_but = tk.Button(parent, text = "Back", bg = "Green", relief = "flat")
        next_but = tk.Button(parent, text ="Next", bg = "Green", relief = "flat", 
        command = lambda : main_view.show_frame(CreateBodyCondition))
        
        # make all elements visible by using grid
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, columnspan = 3, pady = 10, ipadx = 0)
        combo_box.grid (column = 1, row = 2, pady = 30)
        back_but.grid(column = 0, row = 3, padx = 15, pady = 10)
        next_but.grid(column = 2, row = 3, padx = 15, pady = 10)


class CreateBodyCondition(tk.Frame):
    '''
    
    '''
    def __init__(self, parent, main_view):
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
        command = lambda : main_view.show_frame(CreateNutritionPlan))
        next_but = tk.Button(parent, text ="Next", bg = "Green", relief = "flat", 
        command = lambda : main_view.show_frame(CreatePlanPeriod))

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

class CreatePlanPeriod(tk.Frame):
    '''
    
    '''
    def __init__(self, parent, main_view):
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
        command = lambda : main_view.show_frame(CreateBodyCondition))
        next_but = tk.Button(parent, text ="Next", bg = "Green", relief = "flat", 
        command = lambda : main_view.show_frame(CreateUserDefinedMeal))
        
        # make all elements visible by using grid
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, columnspan = 3, pady = 10)
        combo_box.grid (column = 1, row = 2, pady = 30)
        back_but.grid(column = 0, row = 3, padx = 15, pady = 10)
        next_but.grid(column = 2, row = 3, padx = 15, pady = 10)

class CreateUserDefinedMeal(tk.Frame):

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

        # for i in range(50):
        #     ttk.Label(scrollable_frame, text="Sample scrolling label").pack()
        # main_view.frames[CreateSubUserDefinedMeal] = CreateSubUserDefinedMeal(scrollable_frame, main_view)
        CreateSubUserDefinedMeal(scrollable_frame, main_view).pack()
        CreateSubUserDefinedMeal(scrollable_frame, main_view).pack()
        CreateSubUserDefinedMeal(scrollable_frame, main_view).pack()
        CreateSubUserDefinedMeal(scrollable_frame, main_view).pack()
        # main_view.show_frame(CreateSubUserDefinedMeal)

        

        # the title of the frame
        title = tk.Label(parent,text = "Set plan period", font = TITLEFONT, bg = "white")
        back_but = tk.Button(parent, text = "Back", bg = "Green", relief = "flat")
        next_but = tk.Button(parent, text ="Next", bg = "Green", relief = "flat")
        
        # make all elements visible by using grid
        parent.grid(column = 0, row = 0)
        title.grid(column = 0, row = 0, columnspan = 3, pady = 10)

        container.grid(column = 1, row = 1)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


        back_but.grid(column = 0, row = 3, padx = 15, pady = 10)
        next_but.grid(column = 2, row = 3, padx = 15, pady = 10)

class CreateSubUserDefinedMeal(tk.Frame):

    def __init__(self, parent, main_view):
        tk.Frame.__init__(self, parent)
        parent = tk.Frame(self, bg = "white")
        #instantiate wireframe's components and position them within the frame
        del_meal          = tk.Button(parent, text = "-", bg ="grey")
        
        name_label        = tk.Label(parent, text = "Name", bg ="grey", anchor = "w", justify="left", pady=5, padx=5)
        name_entry        = tk.Entry(parent)
        
        time_label        = tk.Label(parent, text = "Time", bg ="grey")
        valuelist = ["05:00","05:15","05:30","05:45","06:00","06:15","06:30","06:45","07:00","07:15","07:30","07:45",
                     "08:00","08:15","08:30","08:45","09:00","09:15","09:30","09:45","10:00","10:15","10:30","10:45",
                     "11:0","11:15","11:30","11:45","12:0","12:15","12:30","12:45","13:0","13:15","13:30","13:45",
                     "14:0","14:15","14:30","14:45","15:0","15:15","15:30","15:45","16:0","16:15","16:30","16:45",
                     "17:0","17:15","17:30","17:45","18:0","18:15","18:30","18:45","19:0","19:15","19:30","19:45",
                     "20:0","20:15","20:30","20:45","21:0","21:15","21:30","21:45","22:0","22:15","22:30","22:45"]
        start_time   = tk.StringVar()
        end_time     = tk.StringVar()

        time_start_combo  = ttk.Combobox(parent, width = 15, values = valuelist, textvariable = start_time)
        time_end_combo    = ttk.Combobox(parent, width = 15, values = valuelist, textvariable = end_time)
        dash_label        = tk.Label(parent, text = "-")
        # time_start_combo.bind("<<ComboboxSelected>>", self.is_checked)
        # time_end_combo.bind("<<ComboboxSelected>>", self.is_checked)
        
        if isinstance(start_time, str):
            print(start_time) 

        set_dish_label    = tk.Label(parent, text = "Set of dishes", bg ="grey")
        set_dish_entry    = tk.Entry(parent)

        nutri_label       = tk.Label(parent, text = "Nutritional restriction", bg ="grey")
        nutri_entry       = tk.Entry(parent)
        
        #variable to keep track the checkbutton
        reg = tk.IntVar()
        flex = tk.IntVar()
        regular  = tk.Checkbutton(parent, text ="Regular", variable = reg, bg ="grey")
        flexible = tk.Checkbutton(parent, text ="Flexible", variable = flex, bg ="grey")
    
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

    def check_valid_time(self, start_time, end_time):
        '''
        check if start_time happens before end_time
        '''

        return True

    # def is_checked(self):
    #     print(start_time.get())
    #     print(type(start_time.get()))
    #     if (self.start_time.get() != '') and (self.end_time.get() != ''):
    #         if self.check_valid_time(start_time, end_time):
    #             print('hi')


    
view = View()
view.mainloop()

