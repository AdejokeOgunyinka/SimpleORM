import unittest
from unittest import TestCase
import os
from src.books import Books


class TestBooks(TestCase):
    # Test each and every method in the Books class
    def setUp(self) -> None:
        self.exec = Books()
        self.cwd = os.getcwd()
        self.csv_path = self.cwd + '/projectdb.sqlite'
        self.does_file_exist = lambda path: os.path.exists(path)

    def test_connect(self):
        self.assertEqual(self.exec.connect(), None)
        self.assertTrue(self.does_file_exist(self.csv_path))

    def test_create(self):
        self.exec.connect()
        self.assertEqual(self.exec.create(), None)
        self.exec.cursor.execute("""SELECT * FROM books""")
        header_list = [tup[0] for tup in self.exec.cursor.description]
        self.assertEqual(header_list, ['id', 'author_id', 'title', 'page_count'])

    def test_insert(self):
        self.exec.connect()
        self.exec.create()
        self.assertEqual(self.exec.insert(), None)
        result = self.exec.cursor.execute("""SELECT * FROM books""").fetchall()
        self.assertEqual(result, [(1, 1, "Pride and Prejudice", 10), (2, 2, "The Red and the Black", 120),
                                  (3, 1, "David Copperfield", 40), (4, 2, "Madame Bovary", 190),
                                  (5, 1, "Moby-Dick", 900), (6, 2, "Wuthering Heights", 67)])

    def test_select(self):
        self.exec.connect()
        self.exec.create()
        self.exec.insert()
        self.assertEqual(self.exec.select(), [(1, 1, "Pride and Prejudice", 10), (2, 2, "The Red and the Black", 120),
                                                 (3, 1, "David Copperfield", 40), (4, 2, "Madame Bovary", 190),
                                                 (5, 1, "Moby-Dick", 900), (6, 2, "Wuthering Heights", 67)])

    def test_find(self):
        self.exec.connect()
        self.exec.create()
        self.exec.insert()
        self.assertEqual(self.exec.find(1), [(1, 1, 'Pride and Prejudice', 10)])
        # pass

    def test_update(self):
        self.exec.connect()
        self.exec.create()
        self.exec.insert()
        result = [(1, 3, 'Sense and Sensibility', 200), (2, 2, "The Red and the Black", 120),
                  (3, 1, "David Copperfield", 40), (4, 2, "Madame Bovary", 190),
                  (5, 1, "Moby-Dick", 900), (6, 2, "Wuthering Heights", 67)]
        self.assertEqual(self.exec.update(1, [3, 'Sense and Sensibility', 200]), None)
        result2 = self.exec.cursor.execute("""SELECT * FROM books""").fetchall()
        self.assertEqual(result2, result)

    def test_delete(self):
        self.exec.connect()
        self.exec.create()
        self.exec.insert()
        self.assertEqual(self.exec.delete(1), None)
        result1 = self.exec.cursor.execute("""SELECT * FROM books""").fetchall()
        result2 = [(2, 2, "The Red and the Black", 120),
                   (3, 1, "David Copperfield", 40), (4, 2, "Madame Bovary", 190),
                   (5, 1, "Moby-Dick", 900), (6, 2, "Wuthering Heights", 67)]
        self.assertEqual(result1, result2)


    def tearDown(self) -> None:
        self.exec.cursor.execute("""DROP TABLE IF EXISTS books""")


if __name__ == '__main__':
    unittest.main()
