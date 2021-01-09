# Directed Weighted Graph

## Contributors:
* ishay320
* uriya222

## about the project
this is a university project about directed weighted graph in python.

## How to use
download and put in your favorite IDE :)  
in src/DiGraph.py is the object that contain the graph.  
in src/GraphAlgo.py is the object that do the algorithm.

## How its built
the GraphAlgo contain the logic pf the algorithm that operate on the graph that in DiGraph.



## commands:
<details>
  <summary>DiGraph</summary>
  
  ```python
def v_size(self) -> int: # returns the number of nodes in the graph
def e_size(self) -> int: # returns the number of edges
def all_v(self) -> dict: # return a dictionary of all the nodes in the Graph, each node is represented using a pair(node_id, node_data) for using
def get_all_v(self) -> dict: # return a dictionary of all the nodes in the Graph, each node is represented using a pair(node_id, node_data) for using
def all_in_edges_of_node(self, id1: int) -> dict: #return a dictionary of all the nodes connected to (into) node_id ,each node is represented using a pair (other_node_id, weight)
def all_out_edges_of_node(self, id1: int) -> dict: # return a dictionary of all the nodes connected from node_id , each node is represented using a pair(other_node_id, weight)
def get_mc(self) -> int: # returns the Modify Count
def add_edge(self, id1: int, id2: int, weight: float) -> bool: # Adds an edge to the graph.
def add_node(self, node_id: int, pos: tuple = None) -> bool: # Adds a node to the graph.
def remove_node(self, node_id: int) -> bool: # Removes a node from the graph.
def remove_edge(self, node_id1: int, node_id2: int) -> bool: # Removes an edge from the graph.
  ```
  </details>

  <details>
 
   <summary>GraphAlgo</summary>
   
   ```python
def get_graph(self) -> GraphInterface: # returns the directed graph
def connected_component(self, id1: int) -> list # Finds the Strongly Connected Component(SCC) that node id1 is a part of by using the dfs_algo method
def connected_components(self) -> List[list] # Finds all the Strongly Connected Component(SCC) in the graph
def shortest_path(id1: int, id2: int) -> (float, list) # Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
def save_to_json(file_name: str) -> bool # Saves the graph in JSON format to a file
def load_from_json(file_name: str) -> bool # Loads a graph from a json file
def plot_graph(self) -> None # Plots the graph
   ```
 </details>

 
## why we choose
We chose to build the graph from dictionaries because all the objects
 have a key field, and the access to the dictionary is really fast.
We chose Dijkstra's algorithm because it's fast.


## How to contribute:
 If you want you can issue an idea or a bug.

## Example

let's say that the graph represent a country, and the nodes to be the cities:
###### code example
  ```python
g = DiGraph()
g.add_node(1) #Jerusalem
g.add_node(2) #Tel-Aviv
g.add_node(3) #Elat
g.add_node(4) #Ramat-Gan
g.add_node(5) #Netanya
# add the edge with the distance
g.add_edge(1,2,20)
g.add_edge(1,3,123)
g.add_edge(3,1,112)
g.add_edge(1,4,14)
g.add_edge(4,2,12)
g.add_edge(4,5,34)
a = GraphAlgo(g) #for algorithms
a.shortest_path(1,5)
  ```
the shortest path from Jerusalem and Netanya is 48 km  
and the path is: jerusalem->Ramat-Gan->Netanya  
the graph will look like this:
(import photo)  