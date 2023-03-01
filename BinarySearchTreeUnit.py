import unittest
from BinarySearchTree import BinarySearchTree

class TestTree(unittest.TestCase):
    def test_treeIsEmpty(self):
        tree = BinarySearchTree()
        self.assertIsNotNone(tree)
        self.assertIsNone(tree.root)
        self.assertEqual(tree.size, 0)


    def test_treeIsNotEmpty(self):
        tree = BinarySearchTree()
        tree[10] = 10
        self.assertIsNotNone(tree)
        self.assertIsNotNone(tree.root)
        self.assertEqual(tree.root.payload, 10)
        self.assertEqual(tree.size, 1)


    def test_treePut(self):
        tree = BinarySearchTree()
        tree[10] = 10
        tree[5] = 5
        tree[20] = 20
        self.assertIsNotNone(tree)
        self.assertIsNotNone(tree.root)
        self.assertIsNotNone(tree.root.leftChild)
        self.assertIsNotNone(tree.root.rightChild)
        self.assertEqual(tree.root.payload, 10)
        self.assertEqual(tree.root.leftChild.payload, 5)
        self.assertEqual(tree.root.rightChild.payload, 20)
        self.assertEqual(tree.size, 3)


    def test_treeDelete(self):
        tree = BinarySearchTree()
        tree[10] = 10
        tree[5] = 5
        tree[20] = 20
        tree.delete(5)
        self.assertIsNotNone(tree)
        self.assertIsNotNone(tree.root)
        self.assertIsNone(tree.root.leftChild)
        self.assertIsNotNone(tree.root.rightChild)
        self.assertEqual(tree.root.payload, 10)
        self.assertEqual(tree.root.rightChild.payload, 20)
        self.assertEqual(tree.size, 2)


    def test_treeContains(self):
        tree = BinarySearchTree()
        tree[10] = 10
        tree[5] = 5
        tree[20] = 20
        self.assertIn(10, tree)
        self.assertNotIn(8, tree)


if __name__ == '__main__':
    unittest.main()   