import unittest

from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    def add_node_to_graph(self, ls, g):
        for i in ls:
            g.add_node(i)

    def add_edge_to_graph(self, ls, g):
        for i in ls:
            g.add_edge(*i)

    def test_remove_node(self):
        # setup
        g = DiGraph()
        self.add_node_to_graph((1, 3, 4), g)
        self.add_edge_to_graph([(1, 3, 1)], g)
        lis_d = g.src_dest
        lid_s = g.dest_src
        nodes = g.nodes
        g.add_node(2)
        self.add_edge_to_graph([(1, 2, 1), (3, 2, 1), (4, 2, 1)], g)

        # remove node that don't exist
        self.assertFalse(g.remove_node(5))

        # remove node that only connect to her
        self.assertTrue(g.remove_node(2))
        self.assertEqual(g.nodes, nodes)
        self.assertEqual(g.src_dest, lis_d)
        self.assertEqual(g.dest_src, lid_s)

        # double remove
        self.assertFalse(g.remove_node(2))
        self.assertEqual(g.nodes, nodes)
        self.assertEqual(g.src_dest, lis_d)
        self.assertEqual(g.dest_src, lid_s)

        # remove node that only connect to others
        g.add_node(2)
        self.add_edge_to_graph([(2, 3, 1), (2, 1, 1)], g)
        self.assertTrue(g.remove_node(2))
        self.assertEqual(g.nodes, nodes)
        self.assertEqual(g.src_dest, lis_d)
        self.assertEqual(g.dest_src, lid_s)

        # double remove
        self.assertFalse(g.remove_node(2))
        self.assertEqual(g.nodes, nodes)
        self.assertEqual(g.src_dest, lis_d)
        self.assertEqual(g.dest_src, lid_s)

        # mix connections
        g.add_node(2)
        self.add_edge_to_graph([(1, 2, 1), (3, 2, 1), (4, 2, 1), (2, 3, 1), (2, 1, 1)], g)
        self.assertTrue(g.remove_node(2))
        self.assertEqual(g.nodes, nodes)
        self.assertEqual(g.src_dest, lis_d)
        self.assertEqual(g.dest_src, lid_s)

        # double remove
        self.assertFalse(g.remove_node(2))
        self.assertEqual(g.nodes, nodes)
        self.assertEqual(g.src_dest, lis_d)
        self.assertEqual(g.dest_src, lid_s)

    def test_remove_edge(self):
        g = DiGraph()
        # remove if g is none
        self.assertFalse(g.remove_edge(1, 4))
        self.assertEqual(g.num_of_edges, 0)
        self.assertEqual(g.src_dest, {})
        self.assertEqual(g.dest_src, {})
        self.add_node_to_graph(range(1, 5), g)
        # if no edges
        self.assertFalse(g.remove_edge(1, 4))
        self.assertEqual(g.num_of_edges, 0)
        self.assertEqual(g.src_dest, {})
        self.assertEqual(g.dest_src, {})
        # if there are edges
        self.add_edge_to_graph([(3, 2, 1), (1, 3, 1), (4, 2, 1)], g)
        e = g.e_size()
        lis_d = g.src_dest
        lid_s = g.dest_src
        self.add_edge_to_graph([(1, 2, 1)], g)
        self.assertTrue(g.remove_edge(1, 2))
        self.assertEqual(g.num_of_edges, e)
        self.assertEqual(g.src_dest, lis_d)
        self.assertEqual(g.dest_src, lid_s)


if __name__ == '__main__':
    unittest.main()
