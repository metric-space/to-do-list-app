import sqlite3

// did you really expect a ORM? haha jokes on you motherfucker

def getCursor(path):
    #check to see if path exists
    connection = connect(path)
    return connection.cursor

def makeTable(cursor,schema):

class databaseObject(object):

    schema = "create table  %s (id integer primary key ,note text) "

	def __init__(self,path):
                connection  = connect(path) 
                self.cursor =  
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

