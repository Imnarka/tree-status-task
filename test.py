import unittest
from tree_store import TreeStore


class TestTreeStatus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.items = [
            {"id": 1, "parent": "root"},
            {"id": 2, "parent": 1, "type": "test"},
            {"id": 3, "parent": 1, "type": "test"},
            {"id": 4, "parent": 2, "type": "test"},
            {"id": 5, "parent": 2, "type": "test"},
            {"id": 6, "parent": 2, "type": "test"},
            {"id": 7, "parent": 4, "type": None},
            {"id": 8, "parent": 4, "type": None}
        ]
        cls.tst = TreeStore(cls.items)

    def test_get_all(self):
        self.assertEqual(self.tst.getAll(), self.items)

    def test_get_by_id(self):
        self.assertEqual(self.tst.getItem(3), {"id": 3, "parent": 1, "type": "test"})

    def test_get_children(self):
        self.assertEqual(self.tst.getChildren(2), [
            {"id": 4, "parent": 2, "type": "test"},
            {"id": 5, "parent": 2, "type": "test"},
            {"id": 6, "parent": 2, "type": "test"},
        ])
        self.assertEqual(self.tst.getChildren(99), [])

    def test_get_parent(self):
        self.assertEqual(self.tst.getAllParents(7), [
            {"id": 1, "parent": "root"},
            {"id": 2, "parent": 1, "type": "test"},
            {"id": 4, "parent": 2, "type": "test"},
            {'id': 7, 'parent': 4, 'type': None}
        ])
        self.assertEqual(self.tst.getAllParents(1), [{"id": 1, "parent": "root"}])
        self.assertEqual(self.tst.getAllParents(1000), None)


if __name__ == '__main__':
    unittest.main()
