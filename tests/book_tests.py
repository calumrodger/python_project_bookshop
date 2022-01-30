import unittest
from models.book import Book

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book('A Little Larger than the Entire Universe', "Penguin", 'Fernando Pessoa', 'poetry', 3, 7.00, 10.99, 3.99, 'The definitive English translation of the iconic Portugeuse poet.')

    def test_sell_copy(self):
        self.book.sell_copy()
        self.assertEqual(2, self.book.stock)