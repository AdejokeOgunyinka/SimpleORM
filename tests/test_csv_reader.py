import unittest
from src.csv_reader import CsvReader


class TestCsvReader(unittest.TestCase):
    """This class tests the CsvReader.read_csv function in the csv_reader file"""
    def setUp(self) -> None:
        self.exec = lambda file_path: CsvReader.read_csv(file_path)
        self.authors_csv = './data/authors.csv'
        self.books_csv = './data/books.csv'

    def test_correct_authors_file(self):
        result = [['id', 'username', 'firstname', 'lastname', 'password'],
                  ['1', 'johndoe', 'John', 'Doe', 'john12345'],
                  ['2', 'janedoe', 'Jane', 'Doe', 'jane12345']]

        self.assertEqual(self.exec(self.authors_csv), result)

    def test_correct_books_file(self):
        result = [['id', 'author_id', 'title', 'page_count'], ['1', '1', 'Pride and Prejudice', '10'],
                  ['2', '2', 'The Red and the Black', '120'], ['3', '1', 'David Copperfield', '40'],
                  ['4', '2', 'Madame Bovary', '190'], ['5', '1', 'Moby-Dick', '900'],
                  ['6', '2', 'Wuthering Heights', '67']]

        self.assertEqual(self.exec(self.books_csv), result)

    def test_wrong_file(self):
        with self.assertRaises(Exception):
            self.assertEqual(self.exec('./data/author.csv'), [])

    def tearDown(self) -> None:
        self.exec = None


if __name__ == '__main__':
    unittest.main()
