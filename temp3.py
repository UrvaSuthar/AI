import time


class Node:
    def __init__(self, data, x=0, y=0):
        self.parent = data
        self.x = x
        self.y = y


def operation(cnode, rule):
    x = cnode.x
    y = cnode.y

    if rule == 1:
        if x < max_jug1:
            x = max_jug1
    elif rule == 2:
        if y < max_jug1:
            y = max_jug1
    elif rule == 3:
        if x > 0:
            x = 0
    elif rule == 4:
        if y > 0:
            y = 0
    elif rule == 5:
        if (0 < x+y >= max_jug1) and y > 0:
            x = max_jug1
            y = y - (max_jug1 - x)
    elif rule == 6:
        if (0 < x+y >= max_jug2) and x > 0:
            x = x - (max_jug2 - y)
            y = max_jug2
    elif rule == 7:
        if 0 < x+y <= max_jug1 and y >= 0:
            x = x + y
            y = 0
    elif rule == 8:
        if 0 < x + y <= max_jug2 and x >= 0:
            x = 0
            y = x + y
    else:
        print("Rule Not Found.")
    temp_node = Node(cnode, x, y)
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
            temp_list.append(temp_node)
        return temp_list

    def bfs_main(self, initial_node, goal_node):
        self.bfs_queue.append(initial_node)
        while not self.is_empty():
            visited_node = self.bfs_queue.pop(0)
            if visited_node.x == goal_node.x and visited_node.y == goal_node.y:
                print("Goal Node Found")
                return visited_node
            else:
                successor_node = self.generateallnode(visited_node)
            self.bfs_queue.extend(successor_node)
        return None


max_jug1 = int(input('Enter the value of Jug 1: '))
max_jug2 = int(input('Enter the value of Jug 2: '))

initialNode = Node(None)
goalNode = Node(None)

goalNode.x = int(input('Enter the value of goal in Jug 1: '))

print("BFS Algorithm is running...💨")

start_time = time.time()
solNode = BfsAlgo().bfs_main(initialNode, goalNode)
print(f"x = {solNode.x}, y = {solNode.y}")
stop_time = time.time()

print(f"BFS Algorithm took: {stop_time - start_time} ms")
print('BFS Algorithm run completed')
