💻 Strongly Connected Components (SCC) and Single-Source Shortest Path (SSSP) Algorithms

💡 Kosaraju's Algorithm (for SCC)
Kosaraju’s algorithm is a well-known method for finding strongly connected components (SCCs) in a directed graph. The algorithm consists of two main steps:
Perform a Depth-First Search (DFS) on the original graph to get the finish times of the nodes.
Transpose (reverse) the graph and perform DFS again, in the order of nodes determined by the finish time stack from the first DFS. Each DFS tree formed during this second DFS corresponds to an SCC.

💡 Tarjan's Algorithm (for SCC)
Tarjan's algorithm also identifies strongly connected components in a directed graph. It uses a single DFS traversal to identify SCCs, utilizing two arrays (id[] and low_link[]) to track the discovery time and the lowest reachable node from each node. Nodes are added to a stack during DFS, and once an SCC is identified (when the current node's ID equals its low-link value), nodes are popped from the stack to form that SCC.

💡 Dijkstra's Algorithm (for SSSP)
Dijkstra's algorithm is a classic algorithm for finding the shortest paths from a single source node to all other nodes in a weighted graph. It uses a priority queue (min-heap) to always expand the node with the smallest known distance.


1️⃣ Kosaraju’s algorithm requires two passes of DFS and a graph transpose, while Tarjan’s algorithm works in a single pass.
2️⃣ Dijkstra’s Algorithm assumes all edge weights are non-negative.
