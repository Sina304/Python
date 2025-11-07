import unittest
from Tree import Tree

class TestTree(unittest.TestCase):
    
    def setUp(self):
        """Tworzymy przykładowe drzewo do testów"""
        self.root = Tree("Bogdan")
        self.a = Tree("Stasiek")
        self.b = Tree("C")
        self.c = Tree("D")
        self.a_a = Tree("Maciej")
        
        self.root.add_child(self.a, "syn")
        self.root.add_child(self.b, "syn")
        self.root.add_child(self.c, "córka")
        self.a.add_child(self.a_a, "wnuk")
    
    def test_node_values(self):
        """Test, czy wartości węzłów są poprawnie przypisane"""
        self.assertEqual(self.root.value, "Bogda")
        self.assertEqual(self.a.value, "Stasiek")
        self.assertEqual(self.a_a.value, "Maciej")
    
    def test_children_count(self):
        """Test liczby dzieci w węzłach"""
        self.assertEqual(len(self.root.children), 3)
        self.assertEqual(len(self.a.children), 1)
        self.assertEqual(len(self.b.children), 0)
    
    def test_DFS(self):
        """Test metody DFS"""
        expected = ["Bogdan", "Stasiek", "Maciej", "C", "D"]
        self.assertEqual(self.root.DFS(), expected)
    
    def test_str_contains_values(self):
        """Test czy __str__ zwraca wartości w węzłach"""
        tree_str = str(self.root)
        self.assertIn("Bogdan", tree_str)
        self.assertIn("Stasiek", tree_str)
        self.assertIn("Maciej", tree_str)
        self.assertIn("C", tree_str)
        self.assertIn("D", tree_str)
    
    def test_edge_labels_in_str(self):
        """Test, czy etykiety krawędzi pojawiają się w __str__"""
        tree_str = str(self.root)
        self.assertIn("(syn)", tree_str)
        self.assertIn("(córka)", tree_str)
        self.assertIn("(wnuk)", tree_str)

if __name__ == "__main__":
    unittest.main()
