# This is a useful data structure for implementing
# a counter that counts the time.
class DFSTimeCounter:
    def __init__(self):
        self.count = 0

    def reset(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1

    def get(self):
        return self.count

class UndirectedGraph:

    # n is the number of vertices
    # we will label the vertices from 0 to self.n -1
    # Initialize to an empty adjacency list
    # We will store the outgoing edges using a set data structure
    def __init__(self, n):
        self.n = n
        self.adj_list = [ set() for i in range(self.n) ]

    def add_edge(self, i, j):
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        assert i != j
        # Make sure to add edge from i to j
        self.adj_list[i].add(j)
        # Also add edge from j to i
        self.adj_list[j].add(i)

    # get a set of all vertices that
    # are neighbors of the
    # vertex i
    def get_neighboring_vertices(self, i):
        assert 0 <= i < self.n
        return self.adj_list[i]

    # Function: dfs_visit
    # Program a DFS visit of a graph.
    # We maintain a list of discovery times and finish times.
    # Initially all discovery times and finish times are set to None.
    # When a vertex is first visited, we will set discovery time
    # When DFS visit has processed all the neighbors then
    # set the finish time.
    # DFS visit should update the list of discovery and finish times in-place
    # Arguments
    #  i --> id of the vertex being visited.
    #  dfs_timer --> An instance of DFSTimeCounter structure provided for you.
    #  discovery --> discovery time of each vertex -- a list of size self.n
    #                None if the vertex is yet to be visited.
    #  finish --> finish time of each vertex -- a list of size self.n
    #                None if the vertex is yet to be finished.
    #  dfs_tree_parent --> the parent for for each node
    #                       if we visited node j from node i, then j's parent is i.
    #                      Do not forget to set tree_parent when you call dfs_visit
    #                                                         on node j from node i.
    #  dfs_back_edges --> a list of back edges.
    #                     a back edge is an edge from i to j wherein
    #                     DFS has already discovered j when i is discovered
    #                                     but not finished j

    def dfs_visit(self, i, dfs_timer, discovery_times, finish_times,
                  dfs_tree_parent, dfs_back_edges):
        assert 0 <= i < self.n
        assert discovery_times[i] == None
        assert finish_times[i] == None
        discovery_times[i] = dfs_timer.get()
        dfs_timer.increment()
        # your code here
        neighbors = self.get_neighboring_vertices(i)
        for neighbor in neighbors:
            if discovery_times[neighbor] == None:
                dfs_tree_parent[neighbor] = i
                dfs_back_edges.append((neighbor, i))
                self.dfs_visit(neighbor,dfs_timer, discovery_times, finish_times,
                               dfs_tree_parents, dfs_back_edges)
            else:
                if finish_times[neighbor] == None and (neighbor, i) not in dfs_back_edges and (i, neighbor) not in dfs_back_edges:
                    dfs_back_edges.append((i, neighbor))
        finish_times[i] = dfs_timer.get()
        dfs_timer.increment()

    # Function: dfs_traverse_graph
    # Traverse the entire graph.
    def dfs_traverse_graph(self):
        dfs_timer = DFSTimeCounter()
        discovery_times = [None]*self.n
        finish_times = [None]*self.n
        dfs_tree_parents = [None]*self.n
        finish_order = []
        dfs_back_edges = []
        for i in range(self.n):
            if discovery_times[i] == None:
                self.dfs_visit(i,dfs_timer, discovery_times, finish_times,
                               dfs_tree_parents, dfs_back_edges)
        # Clean up the back edges so that if (i,j) is a back edge then j cannot
        # be i's parent.
        non_trivial_back_edges = [(i,j) for (i,j) in dfs_back_edges if dfs_tree_parents[i] != j]
        return (dfs_tree_parents, non_trivial_back_edges, discovery_times, finish_times)

# create the graph from problem 1A.
g = UndirectedGraph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,4)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)


# Test DFS visit
discovery_times = [None]*5
finish_times = [None]*5
dfs_tree_parents = [None]*5
dfs_back_edges = []
g.dfs_visit(0, DFSTimeCounter(), discovery_times, finish_times, dfs_tree_parents, dfs_back_edges)

print('DFS visit discovery and finish times given by your code.')
print('Node\t Discovery\t Finish')
for i in range(5):
    print(f'{i} \t {discovery_times[i]}\t\t {finish_times[i]}')



print()
# Filter out all trivial back eddges (i,j)  where j is simply the parent of i.
# such back edges occur because we are treating an undirected edge as two directed edges
# in either direction.
non_trivial_back_edges = [(i,j) for (i,j) in dfs_back_edges if dfs_tree_parents[i] != j]
print('Back edges are')
for (i,j) in non_trivial_back_edges:
    print(f'{(i,j)}')


assert len(non_trivial_back_edges) == 2, f'Fail: There must be 2 non trivial back edges -- your code reports {len(non_trivial_back_edges)}. Note that (4,0) and (4,2) are the only non trivial backedges'
assert (4,2) in non_trivial_back_edges, '(4,2) must be a backedge that is non trivial'
assert (4,0) in non_trivial_back_edges, '(4,3) must be a non-trivial backedges'

print('Success -- 15 points!')

print()

def num_connected_components(g): # g is an UndirectedGraph class
    # your code here
    graph_size = len(g.adj_list)
    tg = g.dfs_traverse_graph()
    finish_times = tg[3]
    #print(finish_times)
    stack = []
    max_time = max(finish_times)
    for i in range(max_time + 1):
        for j in range(len(finish_times)):
            #print(finish_times[j], i, j)
            if finish_times[j] == i:
                #print('adding ', j)
                stack.append(j)
    discovery_times = [None]*graph_size
    finish_times = [None]*graph_size
    dfs_tree_parents = [None]*graph_size
    dfs_back_edges = []
    #print(stack)
    num_connected_components_counter = 0
    while stack:
        edge = stack.pop()
        if discovery_times[edge] == None:
            num_connected_components_counter += 1
            g.dfs_visit(edge, DFSTimeCounter(), discovery_times, finish_times, dfs_tree_parents, dfs_back_edges)
        #print(discovery_times)
    return num_connected_components_counter

# create the graph from problem 1A.
g = UndirectedGraph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,4)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,4)

print(num_connected_components(g))

g2 = UndirectedGraph(7)
g2.add_edge(0,1)
g2.add_edge(0,2)
g2.add_edge(0,4)
g2.add_edge(2,3)
g2.add_edge(2,4)
g2.add_edge(3,4)
g2.add_edge(5,6)

print(num_connected_components(g2))
#assert num_connected_components(g) == 1, f' Test A failed: g must have 1 connected component. Your code returns {num_connected_components(g)}'



