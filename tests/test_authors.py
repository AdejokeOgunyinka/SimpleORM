import unittest
from unittest import TestCase
import os
from src.authors import Authors


class TestAuthors(TestCase):
    # Test each and every method in the Authors class
    def setUp(self) -> None:
        self.exec = Authors()

    def test_connect(self):
        self.assertEqual(self.exec.connect(), None)

    def test_create(self):
        self.exec.connect()
        # self.assertEqual(self.exec.connect(), None)
        self.assertEqual(self.exec.create(), None)
        self.exec.cursor.execute("""SELECT * FROM authors""")
        header_list = [tup[0] for tup in self.exec.cursor.description]
        self.assertEqual(header_list, ['id', 'username', 'firstname', 'lastname', 'password'])

    def test_insert(self):
        # self.assertEqual(self.exec.connect(), None)
        # self.assertEqual(self.exec.create(), None)
        self.exec.connect()
        self.exec.create()
        self.assertEqual(self.exec.insert(), None)
        self.exec.cursor.execute("""SELECT id,username,firstname,lastname,password FROM authors""")
        rows = self.exec.cursor.fetchall()

        self.assertEqual(rows, [(1, 'johndoe', 'John', 'Doe', 'john12345'), (2, 'janedoe', 'Jane', 'Doe', 'jane12345')])

    def test_select(self):
        # self.assertEqual(self.exec.connect(), None)
        # self.assertEqual(self.exec.create(), None)
        # self.assertEqual(self.exec.insert(), None)
        self.exec.connect()
        self.exec.create()
        self.exec.insert()
        self.assertEqual(self.exec.select(), [(1, 'johndoe', 'John', 'Doe', 'john12345'),
                                              (2, 'janedoe', 'Jane', 'Doe', 'jane12345')])

    def test_find(self):
        # self.assertEqual(self.exec.connect(), None)
        # self.assertEqual(self.exec.create(), None)
        # self.assertEqual(self.exec.insert(), None)
        self.exec.connect()
        self.exec.create()
        self.exec.insert()
        self.assertEqual(self.exec.find(1), [(1, 'johndoe', 'John', 'Doe', 'john12345')])
        # result1 = self.exec.cursor.fetchall()
        #
        # result2 = [(1, 'johndoe', 'John', 'Doe', 'john12345'),(2, 'janedoe', 'Jane', 'Doe', 'jane12345')]
        # self.assertEqual(result1, result2)


    def test_update(self):
        # self.assertEqual(self.exec.connect(), None)
        # self.assertEqual(self.exec.create(), None)
        # self.assertEqual(self.exec.insert(), None)'
        self.exec.connect()
        self.exec.create()
        self.exec.insert()
        result = [(2, 'janedoe', 'Jane', 'Doe', 'jane12345'), (1, 'archilles', 'archy', 'missile', 'archilles1234')]
        self.assertEqual(self.exec.update(1, ['archilles', 'archy', 'missile', 'archilles1234']), None)
        self.exec.cursor.execute("""SELECT id,username,firstname,lastname,password FROM authors""")
        rows = self.exec.cursor.fetchall()
        self.assertEqual(rows, result)

    def test_delete(self):
        # self.assertEqual(self.exec.connect(), None)
        # self.assertEqual(self.exec.create(), None)
        # self.assertEqual(self.exec.insert(), None)
        self.exec.connect()
        self.exec.create()
        self.exec.insert()
        self.assertEqual(self.exec.delete(1), None)
        self.exec.cursor.execute("""SELECT * FROM authors""")

        result1 = self.exec.cursor.fetchall()
        result2 = [(2, 'janedoe', 'Jane', 'Doe', 'jane12345')]
        self.assertEqual(result1, result2)

    def tearDown(self) -> None:
        self.exec.cursor.execute("""DROP TABLE IF EXISTS authors""")


if __name__ == '__main__':
    unittest.main()
