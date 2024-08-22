from datetime import time, datetime
import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()

    def builGraph(self, year):
        self._countries = DAO.getAllCountries(year)
        self._idMap = {}
        for c in self._countries:
            self._idMap[c.CCode] = c

        self._graph.clear()
        borders = DAO.getCountryPairs(self._idMap, year)
        self._graph.add_nodes_from(self._countries)
        for b in borders:
            self._graph.add_edge(b.c1, b.c2)

    def getNodes(self):
        return list(self._graph.nodes)

    def getNumConfinanti(self, v):
        return len(list(self._graph.neighbors(v)))

    def getNumCompConnesse(self):
        return nx.number_connected_components(self._graph)

    def getRaggiungibili(self, n):
        tic = datetime.now()
        a = self.getRaggiungibiliDFS(n)
        print (f"DFS: {datetime.now()-tic} - {len(a)}")

        tic = datetime.now()
        b = self.getRaggiungibiliBFS(n)
        print(f"BFS: {datetime.now() - tic} - {len(b)}")

        tic = datetime.now()
        c= self.getRaggiungibiliIterative(n)
        print(f"Iterative: {datetime.now() - tic} - {len(c)}")

        tic = datetime.now()
        d = self.getRaggiungibiliRecursive(n)
        print(f"Recursive: {datetime.now() - tic} - {len(d)}")

        return a



    def getRaggiungibiliDFS(self, n):
        tree = nx.dfs_tree(self._graph, n) #solo archi dell'albero e archi all'indietro
        a = list(tree.nodes)
        a.remove(n)
        return a

    def getRaggiungibiliBFS(self, n):
        tree = nx.bfs_tree(self._graph, n) #archi dell'albero e archi trasversali
        a = list(tree.nodes)
        a.remove(n)
        return a

    #dfs(G)=bfs(G) solo se contengono solo archi dell'albero di visita e quindi g è esso stesso un albero

    def getRaggiungibiliIterative(self, n):
        from collections import deque

        visited = []
        toBeVisited = deque()

        visited.append(n)

        toBeVisited.extend(self._graph.neighbors(n))

        while toBeVisited:
            temp = toBeVisited.popleft()
            visited.append(temp)

            neighbors =list(self._graph.neighbors(temp))

            neighbors = [neighbor for neighbor in neighbors if neighbor not in visited]

            neighbors = [neighbor for neighbor in neighbors if neighbor not in toBeVisited]

            toBeVisited.extend(neighbors)

        visited.remove(n)
        return  visited

    def getRaggiungibiliRecursive(self, n):
        visited = []
        self._recursive_visit(n, visited)
        visited.remove(n)
        return visited

    def _recursive_visit(self, n, visited):
        visited.append(n)

        for c in self._graph.neighbors(n):
            if c not in visited:
                self._recursive_visit(c, visited)
