
# Python to-do-app

#### Purpose and details

This is a Python app that serves as a simple to-do-list.

1. One can add entries via the UI
2. One can edit entries 


This app is an exercise for yours truly to improve my code writing and my software engineering skills. Also this also served as
a starting point for using software I develop so as to increase self reliance and to understand what the user goes through so that
I can better my understanding of UI and user-centered application functionality.

Backend  : Sqlite3 ( Reason for choosing : none of that initiate a server first bullshit )

Frontend : PyQT4 ( no real reason for choosing this GUI framework(library?))



#### Future Functionality and things to be added/done

1. Multi-list functionality
2. Better looking and advanced UI
3. Delete entries
4. Cleaner and commented code
5. Detailed Wiki
6. Advanced Tests
7. Add abstract classes


### Work done so far

```
     ________________________________________
    |                                        |
    |   class Name  :file_stuff              |-----> database cursor
    |                                        |                   |
    |   Responsibilities: file lookup        |                   |
    |                     database creation  |                   |
    |                     directory change   |                   |
    |                     database commit    |                   |
    |                     database closing   |                   |
    |_______________________________________ |                   |
                                                                 |
                                                                 |
            ______________________________________               |
           |                                     |    init       |   
           |  class Name: database_avatar        |<-------------- 
           |                                     |
           |   Responsibilities: create tables   |
           |                     insert entry    |<--(id,entry)-----------|
       |---|                     update entry    |<--(id,entry)-----------|
       |   |                     delete entry    |                        |
       |   |                     list tables     |                        |
       |   |                     list entries    |--->list of tuples----| |
       |   |_____________________________________|                      | |
       |                                                                | |
       |                                                                | |
       |   _______________________________________                      | |
       |   |                                     |                      | |
       |   |  class Name: Form                   |                      | |
       |   |                                     |                      | |
       |---|  Responsibilities: UI creation      |                      | |
       |   |                    onscreen update  |                      | |
       |   |       display db contents on screen |                      | |
       |   |             provide an updated list |--->dictionary--|     | |
       |   |                        event driver |                |     | |
       |   |_____________________________________|                |     | |
 init  |                                                          |     | |
       V                                                          |     | |
   _________________________________________________              |     | |
  |                                                 |             |     | |
  |    class Name: manager                          |             |     | |
  |                                                 |             |     | |
  |  Responsibilies:                                |             |     | |
  |        convert db contents into comparable form |-------------|-----  |              
  |        provide event for db update/insert       |-------------|-------|
  |                                                 |
  |_________________________________________________|

 
```                     
					                              






