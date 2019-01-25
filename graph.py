from collections import defaultdict

class Graph(object):

    def __init__(self):
        self._graph = defaultdict(set)

    def getConnections(self, node):
        return self._graph[node]

    def addConnection(self, node1, node2):
        self._graph[node1].add(node2)
        self._graph[node2].add(node1)

    def addConnections(self, connections):
        for node1, node2 in connections:
            self.addConnection(node1, node2)

    def remove(self, node):
        for node, connections in self._graph.iteritems():
            try:
                connections.remove(node)
            except KeyError:
                pass

        try:
            del self._graph[node]
        except KeyError:
            pass

    def isConnected(self, node1, node2):
        return node1 in self._graph and node2 in self._graph[node1]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))
