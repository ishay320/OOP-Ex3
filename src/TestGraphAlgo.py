import unittest

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class AlgoTest(unittest.TestCase):

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
        # 3 connected
        # 4 with 2 paths

        # if graph none and get
        # json for empty
        # check if same
        # open json empty
        # check if same
        # empty shortest
        # only 1
        # node don't exist
        # 2 connected
        # 3 disconnected
        # 3 connected
        # 4 with 2 paths

        # connected 1
        # 2 disconnected
        # 2 connected
        # 5 with 2 part


if __name__ == '__main__':
    AlgoTest.main()
