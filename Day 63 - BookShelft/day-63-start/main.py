import sqlite3

# TODO 1: create the database
db = sqlite3.connect("books-collection.db")

# TODO 2: create a mouse or pointer to modify the database
cursor = db.cursor()

# TODO 3: create the table
'''
cursor.execute("CREATE TABLE books ("
               "id INTEGER PRIMARY KEY, "
               "title VARCHAR(250) NOT NULL UNIQUE, "
               "author VARCHAR(250) NOT NULL, "
               "rating FLOAT NOT NULL)")
'''

# TODO 4: download the viewer database in this link: https://sqlitebrowser.org/dl/
# to see the database created we need to download a viewer

# TODO 5: inserting values into the table
cursor.execute("INSERT INTO books VALUES (1, 'Harry Potter', 'J.K Rowling', '9.3')")

# TODO 6: commit the changes to the database
db.commit()
