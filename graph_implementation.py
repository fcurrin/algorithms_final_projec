class Graph:
	def __init__(self, nodes):
		self.nodes = nodes
		
class GraphNode:
	def __init__(self, index, name, adj_edges):
		self.index = index
		self.name = name
		self.adj_edges = adj_edges
		
	def getIndex(self):
		return self.index
		
	def setIndex(self, index):
		self.index = index
		
	def getName(self):
		return self.name
		
	def setName(self, name):
		self.name = name
		
	def firstEdge(self):
		return adj_edges
		
	def addEdge(self, destination):
		adj_edges = GraphEdge(destination, adj_edges)
		
class GraphEdge:
	def __init__(self, destination, next):
		self.destination = destination
		self.next = next
	
	def getNext(self):
		return self.next
		
	def getDestination(self):
		return self.destination