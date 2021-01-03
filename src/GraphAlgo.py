from typing import List
from queue import Queue
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from src import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    """This abstract class represents an interface of a graph."""

    def __init__(self):
        self.__graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        raise NotImplementedError

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        raise NotImplementedError

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        """
        if id1 not in self.get_graph().nodes or id2 not in self.get_graph().nodes:
            return float('inf'), []
        if id1 == id2:
            return 0, [id1]
        visited, close, prev, dist = {}, {}, {}, 0
        for i in self.get_graph().nodes:
            visited[i], close[i], prev[i] = False, float('inf'), -1
        visited[id1], close[id1] = True, 0
        q = Queue(maxsize=len(self.get_graph().nodes))
        q.put(id1)
        while not q.empty():
            u = q.get()
            if self.get_graph().all_out_edges_of_node(u) is not None:
                for i, w in self.get_graph().all_out_edges_of_node(u).items():
                    if not visited[i]:
                        dist = close[i]
                        close[i] = min(close[i], close[u] + w)
                        if close[i] != dist:
                            prev[i] = u
            visited[u] = True
            tmp = self.smallest_w(close, visited)
            if tmp > -1:
                q.put(tmp)
        if close[id2] == float('inf'):
            return float('inf'), []
        tmp2, ls = id2, []
        while tmp2 != -1:
            ls.insert(0, tmp2)
            tmp2 = prev[tmp2]
        return close[id2], ls

    def smallest_w(self, close, visited) -> int:
        min1, min_index = float('inf'), -1
        for i in close:
            if close[i] < min1 and not visited[i] and i in self.get_graph().nodes:
                min1, min_index = close[i], i
        return min_index

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC

        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        ls = []
        if self.get_graph() is None or id1 not in self.get_graph().nodes:
            return ls
        v1 = self.dfs_algo(id1, True)
        v2 = self.dfs_algo(id1, False)
        for node in v1:
            if v1[node] and v2[node]:
                ls.append(node)
        return ls

    def dfs_algo(self, id1, s) -> dict:
        visited = {}
        for i in self.get_graph().nodes:
            visited[i] = False
        q = Queue(maxsize=len(self.get_graph().nodes))
        q.put(id1)
        visited[id1] = True
        while not q.empty():
            n = q.get()
            if s:
                if self.get_graph().all_out_edges_of_node(n) is not None:
                    for i in self.get_graph().all_out_edges_of_node(n):
                        if not visited[i]:
                            q.put(i)
                            visited[i] = True
            else:
                if self.get_graph().all_in_edges_of_node(n) is not None:
                    for i in self.get_graph().all_in_edges_of_node(n):
                        if not visited[i]:
                            q.put(i)
                            visited[i] = True
        return visited

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC

        Notes:
        If the graph is None the function should return an empty list []
        """
        ls = []
        if self.get_graph() is None or len(self.get_graph().get_all_v()) == 0:
            return []
        set_nodes = set()
        for node in self.get_graph().get_all_v():
            if node not in set_nodes:
                tmp = self.connected_component(node)
                ls.append(tmp)
                set_nodes.update(tmp)
        return ls

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError
