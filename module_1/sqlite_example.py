# step 0 - import dqlite3
import sqlite3
import queries as q

# step 1 - connect to the database
 # triple-check the spelling of your database filename bc 
 # error will not be thrown if misspelled - instead, a new
 # db will be created
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2 - make the 'cursor' (a cursor is like a butler/teller)
cursor = connection.cursor()

# step 3 - write a query
# (see the queries.py file)

# step 4 - execute the query on the cursor and fetch results
# aka pulling the results from the cursor
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])