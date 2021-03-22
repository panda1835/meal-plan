import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
	def __init__(self, controller):
		'''
		Constructor 
		'''
		super().__init__() # call init of tk.Tk parents
		self.controller = controller 
		

	def main(self):
		self.mainloop()

	def _create_components(self):
		'''
		Put the elements here
		'''
		pass
