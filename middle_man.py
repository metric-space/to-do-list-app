import g
import f
import sys # just for testing purpose, not for the module itself
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class manager:

	def __init__(self,db_avatar_obj,gui_obj):
		self.db_obj = db_avatar_obj
		self.gui = gui_obj
		self.inner_list = self.db_special() 
		self.gui.populate(list=self.inner_list)

	def update_call(self):
		
		stuff = self.gui.generate_content()
		print "manager debug : %s " %stuff
		for i,j in enumerate(self.inner_list):
			if j != stuff[i]:
				print "entered desired loop on %s %s " %(j,stuff[i])
				self.db_obj.update(i,stuff[i])

		if len(stuff)> len(self.inner_list):
			for i in range(len(self.inner_list),len (stuff)):
				self.db_obj.insert(stuff[i])
		self.inner_list = self.db_special()

	def db_special(self):
		temp =  self.db_obj.list_contents()
		stuff = []
		for i in temp:
			stuff.append(i[1])
		return stuff


if __name__ == '__main__':
	try:
		egg = f.file_stuff()
		egg2 = egg.hand_me_the_cursor()
		mario =f. database_avatar(egg2)



		app = QApplication(sys.argv)
		form = g.Form()

		nine = manager(mario,form)
		
		form.set_external_function(nine.update_call)

		form.show()
		app.exec_()
		
	
	finally:
		egg.delete_me()
