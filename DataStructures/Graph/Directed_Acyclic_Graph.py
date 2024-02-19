from typing import List, Tuple
import networkx as nx
from matplotlib import pyplot as plt


class DAG:
    """
    A class representing a Directed Acyclic Graph (DAG) using the networkx library.
    It allows adding edges, verifying the acyclic property, and visualizing the graph.
    """

    def __init__(self):
        """
        Initializes a new instance of the DAG class with an empty directed graph.
        """
        self.graph = nx.DiGraph()

    def add_edge(self, edge: Tuple[str, str]) -> None:
        """
        Adds a single edge to the DAG and checks if the graph remains acyclic.

        Args:
            edge (Tuple[str, str]): The edge to add, represented as a tuple of two strings (source, target).

        Raises:
            Exception: If adding the edge would make the graph cyclic.
        """
        self.graph.add_edge(*edge)  # Unpack the edge tuple
        if not nx.is_directed_acyclic_graph(self.graph):
            self.graph.remove_edge(*edge)  # Correctly remove the edge if it creates a cycle
            raise Exception(f"Unable to insert {edge}. The graph must remain acyclic.")

    def add_edges(self, edges: List[Tuple[str, str]]) -> None:
        """
        Adds a list of edges to the DAG and checks if the graph remains acyclic.

        Args:
            edges (List[Tuple[str, str]]): A list of edges to add, each represented as a tuple of two strings (source, target).

        Raises:
            Exception: If adding any edge in the list would make the graph cyclic.
        """
        for edge in edges:
            self.add_edge(edge)  # Reuse the add_edge method to ensure acyclic property for each edge

    def visualize(self, location: str = "home") -> str:
        """
        Uses Matplotlib to visualize the DAG and saves the graph to a PNG file.

        Args:
            location (str): The file path where the graph image will be saved. Defaults to "home".

        Returns:
            str: A message indicating the outcome of the operation.

        Raises:
            Exception: If there is no graph to visualize.
        """
        if not self.graph:
            raise Exception("There is no graph to visualize. Consider adding edges first.")
        
        plt.tight_layout()
        nx.draw_networkx(self.graph, arrows=True, node_size=800)
        plt.savefig(location, format="PNG")
        plt.clf()  # Clear the figure to free up memory and prevent overlap if called again
        return "Graph generated at " + location


# Example usage:
graph = DAG()

graph.add_edges([
    ("root", "a"), ("a", "b"),
    ("a", "e"), ("b", "c"),
    ("b", "d"), ("d", "e")
])

graph.visualize("dag.png")