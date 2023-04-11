from Vertex import My_Vertex
from Edge import My_Edge

import numpy as np

class Graph():
    def __init__(self):
        self.vertices = []  # list of vertices in the graph
        self.edges = []     # list of edges in the graph
        self.num_vertices = 0
        self.num_edges = 0
        self.undirected_graph = True

    def double_array_size(self):
        self.vertices = self.vertices.copy() + [My_Vertex()] * len(self.vertices) * 2
        self.edges = self.edges.copy() + [My_Edge()] * len(self.edges) * 2 * (len(self.edges) * 2 -1)

    def get_number_of_vertices(self):
        """return: the number of vertices in the graph
        """
        return self.num_vertices

    def get_number_of_edges(self):
        """return: the number of edges in the graph
        """
        return self.num_edges

    def get_vertices(self):
        """return: array of length get_number_of_vertices() with the vertices in the graph
        """
        return self.vertices

    def get_edges(self):
        """return: array of length get_number_of_edges() with the edges in the graph
        """
        return self.edges

    def insert_vertex(self, vertex):
        """Inserts a new vertex into the graph and returns its index in the vertex array.
	    If the vertex array is already full, then the method double_array_size() shall be called
	    before inserting.
        None parameter is not allowed (ValueError).
        :param vertex: the vertex to be inserted
        :return: index of the new vertex in the vertex array
        :raises: ValueError if any of the parameters is None
        """
        if vertex is None:
            raise ValueError("Are you serious?")

        self.vertices.append(vertex)
        self.num_vertices += 1
        index = self.num_vertices - 1
        return index


    def has_edge(self, vertex1, vertex2):
        """Returns the edge weight if there is an edge between index vertex1 and vertex2, otherwise -1.
	    In case of unknown or identical vertex indices raise a ValueError.
        :param vertex1: first vertex
        :param vertex2: second vertex
        :return: edge weight of -1 if there is no edge
        :raises: ValueError if any of the parameters is None
        """
        if vertex1 == vertex2:
            raise ValueError("A loop has nothing to do here!")

        max_index = self.num_vertices - 1

        if vertex1 > max_index:
            raise ValueError("Learn to count indices, Donkey!")
        if vertex2 > max_index:
            raise ValueError("Learn to count indices, Donkey!")

        for x in self.edges:
            if x.vertex_in == vertex1 and x.vertex_out == vertex2:
                return x.weight

        return -1

    def insert_edge(self, vertex1, vertex2, weight):
        """Inserts an edge between vertices with index of vertex1 and index of vertex2. False is returned if the edge already exists,
	    True otherwise. A ValueError shall be raised if the vertex indices are unknown (out of range) or
	    if v1 == v2 (loop).
        .
        .
        :param vertex1: first index of vertex
        :param vertex2: second index of vertex
        :param weight: weight of the edge
        :return: True if the edge could be created, False otherwise
        :raises: ValueError if any of the parameters is None any of the vertices is out of range
        """
        if vertex1 == vertex2:
            raise ValueError("A loop has nothing to do here!")

        max_index = self.num_vertices - 1

        if vertex1 > max_index:
            raise ValueError("Learn to count indices, Donkey!")
        if vertex2 > max_index:
            raise ValueError("Learn to count indices, Donkey!")

        edge = My_Edge()
        edge.vertex_in = vertex1
        edge.vertex_out = vertex2
        edge.weight = weight

        for x in self.edges:
            if x.vertex_in == edge.vertex_in and x.vertex_out == edge.vertex_out:
                return False

        self.edges.append(edge)
        self.num_edges += 1

        return True

    def get_adjacency_matrix(self):
        """Returns an NxN adjacency matrix for the graph, where N = get_number_of_vertices().
        The matrix contains 1 if there is an edge at the corresponding index position, otherwise 0.
        :return: NxN adjacency matrix
        """
        adjacency_matrix = np.zeros(shape=(self.num_vertices, self.num_vertices))

        for x in self.edges:
            adjacency_matrix[x.vertex_in, x.vertex_out] = 1

        return adjacency_matrix

    def get_adjacent_vertices(self, vertex):
        """Returns an array of vertices which are adjacent to the vertex with index "vertex".
        :param vertex: The vertex of which adjacent vertices are searched.
        :return: array of adjacent vertices to "vertex".
        :raises: ValueError if the vertex index "vertex" is unknown
        """
        if vertex > self.num_vertices - 1:
            raise ValueError("You call yourself a programmer?")

        adj_vertices = []

        for edge in self.edges:
            if edge.vertex_in == vertex:
                adj_vertices.append(edge.vertex_out)
            if edge.vertex_out == vertex:
                adj_vertices.append(edge.vertex_in)

        return adj_vertices

    # ------------- """Example 2""" -------------

    def is_connected(self):
        """return: True if the graph is connected, otherwise False.
        """
        if self.num_vertices - self.num_edges <= 1:
            return True
        else:
            return False

    def get_number_of_components(self):
        """return: The number of all (weak) components
        """
        pass

    def print_components(self):
        """Prints the vertices of all components (one line per component).
        E.g.: A graph with 2 components (first with 3 vertices, second with 2 vertices) should look like:
   	 	[vertex1] [vertex2] [vertex3]
   	    [vertex4] [vertex5]
        """
        pass

    def is_cyclic(self):
        """return: Returns True if the graphs contains cycles, otherwise False.
        """
        pass

if __name__ == "__main__":
    map2 = Graph()

    linz = map2.insert_vertex(My_Vertex("Linz"))

    stpoelten = map2.insert_vertex(My_Vertex("St.Poelten"))

    wien = map2.insert_vertex(My_Vertex("Wien"))

    innsbruck = map2.insert_vertex(My_Vertex("Innsbruck"))

    bregenz = map2.insert_vertex(My_Vertex("Bregenz"))

    eisenstadt = map2.insert_vertex(My_Vertex("Eisenstadt"))

    graz = map2.insert_vertex(My_Vertex("Graz"))

    klagenfurt = map2.insert_vertex(My_Vertex("Klagenfurt"))

    salzburg = map2.insert_vertex(My_Vertex("Salzburg"))

    london = map2.insert_vertex(My_Vertex("London"))

    map2.insert_edge(linz, wien, 1)
    map2.insert_edge(wien, eisenstadt, 2)
    map2.insert_edge(wien, graz, 3)
    map2.insert_edge(graz, klagenfurt, 4)
    map2.insert_edge(bregenz, innsbruck, 5)
    map2.insert_edge(klagenfurt, innsbruck, 6)
    map2.insert_edge(salzburg, innsbruck, 7)
    map2.insert_edge(stpoelten, london, 10)

    print(map2.is_connected())

    map2.insert_edge(linz, london, 12)

    print(map2.is_connected())