import random
import unittest

from GraphAlgo import GraphAlgo
from DiGraph import DiGraph
from TestGraphAlgo import copy_to_nex
import networkx as nx
from timeit import default_timer as timer


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

    def test_all_the_graphs_for_correctness(self):  # takes looooooong time so.. run it on your weekend :)
        # g = self.random_graph(12, ((0, 0), (1, 2)), 9)
        a = GraphAlgo()
        l = ["../data/G_10_80_0.json", "../data/G_100_800_0.json", "../data/G_1000_8000_0.json",
             "../data""/G_10000_80000_0.json", "../data/G_20000_160000_0.json", "../data/G_30000_240000_0.json"]
        for i in l:
            print("Graph:", i, ":")
            a.load_from_json(i)
            n = copy_to_nex(a.get_graph())
            # shortest path
            print("shortest path:")  # speed test
            sum_of_runs = 0
            for j in range(10):
                s, e = random.randint(0, len(a.get_graph().nodes) - 1), random.randint(0, len(a.get_graph().nodes) - 1)
                start = timer()
                a.shortest_path(s, e)
                end = timer()
                sum_of_runs += end - start
            sum_of_runs /= 10
            print("us:", sum_of_runs)
            sum_of_runs = 0
            for j in range(10):
                s, e = random.randint(0, len(a.get_graph().nodes) - 1), random.randint(0, len(a.get_graph().nodes) - 1)
                start = timer()
                nx.shortest_path_length(n, s, e, weight="weight")
                end = timer()
                sum_of_runs += end - start
            sum_of_runs /= 10
            print("networkX:", sum_of_runs)

            list_of_a = a.shortest_path(0, 9)  # correctness check
            path_of_n = nx.shortest_path_length(n, 0, 9, weight="weight")
            list_of_n = nx.shortest_path(n, 0, 9, weight="weight")
            self.assertEqual(path_of_n, list_of_a[0])
            self.assertEqual(list_of_n, list_of_a[1])
            # connected components
            print("connected components:")
            sum_of_runs = 0
            for j in range(10):
                start = timer()
                a.connected_components()
                end = timer()
                sum_of_runs += end - start
            sum_of_runs /= 10
            print("us:", sum_of_runs)
            sum_of_runs = 0
            for j in range(10):
                start = timer()
                nx.strongly_connected_components(n)
                end = timer()
                sum_of_runs += end - start
            sum_of_runs /= 10
            print("networkX:", sum_of_runs)

            connected_a = a.connected_components()  # correctness check
            connected_n = nx.strongly_connected_components(n)
            set_list = list()
            for j in connected_a:
                set_list.append(set(j))
            for j in connected_n:
                self.assertIn(j, set_list)


if __name__ == '__main__':
    unittest.main()
