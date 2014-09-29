import os 
import os.path
import sqlite3

class file_stuff(object):

	name = 'to-do-list'

	def __init__(self):
		# -- move to home directory
		egg = os.path.expanduser('~')
		os.chdir(egg)

		#check to see if a specific duirectory exits if not create one and create a new databse inside

		
		if not os.path.exists(self.name):
			os.mkdir(self.name)
			os.chdir(self.name)
		else:
			os.chdir(self.name)

		# other class attributes
		self.db_stuff = None
		self.cur = None

	def hand_me_the_cursor(self):
		self.db_stuff = sqlite3.connect('%s.db' %self.name) 
		self.cur = self.db_stuff.cursor()
		return self.cur

	def delete_me(self):
		if self.db_stuff:
			self.db_stuff.close()

		print " I am sooo coooooooold ....-sad piano music plays-"
	


class database_avatar(object):

	schema = "create table  %s (id integer primary key autoincrement,note text) "

	def __init__(self,cursor,table_name = None):
		self.cursor = cursor
		self.table = table_name

	def list_tables(self):
		self.cursor.execute(" select name from sqlite_master where type=\'table\' ")
		temp = self.cursor.fetchall()
		if temp == []:
			self.cursor.execute(self.schema %"first")
			self.cursor.execute(" select name from sqlite_master where type=\'table\' ")		
			temp = self.cursor.fetchall()
		return temp	



if __name__ == '__main__':

	egg = file_stuff()
	egg2 = egg.hand_me_the_cursor()

	mario = database_avatar(egg2)
	print mario.list_tables()
	egg.delete_me()

