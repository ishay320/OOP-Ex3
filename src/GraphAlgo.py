import random
from typing import List
from queue import Queue
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from src import GraphInterface
import json
import matplotlib.pyplot as plt
import networkx as n


class GraphAlgo(GraphAlgoInterface):
    """
    This class represents directed (positive) Weighted Graph Theory algorithms,including the following method:
    1. init(graph)
    2. connected_component(self, id1: int) -> list
    3. connected_components(self) -> List[list]
    4. shortest_path(id1: int, id2: int) -> (float, list)
    5. save_to_json(file_name: str) -> bool
    6. load_from_json(file_name: str) -> bool
    7. plot_graph(self) -> None
  """

    def __init__(self, graph1=None):
        self.__graph = DiGraph(graph1)

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, if fail return False
        """
        try:
            with open(file_name, 'r') as f:
                json_obj = json.load(f)
            graph1 = DiGraph()
            json_nodes, json_edges = json_obj['Nodes'], json_obj['Edges']
            for obj in json_nodes:
                if 'pos' in obj and obj['pos'] is not None:
                    graph1.add_node(obj['id'], tuple(float(s) for s in obj['pos'].strip("()").split(",")))
                else:
                    graph1.add_node(obj['id'], None)
            for obj in json_edges:
                graph1.add_edge(obj['src'], obj['dest'], obj['w'])
            self.__init__(graph1)
            return True
        except FileNotFoundError:
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @returns True if the loading was successful, if fail return False
        """
        json1 = {'Nodes': [], 'Edges': []}
        for key, value in self.get_graph().all_v().items():
            if value is not None:
                json1['Nodes'].append({'pos': ','.join(str(x) for x in value), 'id': key})
            else:
                json1['Nodes'].append({'pos': None, 'id': key})
        for src in self.get_graph().all_v():
            if self.get_graph().all_out_edges_of_node(src) is not None:
                for dest, w in self.get_graph().all_out_edges_of_node(src).items():
                    json1['Edges'].append({'src': src, 'w': w, 'dest': dest})
        try:
            with open(file_name, 'w') as f:
                json.dump(json1, f)
                return True
        except FileExistsError:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        """
        if id1 not in self.get_graph().all_v() or id2 not in self.get_graph().all_v():
            return float('inf'), []
        if id1 == id2:
            return 0, [id1]
        visited, close, prev, dist = {}, {}, {}, 0
        for i in self.get_graph().all_v():
            visited[i], close[i], prev[i] = False, float('inf'), -1
        visited[id1], close[id1] = True, 0
        q = Queue(maxsize=len(self.get_graph().all_v()))
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
            tmp = self.__smallest_w(close, visited)
            if tmp > -1:
                q.put(tmp)
        if close[id2] == float('inf'):
            return float('inf'), []
        tmp2, ls = id2, []
        while tmp2 != -1:
            ls.insert(0, tmp2)
            tmp2 = prev[tmp2]
        return close[id2], ls

    def __smallest_w(self, close, visited) -> int:
        """
        this is a private method for the Dijkstra's Algorithm
        """
        min1, min_index = float('inf'), -1
        for i in close:
            if close[i] < min1 and not visited[i] and i in self.get_graph().all_v():
                min1, min_index = close[i], i
        return min_index

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of by using the dfs_algo method.
        If the graph is None or id1 is not in the graph, the function return an empty list []
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        ls = []
        if self.get_graph() is None or id1 not in self.get_graph().all_v():
            return ls
        v1 = self.__dfs_algo(id1, True)
        v2 = self.__dfs_algo(id1, False)
        for node in v1:
            if v1[node] and v2[node]:
                ls.append(node)
        return ls

    def __dfs_algo(self, id1, s) -> dict:
        """
        The DFS algorithm:
        1. add the id1 node to a Queue
        2. check if the Queue is empty (if so go to stage 3 ,else go to stage 6)
        3. pop the next node in the Queue to n
        4. add to the Queue all nodes who is neighbors to node n
        5. go back to stage 2
        6. return dict of all nodes that have been passed the Queue with value of True
        """
        visited = {}
        for i in self.get_graph().all_v():
            visited[i] = False
        q = Queue(maxsize=len(self.get_graph().all_v()))
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
        using the connected_component method for every node that not added yet to the list
        If the graph is None the function returns an empty list []
        @return: The list all SCC
        """
        ls = []
        if self.get_graph() is None or len(self.get_graph().all_v()) == 0:
            return []
        set_nodes = set()
        for node in self.get_graph().all_v():
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
        nodes1 = self.get_graph().nodes
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), -float('inf'), -float('inf')
        for key in nodes1:
            if nodes1[key] is not None:
                if nodes1[key][0] < min_x:
                    min_x = nodes1[key][0]
                if nodes1[key][1] < min_y:
                    min_y = nodes1[key][1]
                if nodes1[key][0] > max_x:
                    max_x = nodes1[key][0]
                if nodes1[key][1] > max_y:
                    max_y = nodes1[key][1]
        if min_x == float('inf') and min_y == float('inf'):
            min_x, min_y, max_x, max_y = 0, 0, len(nodes1)*2, len(nodes1)*2
        for key in nodes1:
            if nodes1[key] is None:
                nodes1[key] = self.__random_pos((min_x, min_y), (max_x, max_y), key)
        x = [nodes1[loc][0] for loc in nodes1]
        y = [nodes1[loc][1] for loc in nodes1]
        plt.plot(x, y, 'o', color='blue', ms=10)
        for node in nodes1:
            plt.text(nodes1[node][0], nodes1[node][1], f'{node}', fontsize=12, color='green')
            if self.get_graph().all_out_edges_of_node(node) is not None:
                for ne in self.get_graph().all_out_edges_of_node(node):
                    if nodes1[node] is not None and nodes1[ne] is not None:
                        x1, y1 = nodes1[node][0], nodes1[node][1]
                        x2, y2 = nodes1[ne][0], nodes1[ne][1]
                        plt.arrow(x1, y1, x2 - x1, y2 - y1, width=(max_y - min_y) / 400,
                                  head_width=(max_y - min_y) / 50,
                                  head_length=(max_y - min_y) / 15, length_includes_head=True, fc='k', ec='k')
        plt.show()

    @staticmethod
    def __random_pos(from_pos: tuple, to_pos: tuple, seed: int) -> tuple:
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
