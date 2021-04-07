from model import Model
from view import View

class Controller:

	def __init__(self):
		'''
		Constructor 
		'''
		self.model = Model()
		self.view = View(self)

	def main(self):
		self.view.mainloop() 
