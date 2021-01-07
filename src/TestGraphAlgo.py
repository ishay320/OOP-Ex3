import unittest

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class AlgoTest(unittest.TestCase):
    @staticmethod
    def add_node_to_graph(ls, g):
        for i in ls:
            g.add_node(i)

    @staticmethod
    def add_edge_to_graph(ls, g):
        for i in ls:
            g.add_edge(*i)

    def test_shortest_path(self):
        # setup
        g = DiGraph()
        a = GraphAlgo()

        # empty shortest
        self.assertEqual(a.shortest_path(1, 2), (float('inf'), []))

        # only 1 node
        g.add_node(1)
        a = GraphAlgo(g)
        self.assertEqual(a.shortest_path(1, 1), (0, [1]))

        # node don't exist
        self.assertEqual(a.shortest_path(1, 2), (float('inf'), []))
        self.assertEqual(a.shortest_path(2, 1), (float('inf'), []))

        # 2 disconnected
        g.add_node(2)
        a = GraphAlgo(g)
        self.assertEqual(a.shortest_path(1, 2), (float('inf'), []))
        self.assertEqual(a.shortest_path(1, 2), (float('inf'), []))

        # 2 connected
        g.add_edge(1, 2, 12)
        a = GraphAlgo(g)
        self.assertEqual(a.shortest_path(1, 2), (float(12), [1, 2]))
        self.assertEqual(a.shortest_path(2, 1), (float('inf'), []))

        # 3 disconnected
        g.add_node(3)
        a = GraphAlgo(g)
        self.assertEqual(a.shortest_path(1, 3), (float('inf'), []))

        # 3 connected
        g.add_edge(2, 3, 12)
        a = GraphAlgo(g)
        self.assertEqual(a.shortest_path(1, 3), (12 * 2, [1, 2, 3]))

        # 4 with 2 paths and loop
        g.add_node(4)
        g.add_edge(3, 4, 12)
        g.add_edge(4, 1, 12)
        g.add_edge(3, 1, 12)
        a = GraphAlgo(g)
        self.assertEqual(a.shortest_path(2, 1), (12 * 2, [2, 3, 1]))

    def test_connected_component(self):
        # setup
        g = DiGraph()
        a = GraphAlgo()

        # empty
        self.assertEqual(a.connected_component(1), [])

        # only 1 node
        g.add_node(1)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_component(1), [1])

        # node don't exist
        self.assertEqual(a.connected_component(2), [])

        # 2 disconnected
        g.add_node(2)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_component(1), [1])
        self.assertEqual(a.connected_component(2), [2])

        # 2 connected weak
        g.add_edge(1, 2, 12)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_component(1), [1])
        self.assertEqual(a.connected_component(2), [2])

        # 2 connected strong
        g.add_edge(2, 1, 12)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_component(1), [1, 2])
        self.assertEqual(a.connected_component(2), [1, 2])

        # 3 disconnected
        g.add_node(3)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_component(1), [1, 2])
        self.assertEqual(a.connected_component(3), [3])

        # 3 connected weak
        g.add_edge(2, 3, 12)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_component(1), [1, 2])
        self.assertEqual(a.connected_component(3), [3])

        # 3 connected strong
        g.add_edge(3, 1, 12)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_component(1), [1, 2, 3])
        self.assertEqual(a.connected_component(3), [1, 2, 3])

    def test_json(self):
        # setup
        g = DiGraph()
        a = GraphAlgo(g)

        # if no name
        self.assertFalse(a.load_from_json("hi!"))

        # empty export
        self.assertTrue(a.save_to_json("test"))

        # read the file and check
        self.assertTrue(a.load_from_json("test"))
        self.assertEqual(a.get_graph().all_v(), {})

        # have some data
        g = DiGraph()
        self.add_node_to_graph(range(1, 4), g)
        g.add_node(4, (12, 13))
        self.add_edge_to_graph([(1, 2, 0), (2, 3, 1), (3, 1, 2), (4, 2, 3)], g)
        a = GraphAlgo(g)
        b = GraphAlgo()
        self.assertTrue(a.save_to_json("test"))
        self.assertTrue(b.load_from_json("test"))
        self.assertEqual(a.get_graph().all_v(), b.get_graph().all_v())
        self.assertEqual(a.get_graph().get_mc(), b.get_graph().get_mc())
        self.assertEqual(a.get_graph().all_out_edges_of_node(2), b.get_graph().all_out_edges_of_node(2))

    def test_connected_components(self):
        # setup
        g = DiGraph()
        a = GraphAlgo()

        # empty
        self.assertEqual(a.connected_components(), [])

        # only 1 node
        g.add_node(1)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_components(), [[1]])

        # 2 disconnected
        g.add_node(2)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_components(), [[1], [2]])

        # 2 connected weak
        g.add_edge(1, 2, 12)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_components(), [[1], [2]])

        # 2 connected strong
        g.add_edge(2, 1, 12)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_components(), [[1, 2]])

        # 3 disconnected
        g.add_node(3)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_components(), [[1, 2], [3]])

        # 3 connected weak
        g.add_edge(2, 3, 12)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_components(), [[1, 2], [3]])

        # 3 connected strong
        g.add_edge(3, 1, 12)
        a = GraphAlgo(g)
        self.assertEqual(a.connected_components(), [[1, 2, 3]])


if __name__ == '__main__':
    AlgoTest.main()
