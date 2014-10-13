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
		for i in self.inner_list:
			if self.inner_list[i] != stuff[i]:
				print "entered desired loop on %s %s " %(self.inner_list[i],stuff[i])
				self.db_obj.update(i,stuff[i])

		# check for new members
		set_gui = set(stuff.keys())
		set_db = set(self.inner_list.keys())
	
		assert len(set_gui) >= len(set_db)
		for i in (set_gui - set_db):
			self.db_obj.insert(i,stuff[i])

		self.inner_list = self.db_special()


	def db_special(self):

		"""
			do i need this after refactoring ? we'll se
			
			I do need this because of the retarded format of the db_output
		"""

		temp =  self.db_obj.list_contents()
		stuff = {}
		for i in temp:
			stuff[i[0]]=i[1]
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
