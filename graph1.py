class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        """Add a new unconnected vertex"""
        self.vertices[vertex] = set())

    def add_edge(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
			self.vertices[v_from].add(v_to)
		else:
			raise IndexError("nonexistent vertex")

    def is_connected(self, v_from, v_to):
		if v_from in self.vertices and v_to in self.vertices:
			return v_to in self.vertices[v_from]
		else:
			raise IndexError("nonexistent vertex")
    
    def get_neighbors(self, v):
		return self.vertices[v]
​
	def bft(self, starting_vertex_id):
		q = Queue()
		visited = set()
​
		# Init:
		q.enqueue(starting_vertex_id)
​
		# While queue isn't empty
		while q.size() > 0:
​
			v = q.dequeue()
​
			if v not in visited:
				print(v)   # "Visit" the node
​
				visited.add(v)
​
				for neighbor in self.get_neighbors(v):
					q.enqueue(neighbor)
​
	def dft(self, starting_vertex_id):
		q = Stack()
		visited = set()
​
		# Init:
		q.push(starting_vertex_id)
​
		# While queue isn't empty
		while q.size() > 0:
​
			v = q.pop()
​
			if v not in visited:
				print(v)   # "Visit" the node
​
				visited.add(v)
​
				for neighbor in self.get_neighbors(v):
					q.push(neighbor)
​
	def bfs(self, starting_vertex_id, target_vertex_id):

g = Graph()
g.add_vertex(1)
g.add_vertex(2)

g.add_edge(2, 1)
