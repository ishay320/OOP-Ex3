from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    """This abstract class represents an interface of a graph."""

    def __init__(self, graph=None):
        if graph is not None:
            self.src_dest = graph.src_dest
            self.dest_src = graph.dest_src
            self.nodes = graph.nodes
            self.mc = graph.mc
            self.num_of_edges = graph.num_of_edges
        else:
            self.src_dest = {}
            self.dest_src = {}
            self.nodes = {}
            self.mc = 0
            self.num_of_edges = 0

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return len(self.nodes)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.num_of_edges

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        raise self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 not in self.nodes or id2 not in self.nodes or id2 == id1:
            return False
        if id1 in self.src_dest:  # check if the edge exist
            if id2 in self.src_dest[id1]:
                if self.src_dest[id1][id2] == weight:  ## TODO: check with boaz
                    return False
        if id1 in self.src_dest:
            self.src_dest[id1][id2] = weight
        else:
            self.src_dest[id1] = {id2: weight}
        if id2 in self.dest_src:
            self.dest_src[id2][id1] = weight
        else:
            self.dest_src[id2] = {id1: weight}
        self.mc += 1
        self.num_of_edges += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = pos
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        raise NotImplementedError
