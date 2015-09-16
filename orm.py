import sqlite3 as db 
import operator

# What does this do?
# 1. thin abstraction over commonly used commands to be used by py-sqlite
# 2. this small library encompasses 'the DB primitives'
 
tableLevelCommands = {
        'createTable'    :  { 'command' : "create table {table}(id integer primary key,note text)",'argsLen':1 } , 
        'deleteTable'    :  { 'command' : "drop table if exists {table}"                          ,'argsLen':1},
        'renameTable'    :  { 'command' : "alter table {old_name} rename to {new_name}"           ,'argsLen':2},
  }


commandDictionary = {
        'listTables'       : { 'command' : "SELECT name FROM sqlite_master where type='table'"   , 'argsLen':0 } ,
        'getTableContents' : { 'command' : "select * from {table}"                               , 'argsLen':1 } ,
        'deleteFromTable'  : { 'command' : "delete from {table} where id={id_number}"            , 'argsLen':2 } ,
        'insertIntoTable'  : { 'command' : "insert into {table} (note) values ({insertStuff})"   , 'argsLen':2 } ,
        'updateTableEntry' : { 'command' : "update {table} set note={text} where id={id_number}" , 'argsLen':3 },
}

listOfCommandDicts      = [commandDictionary, tableLevelCommands]
allowedCommands         = reduce(operator.concat,[x.keys() for x in listOfCommandDicts],[])
entireCommandDictionary = reduce(lambda x,y:x.update(y) or x,listOfCommandDicts,{})


def getCursor(path):
    #check to see if path exists
    connection = db.connect(path)
    return connection.cursor()

def execute(cursor,command,**kwargs):
    # limits what one can do with sqlite
    if command in allowedCommands:
        if len(kwargs.keys()) == entireCommandDictionary[command]['argsLen']:
            cursor.execute(entireCommandDictionary[command]['command'].format(**kwargs))
            return cursor.fetchall()
    return [] # should replace this with something more meaningful






