import unittest

from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    @staticmethod
    def add_node_to_graph(ls, g):
        for i in ls:
            g.add_node(i)

    @staticmethod
    def add_edge_to_graph(ls, g):
        for i in ls:
            g.add_edge(*i)

    def test_add_node(self):
        # setup
        g = DiGraph()

        # none in graph
        self.assertEqual(g.nodes, {})

        # one node without pos
        self.assertTrue(g.add_node(1))
        self.assertTrue(1 in g.nodes)

        # replace with one with pos

        self.assertFalse(g.add_node(1, (23, 32)))  # cannot do it - check with boaz

        # second with pos
        self.assertTrue(g.add_node(2, (23, 32)))
        self.assertTrue(2 in g.nodes)
        self.assertEqual(g.nodes[2], (23, 32))

    def test_add_edge(self):
        # setup
        g = DiGraph()
        self.add_node_to_graph((1, 2), g)

        # none exist
        self.assertFalse(g.add_edge(3, 4, 1))

        # src exist
        self.assertFalse(g.add_edge(2, 4, 1))

        # dst exist
        self.assertFalse(g.add_edge(3, 2, 1))

        # both exist
        self.assertTrue(g.add_edge(1, 2, 1))

        # again
        self.assertFalse(g.add_edge(1, 2, 1))

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
        # setup
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

    def test_mc(self):
        # setup
        g = DiGraph()
        mc = g.get_mc()

        # mc in add node
        g.add_node(1)
        self.assertNotEqual(mc, g.get_mc())

        # mc in add edge
        g.add_node(2)
        mc = g.get_mc()
        g.add_edge(1, 2, 1)
        self.assertNotEqual(mc, g.get_mc())

        # mc in remove node
        mc = g.get_mc()
        g.remove_node(2)
        self.assertNotEqual(mc, g.get_mc())

        # mc in remove edge
        g.add_node(2)
        g.add_edge(1, 2, 1)
        mc = g.get_mc()
        g.remove_edge(1, 2)
        self.assertNotEqual(mc, g.get_mc())


if __name__ == '__main__':
    unittest.main()
