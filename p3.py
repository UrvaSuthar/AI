# write a python code to solve water jug problem using node class and use dfs and bfs algo for it
import time

class node:
	def __init__(self, data, x=0, y=0):
		self.parent = data
		self.x = x
		self.y = y	
	def __repr__(self):
		return f"({self.x},{self.y})"

def operation(cnode, rule):
	x = cnode.x
	y = cnode.y

	if rule == 1:
		if x< maxJug1:
			x = maxJug1
		else:
			return None
	elif rule == 2:
		if y< maxJug2:
			y = maxJug2
		else:
			return None
	elif rule == 3:
		if x> 0:
			x = 0
		else:
			return None
	elif rule == 4:
		if y> 0:
			y = 0
		else:
			return None
	elif rule == 5:
		if (0< x+y <= maxJug1) and y> 0:
			x = maxJug1
			y = y - (maxJug1 - x)
		else:
			return None
	elif rule == 6:
		if (0< x+y <= maxJug2) and x> 0:
			x = x - (maxJug2 - y)
			y = maxJug2
		else:
			return None
	elif rule == 7:
		if 0< x+y <= maxJug1 and y>= 0:
			x = x + y
			y = 0
		else:
			return None
	elif rule == 8:
		if 0< x + y <= maxJug2 and x>= 0:
			x = 0
			y = x + y
		else:
			return None
	else:
		print("Rule Not Found.")
	temp_node = node(cnode, x, y)
	return temp_node

class BfsAlgo():
	def __init__(self):
		self.bfs_queue = []

	def is_empty(self):
		return len(self.bfs_queue) == 0

	def generateallnode(self, cnode):
		temp_list = []
		for rule in range(1, 9):
			temp_node = operation(cnode, rule)
			if temp_node is not None:
				temp_list.append(temp_node)
		return temp_list

	def bfs(self, start_node, goal):
		self.bfs_queue.append(start_node)
		while not self.is_empty():
			cnode = self.bfs_queue.pop(0)
			if cnode.x == goal[0] and cnode.y == goal[1]:
				return cnode
			else:
				temp_list = self.generateallnode(cnode)
				for node in temp_list:
					self.bfs_queue.append(node)
		return None

class DfsAlgo():
	def __init__(self):
		self.dfs_stack = []

	def is_empty(self):
		return len(self.dfs_stack) == 0

	def generateallnode(self, cnode):
		temp_list = []
		for rule in range(1, 9):
			temp_node = operation(cnode, rule)
			if temp_node is not None:
				temp_list.append(temp_node)
		return temp_list

	def dfs(self, start_node, goal):
		self.dfs_stack.append(start_node)
		while not self.is_empty():
			cnode = self.dfs_stack.pop()
			if cnode.x == goal[0] and cnode.y == goal[1]:
				return cnode
			else:
				temp_list = self.generateallnode(cnode)
				for node in temp_list:
					self.dfs_stack.append(node)
		return None

def print_path(cnode):
	if cnode.parent is None:
		print(cnode)
	else:
		print_path(cnode.parent)
		print(cnode)

def main():
	global maxJug1, maxJug2
	maxJug1 = int(input("Enter the max capacity of jug1: "))
	maxJug2 = int(input("Enter the max capacity of jug2: "))
	start_node = node(None, 0, 0)
	goal = (int(input("Enter the goal state of jug1: ")), int(input("Enter the goal state of jug2: ")))
	print("BFS:")
	start_time = time.time()
	bfs = BfsAlgo()
	bfs_node = bfs.bfs(start_node, goal)
	print_path(bfs_node)
	print("Time taken: ", time.time() - start_time)
	print("DFS:")
	start_time = time.time()
	dfs = DfsAlgo()
	dfs_node = dfs.dfs(start_node, goal)
	print_path(dfs_node)
	print("Time taken: ", time.time() - start_time)
	
main()
	