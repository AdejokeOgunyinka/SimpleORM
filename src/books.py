import sqlite3
from src.csv_reader import CsvReader


class Books:
    """ This class contains several functions that can be performed on an books database,
    such as connect, create etc."""
    connection = sqlite3.connect('projectdb.sqlite')
    cursor = connection.cursor()

    def connect(self):
        # Connects to the database
        try:
            self.connection

        except Exception as error:
            print(error)

    def create(self):
        # Creates `books` table, making the headers
        # in `books.csv` file the fields of the table
        file = CsvReader.read_csv('./data/books.csv')
        headers = file[0]

        self.cursor.execute(f"""CREATE TABLE books ({headers[0]} integer primary key, {headers[1]} integer, {headers[2]} text,
                            {headers[3]} integer)""")

    def insert(self):
        # Inserts all data rows in `books.csv` file into
        # the `books` table created
        with self.connection:
            file = CsvReader.read_csv('./data/books.csv')
            values = file[1:]

            for row in values:
                self.cursor.execute("""INSERT INTO books (id,author_id,title,page_count) VALUES (?,?,?,?)""",
                                    (row[0], row[1], row[2], row[3]))

    def select(self):
        # Select all rows from the `books` table
        return self.cursor.execute("""SELECT * FROM books""").fetchall()

    def find(self, id):
        # Select a row with id supplied from the `books` table
        return self.cursor.execute(f"""SELECT * FROM books WHERE id = {id}""").fetchall()

    def update(self, id, params):
        # Update a row with id supplied in the `books` table with
        # data provided as `params`
        with self.connection:
            self.cursor.execute(f"""UPDATE books
                                SET author_id= ?,title= ?, page_count= ?
                                WHERE id = {id}""", (params[0], params[1], params[2]))

    def delete(self, id):
        # Delete the row with id supplied from the `books` table
        with self.connection:
            self.cursor.execute(f"""DELETE FROM books WHERE id = {id}""")
