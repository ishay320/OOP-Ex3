import unittest

from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    def add_node_to_graph(self,ls,g):
        for i in ls:
            g.add_node(i)

    def add_edge_to_graph(self,ls,g):
        for i in ls:
            g.add_edge(*i)

    def test_remove_node(self):
        g=DiGraph()
        self.add_node_to_graph(range(1,4),g)
        self.add_edge_to_graph([(1,2,1),(3, 2, 1),(1, 3, 1),(4, 2, 1)],g)
        self.assertFalse(g.remove_node(5))
        self.assertTrue(g.remove_node(2))
        self.assertFalse(2 in g.nodes)
        self.assertFalse(g.remove_node(2))
        g.add_node(2)
        self.add_edge_to_graph([(2, 3, 1),(2, 1, 1)], g)
        self.assertTrue(g.remove_node(2))
        self.assertFalse(2 in g.nodes)
        self.assertFalse(g.remove_node(2))
        self.assertFalse(2 in g.src_dest)
        self.assertFalse(2 in g.dest_src[3])
        g.add_node(2)
        self.add_edge_to_graph([(1, 2, 1), (3, 2, 1), (4, 2, 1),(2, 3, 1),(2, 1, 1)], g)
        print(g.src_dest, g.dest_src)
        self.assertTrue(g.remove_node(2))
        self.assertFalse(2 in g.nodes)
        self.assertFalse(g.remove_node(2))
        self.assertFalse(2 in g.src_dest)
        print(g.src_dest,g.dest_src)





if __name__ == '__main__':
    unittest.main()
