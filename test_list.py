import unittest
from my_list import MyList


class TestList(unittest.TestCase):

    def get_list(self):
        l = MyList()
        l.add(1)
        l.add(2)
        l.add(3)
        return l

    def test_size(self):
        l = self.get_list()
        self.assertEqual(l.get_size(), 3)

    def test_clear(self):
        l = self.get_list()
        self.assertEqual(l.get_size(), 3)
        l.clear()
        self.assertEqual(l.get_size(), 0)

    def test_add(self):
        l = self.get_list()
        self.assertEqual(l.get_size(), 3)
        l.add(4)
        self.assertEqual(l.get_size(), 4)

    def test_contains_item(self):
        l = self.get_list()
        self.assertTrue(l.contains(2))

    def test_get_by_index(self):
        l = self.get_list()
        self.assertTrue(l.get(0), 1)

    def test_search_item(self):
        l = self.get_list()
        self.assertTrue(l.search(2), 1)

    def test_remove_by_index(self):
        l = self.get_list()
        self.assertEqual(l.get_size(), 3)
        l.remove(0)
        self.assertEqual(l.get_size(), 2)

    def test_get_raises_negatives(self):
        l = self.get_list()
        self.assertRaises(IndexError, l.get, -1)

    def test_get_raises_great_than_length(self):
        l = self.get_list()
        self.assertRaises(IndexError, l.get, 55)

    def test_remove_raises_negatives(self):
        l = self.get_list()
        self.assertRaises(IndexError, l.remove, -1)

    def test_remove_raises_great_than_length(self):
        l = self.get_list()
        self.assertRaises(IndexError, l.remove, 55)
