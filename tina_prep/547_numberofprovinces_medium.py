class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        connected = set()

        def dfs(node):
            for neighbor, adjacent in enumerate(isConnected[node]):
                if adjacent and neighbor not in connected:
                    connected.add(neighbor)
                    dfs(neighbor)

        provinces = 0
        for i in range(n):
            if i not in connected:
                dfs(i)
                provinces += 1
        return provinces


# From some source, we can visit every connected node to it with a simple DFS.  Seen will keep track of nodes that have been visited.
# For every node, we can visit every node connected to it with this DFS, and increment our answer as that represents one connected component.

# Input: nxn matrix isConnected where isConnected[i][j] means that the ith city and the jth city are directly connected.
# Basically this means that any row or column with an isConnected is then indirectly connected as well.
# Thus, our problem becomes one of traversing from topleft to bottomright, looking for 1s, and then scanning across horizontally and vertically for other 1s for indirect connections, and marking that as 1.
