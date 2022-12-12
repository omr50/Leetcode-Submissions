"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}
        if not node:
            return None
        def clone(node):
            if node not in hashmap:
                hashmap[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in hashmap:
                    cloneNeighbor = clone(neighbor)
                    hashmap[node].neighbors.append(cloneNeighbor)
                else:
                    hashmap[node].neighbors.append(hashmap[neighbor])
            return hashmap[node]
        return clone(node)