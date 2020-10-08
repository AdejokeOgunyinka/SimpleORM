# Show examples of how you would use ALL your implementations here
from src.authors import Authors
from src.books import Books

# create a new Authors instance
new_author = Authors()
# connect to the authors database table
new_author.connect()
# drop the table if it already exists
Authors.cursor.execute("""DROP TABLE IF EXISTS authors""")
# create the table headers
new_author.create()
# insert values into the database from the authors csv file
print(new_author.insert())
# select all the values in the database
print(new_author.select())
# find an entry in the database based on the id
print(new_author.find(2))
# update the database based on the id provided
print(new_author.update(1, ['joe', 'tim', 'joetim', 'ds256787']))
# delete from the database based on id provided
print(new_author.delete(1))
new_author.cursor.close()
new_author.connection.close()

# create a new Books instance
new_books = Books()
# connect to the books database table
new_books.connect()
# drop the table if it already exists
Books.cursor.execute("""DROP TABLE IF EXISTS books""")
# create the table headers
new_books.create()
# insert values into the database from the authors csv file
print(new_books.insert())
# select all the values in the database
print(new_books.select())
# find an entry in the database based on the id
print(new_books.find(2))
# update the database based on the id provided
print(new_books.update(1, [3, 'Sense and Sensibility', 200]))
# delete from the database based on id provided
print(new_books.delete(1))
new_books.cursor.close()
new_books.connection.close()
# Show examples of how you would use ALL your implementations here
