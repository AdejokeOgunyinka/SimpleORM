import psycopg2
from src.csv_reader import CsvReader


class Authors:
    """ This class contains several functions that can be performed on an authors database, such as connect, create etc."""
    connection = psycopg2.connect(
        host='localhost',
        database='projectdb',
        user='Adejoke'
    )
    # This creates a cursor for the connection that can be accessible anywhere in the program file.
    cursor = connection.cursor()

    def connect(self):
        # Connects to the database
        try:
            self.connection

        except Exception as error:
            print(error)

    def create(self):
        # Creates `authors` table, making the headers
        # in `authors.csv` file the fields of the table

        file = CsvReader.read_csv('./data/authors.csv')
        headers = file[0]

        self.cursor.execute(f"""CREATE TABLE authors ({headers[0]} integer primary key, {headers[1]} text, 
                            {headers[2]} text,{headers[3]} text, {headers[4]} text)""")

    def insert(self):
        # Inserts all data rows in `authors.csv` file into
        # the `authors` table created
        with self.connection:
            file = CsvReader.read_csv('./data/authors.csv')
            values = file[1:]

            for row in values:
                self.cursor.execute("""INSERT INTO authors (id,username,firstname,lastname,password) VALUES 
                                    (%s,%s,%s,%s,%s)""", (row[0], row[1], row[2], row[3], row[4]))

    def select(self):
        # Select all rows from the `authors` table
        self.cursor.execute("""SELECT id,username,firstname,lastname,password FROM authors""")
        rows = self.cursor.fetchall()
        return rows

    def find(self, id):
        # Select a row with id supplied from the `authors` table
        self.cursor.execute(f"""SELECT id,username,firstname,lastname,password FROM authors WHERE id = {id}""")
        rows = self.cursor.fetchall()
        return rows

    def update(self, id, params):
        # Update a row with id supplied in the `authors` table with
        # data provided as `params`
        with self.connection:
            self.cursor.execute(f"""UPDATE authors
                                SET username= %s,firstname= %s, lastname= %s, password= %s
                                WHERE id = {id}""", (params[0], params[1], params[2], params[3]))

    def delete(self, id):
        # Delete the row with id supplied from the `authors` table
        with self.connection:
            self.cursor.execute(f"""DELETE FROM authors WHERE id = {id}""")
