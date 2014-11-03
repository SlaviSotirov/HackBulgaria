import unittest
from directed_graph import DirectedGraph


class TestDirectedGraph(unittest.TestCase):
    NODE_A = "A"
    NODE_B = "B"
    NODE_C = "C"
    NODE_D = "D"

    def setUp(self):
        self.graph = DirectedGraph()

    def test_init(self):
        self.assertEqual({}, self.graph.nodes)

    def test_add_edge(self):
        self.graph.add_edge(self.NODE_A, self.NODE_B)
        graph_dict = {self.NODE_A: [self.NODE_B], self.NODE_B: []}
        self.assertEqual(graph_dict, self.graph.nodes)

    def test_more_edges(self):
        self.graph.add_edge(self.NODE_A, self.NODE_B)
        self.graph.add_edge(self.NODE_A, self.NODE_C)
        graph_dict = {self.NODE_A: [self.NODE_B, self.NODE_C], self.NODE_B: [], self.NODE_C: []}
        self.assertEqual(graph_dict, self.graph.nodes)

    def test_path_between(self):
        self.graph.add_edge(self.NODE_A, self.NODE_B)
        truth = self.graph.path_between(self.NODE_A, self.NODE_B)
        lie = self.graph.path_between(self.NODE_B, self.NODE_A)
        self.assertTrue(truth)
        self.assertFalse(lie)

    def test_long_path_between(self):
        self.graph.add_edge(self.NODE_A, self.NODE_B)
        self.graph.add_edge(self.NODE_B, self.NODE_C)
        truth = self.graph.path_between(self.NODE_A, self.NODE_C)
        self.assertTrue(truth)

    def test_very_long_path_between(self):
        self.graph.add_edge(self.NODE_A, self.NODE_B)
        self.graph.add_edge(self.NODE_B, self.NODE_C)
        self.graph.add_edge(self.NODE_C, self.NODE_D)
        truth = self.graph.path_between(self.NODE_A, self.NODE_D)
        self.assertTrue(truth)

    def test_false_path_between(self):
        self.graph.add_edge(self.NODE_A, self.NODE_B)
        self.graph.add_edge(self.NODE_C, self.NODE_D)
        truth = self.graph.path_between(self.NODE_A, self.NODE_D)
        self.assertFalse(truth)

    def test_two_way_directed(self):
        self.graph.add_edge(self.NODE_A, self.NODE_B)
        self.graph.add_edge(self.NODE_B, self.NODE_A)
        truth = self.graph.path_between(self.NODE_A, self.NODE_B)
        second_truth = self.graph.path_between(self.NODE_B, self.NODE_A)
        self.assertTrue(truth)
        self.assertTrue(second_truth)


if __name__ == '__main__':
    unittest.main()
