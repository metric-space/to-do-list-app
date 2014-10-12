import os 
import os.path
import sqlite3

from shutil import rmtree

class file_stuff(object):

	name = 'to-do-list'

	def __init__(self,test_override=None):

		# ---- TEST MODE START ------------------------
		# --- this small part only applies for a test-mode
		if test_override:
			self.name = self.name+"-test"

		#~~~~~~~~~END OF TEST MODE ~~~~~~~~~~~~~~~~~~~~~~~


		# -- move to home directory
		egg = os.path.expanduser('~')
		os.chdir(egg)


		#check to see if a specific directory exits if not create one and create a new databse inside

		
		if not os.path.exists(self.name):
			os.mkdir(self.name)
			os.chdir(self.name)
		else:
			os.chdir(self.name)

		# other class attributes
		self.db_stuff = None
		self.cur = None

	def hand_me_the_cursor(self):
		'''      
			returns the cursor of the db(only single) 
		'''
		self.db_stuff = sqlite3.connect('%s.db' %self.name) 
		self.cur = self.db_stuff.cursor()
		return self.cur

	def delete_me(self):
		if self.db_stuff:
			self.db_stuff.commit()
			self.db_stuff.close()

		print " I am sooo coooooooold ....-sad piano music plays-"
	
	def clean_up(self):
		egg = os.path.expanduser('~')
		os.chdir(egg)
		rmtree(self.name)

class database_avatar(object):

	'''
			



	'''

	schema = "create table  %s (id integer primary key ,note text) "

	def __init__(self,cursor):
		self.cursor = cursor
		self.table = None
		if self.list_tables() == []:
			self.cursor.execute(self.schema %"first")
		temp = self.list_tables()
		self.select_table(temp[0][0])

	def list_tables(self):
		self.cursor.execute(" select name from sqlite_master where type=\'table\' ")
		temp = self.cursor.fetchall()
		return temp	

	def select_table(self,name):
		''' assuming the table exists '''
		self.table = name
		
	def create_new_table(self,name):
		self.cursor.execute(self.schema %name)

	def list_contents(self):
		self.cursor.execute("select * from %s " %self.table)
		return self.cursor.fetchall()
	
	def insert(self,id,what):
		self.cursor.execute("insert into %s (id,note) values (%d,\'%s\')" %(self.table,id,what))

	def update(self,id,what):
		try:
			self.cursor.execute("update %s set note=\'%s\' where id=%d" %(self.table,what,id))
		except:
			print "something went wrong with the update button"

	def delete(self,id):
		self.cursor.execute("delete from %s where id = %d" %(self.table,id))


if __name__ == '__main__':
	try:
		print " ---Start of test mode --- "
		egg = file_stuff(test_override='Yes')
		egg2 = egg.hand_me_the_cursor()

		mario = database_avatar(egg2)

		test_list = [(1,"idiots"),(2,"eat zombie brains"),(3,"get 100 cans of poop")]

		for i in test_list:
			mario.insert(i[0],i[1])
	
		print " db output : ",mario.list_contents()
		print " db input :  ",test_list,"\n\n"

		assert mario.list_contents() == test_list 

		mario.update(2,"buy chicken")
		
		test_list[1] =(2,"buy chicken")

		print " db output : ",mario.list_contents()
		print " db input :  ",test_list

		assert mario.list_contents() == test_list

		print "---end-of-test---- \n\n"

	finally:
		print "finishing up"
		egg.delete_me()
		egg.clean_up()
