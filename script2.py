# working with sqlite3 database
import sqlite3

# function that creates table
def create_table():
	# connect to db
	conn = sqlite3.connect("lite.db")
	# create a cursor to read and write data
	cur = conn.cursor()
	cur.execute( "CREATE TABLE IF NOT EXISTS store ( item TEXT, quantity INTEGER, price REAL ) " )
	conn.commit()
	conn.close()

def insert( item, quantity, price ):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute( "INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price) )
	conn.commit()
	conn.close()

def view():
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute( "SELECT * FROM store" )
	rows = cur.fetchall()
	conn.close()
	return rows

def delete( item ):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute( "DELETE FROM store WHERE item=?", (item,) )
	conn.commit()
	conn.close()

def update( quantity, price, item ):
	conn = sqlite3.connect("lite.db")
	cur = conn.cursor()
	cur.execute( "UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item) )
	conn.commit()
	conn.close()

#insert( "Water Glass", 10, 14.1 )
#insert( "Coffee Cup", 10, 12 )
#delete( "Coffee Cup" )
#update(11, 14.9, "Coffee Cup")
print( view() )