class Solution:

    rank = {}
    graph = defaultdict(list)
    conn_dict = {}

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        self.formGraph(n, connections)
        self.dfs(0, 0)

        result = []
        for u, v in self.conn_dict:
            result.append([u, v])

        return result

    def dfs(self, node: int, discovery_rank: int) -> int:

        # That means this node is already visited. We simply return the rank.
        if self.rank[node]:
            return self.rank[node]

        # Update the rank of this node.
        self.rank[node] = discovery_rank

        # This is the max we have seen till now. So we start with this instead of INT_MAX or something.
        min_rank = discovery_rank + 1
        for neighbor in self.graph[node]:

            # Skip the parent.
            if self.rank[neighbor] and self.rank[neighbor] == discovery_rank - 1:
                continue

            # Recurse on the neighbor.
            recursive_rank = self.dfs(neighbor, discovery_rank + 1)

            # Step 1, check if this edge needs to be discarded.
            if recursive_rank <= discovery_rank:
                del self.conn_dict[(min(node, neighbor), max(node, neighbor))]

            # Step 2, update the minRank if needed.
            min_rank = min(min_rank, recursive_rank)

        return min_rank

    def formGraph(self, n: int, connections: List[List[int]]):

        # Reinitialize for each test case
        self.rank = {}
        self.graph = defaultdict(list)
        self.conn_dict = {}

        # Default rank for unvisited nodes is "null"
        for i in range(n):
            self.rank[i] = None

        for edge in connections:

            # Bidirectional edges.
            u, v = edge[0], edge[1]
            self.graph[u].append(v)
            self.graph[v].append(u)

            self.conn_dict[(min(u, v), max(u, v))] = 1


# Time Complexity: O(V + E)O(V+E) where VV represents the number of vertices and EE represents the number of edges in the graph. We process each node exactly once thanks to the rank dictionary also acting as a "visited" safeguard at the top of the dfs function. Since the problem statement mentions that the graph is connected, that means E >= VE>=V and hence, the overall time complexity would be dominated by the number of edges i.e. O(E)O(E).

# Space Complexity: O(E)O(E). The overall space complexity is a sum of the space occupied by the connDict dictionary, rank dictionary, and graph data structure. E + V + (V + E)E+V+(V+E) = O(E)O(E).


# Tarjan's algorithm

# given an undirected graph and are asked to find the number of bridges in the graoh.
# a bridge is essentially an edge whose removal would make the graph disconnected.
# how could we apply existing knowledge of DFS to derive a solution
# an edge is a critical connection if and only if it is not in a cycle

# Depth first search for cycle detection

# define a functio called dfs that takes in the node and the discoveryRank to be assigned to this node
# the first step is to build the graph itself, for that we'll be using an adjacency list structure
# since our algorithm involves discarding edges, we need some efficient data structure that will allow us to do this operation in O(1) time.  We'll convert the list of edges into a dictionary for that.
# name our graph and our connections dictionary as connDict.
# use an array to keep track of the rank of our nodes.  That's something we define in the main function criticalConnections along with all the things explained above.
# within dfs,check if the node already has a rank assigned; if so, return that value
# assign the rank of this node to the discoveryRank
# iterate over all the neighbors of the node and for each of them, make a recursive call and obtain the recursiveRank as the return value and do two things using this value.
# If this recursiveRank is less than the current discoveryRank, this means the edge is a part of the cycle and can be discarded.
# second, record the minimum rank till now from amongst all the neighbors.
# return the minRank
# call the dfs function using the node 0 and rank 0 and once the search function completes, convert the remaining edges from connDict to a list and return that as the result.
