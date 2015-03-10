import unittest
import myset

class TestMySet(unittest.TestCase):

    def setUp(self):
        self.set = myset.MySet(["a", "b", "c", "d", "e"])


    def test_add(self):
        self.set.add_item("a")  # Test adding a character that is already part of the set
        self.assertEqual(self.set.collection, ["a", "b", "c", "d", "e"])
        self.set.add_item("s")  # Test adding a new character
        self.assertEqual(self.set.collection, ["a", "b", "c", "d", "e", "s"])

    def test_remove(self):
        self.set.remove_item("a")
        self.assertEqual(self.set.collection, ["b", "c", "d", "e"])

    def test_is_empty(self):
        self.assertFalse(self.set.is_empty())

    def test_has_item(self):
        self.assertTrue(self.set.has_item("c"))
        self.assertFalse(self.set.has_item("z"))

    def test_intersection(self):
        new_set = ["d", "e", "f", "g"]
        self.assertEqual(self.set.intersection(new_set), ["d", "e"])

    def test_union(self):
        new_set = ["d", "e", "f", "g"]
        self.assertEqual(self.set.union(new_set), ["a", "b", "c", "d", "e", "f", "g"])

    def test_is_subset_of(self):
        self.assertTrue(self.set.is_subset_of(["b", "c"]))

if __name__ == '__main__':
    unittest.main()
