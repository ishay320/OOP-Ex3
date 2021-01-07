import random
import unittest

import GraphAlgo
from DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    def random_pos(self, from_pos: tuple, to_pos: tuple, seed: int) -> tuple:
        """
        private method that gives random pos
        @param from_pos: point of the start in x, y
        @param to_pos: point of the end in x, y
        @param seed: seed of randomness
        @return: random pos in range
        """
        random.seed(seed)
        rx = random.uniform(from_pos[0], to_pos[0])
        ry = random.uniform(from_pos[1], to_pos[1])
        return rx, ry

    @staticmethod
    def random_node(nodes):
        i = [*nodes.keys()]
        return random.choice(i)

    def random_graph(self, size: int = 10, random_pos: (tuple, tuple) = None, edge_size: int = 0) -> DiGraph:
        g = DiGraph()
        if random_pos is not None:
            for i in range(0, size):
                g.add_node(i, self.random_pos(*random_pos, i))
        else:
            for i in range(0, size):
                g.add_node(i)
        while g.e_size() < edge_size:
            g.add_edge(self.random_node(g.nodes), self.random_node(g.nodes), random.random())
        return g

    def test_something(self):
        g = self.random_graph(12, ((0, 0), (1, 2)), 9)
        print(g)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
