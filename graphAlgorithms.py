import heapq
# SCC (Strongly Connected Components)

class Graph:
    def __init__(self):
        self.graph = {}
        self.size = 0
        
    def addEdges(self, u, v):
        if not u in self.graph:
            self.size += 1
            self.graph[u] = []
        if not v in self.graph:
            self.size += 1
            self.graph[v] = []
        self.graph[u].append(v)
        #self.graph[v].append(u)
        
    def dfs_traverse(self, visited, finishTimeStack, u):
        # print(u, end='')
        visited.add(u)
        finishTimeStack.pop()
        for v in self.graph[u]:
            if v not in visited:
                self.dfs_traverse(visited, finishTimeStack, v)
  
    def Transpose(self) -> "Graph":
        transpose = Graph()
        for u in self.graph:
            for v in self.graph[u]:
                transpose.addEdges(v, u)
        return transpose
        
    def Kosaraju(self, u):
        finishTimeStack = []
        visited = set()
        
        def finishTime(u):
            visited.add(u)
            for v in self.graph[u]:
                if v not in visited:
                    finishTime(v)
            finishTimeStack.append(u)
        finishTime(u)
        print(finishTimeStack)
        transpose = self.Transpose()
        count = 0
        visited.clear()
        while finishTimeStack:
            u = finishTimeStack[-1]
            transpose.dfs_traverse(visited, finishTimeStack, u)
            count += 1
        return count
    
    def Tarjan(self, u):
        id = self.size * [-1]
        low_link = self.size * [-1]
        onStack = set()
        stack = []
        countSCC = 0
        ID = -1
        def dfs(u):
            onStack.add(u)
            stack.append(u)
            nonlocal ID; ID += 1
            low_link[u] = id[u] = ID
            for v in self.graph[u]:
                if id[v] == -1:
                    dfs(v)
                if v in onStack:
                    low_link[u] = min(low_link[v], low_link[u])
            if id[u] == low_link[u]:
                nonlocal countSCC; countSCC += 1
                StackScc = []
                while True:
                    node = stack.pop()
                    onStack.remove(node)
                    StackScc.append(node)
                    if node == u:
                        break
                print(StackScc)
        for u in self.graph:
            if id[u] == -1:
                dfs(u)
        return countSCC
   
# SSSP (Single-Source Shortest Path) 
class WeightedGraph:
    def __init__(self):
        self.graph = {}
        self.size = 0
    def addEdges(self, u, v, weight):
        if not u in self.graph:
            self.graph[u] = []
            self.size += 1
        if not v in self.graph:
            self.graph[v] = []
            self.size += 1
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
    def Dijkstar(self, u):
        dist = [float("inf") for num in range(self.size)]
        dist[u] = 0
        prio_q = []
        heapq.heappush(prio_q, (dist[u], u))
        while prio_q:
            cost, u = heapq.heappop(prio_q)
            for v, w in self.graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(prio_q, (dist[v], v))
        print(dist)
        
        
# wgraph = WeightedGraph()
# wgraph.addEdges(0, 1, 3)
# wgraph.addEdges(0, 2, 4)
# wgraph.addEdges(0, 5, 4)
# wgraph.addEdges(1, 5, 8)
# wgraph.addEdges(1, 4, 5)
# wgraph.addEdges(2, 1, 6)
# wgraph.addEdges(2, 3, 2)
# wgraph.addEdges(2, 7, 10)
# wgraph.addEdges(3, 4, 7)
# wgraph.addEdges(3, 6, 7)
# wgraph.addEdges(4, 7, 6)
# wgraph.addEdges(5, 6, 9)
# wgraph.addEdges(6, 7, 1)
# wgraph.Dijkstar(0)

# print(wgraph.graph[2])   
# print(wgraph.size)  
            
graph = Graph()
# graph.addEdges(0, 1)
# graph.addEdges(1, 2)
# graph.addEdges(2, 5)
# graph.addEdges(5, 3)
# graph.addEdges(3, 4)
# graph.addEdges(4, 0)

graph.addEdges(0, 1)
graph.addEdges(1, 2)
graph.addEdges(2, 5)
graph.addEdges(5, 3)
graph.addEdges(3, 4)
graph.addEdges(4, 0)
visited = set() 
countSCC = graph.Kosaraju(0)
print(countSCC)

countSCC = graph.Tarjan(0)
print(countSCC)
        
        
        
