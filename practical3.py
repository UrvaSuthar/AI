# Write a program to implement a Water Jug Problem using Python and to solve a Water Jug Problem by using BFS?

import time


class node:
    def __init__(self, data):
        self.x = 0
        self.y = 0
        self.parent = data

    def __repr__(self) -> str:
        return f"{self.x} {self.y}"


def operation(currentNode, rule):
    x = currentNode.x
    y = currentNode.y

    if rule == 1:
        if(x < maxJug1):
            x = maxJug1
        else:
            return node
    elif rule == 2:
        if (y < maxJug2):
            y = maxJug2
        else:
            return node

    elif rule == 3:
        if(x != 0):
            x = 0
        else:
            return node
    elif rule == 4:
        if(y != 0):
            y = 0
        else:
            return node
    elif rule == 5:
        if(x+y >= maxJug1 and y > 0):
            y = y - (maxJug1 - x)
            x = maxJug1
        else:
            return node
    elif rule == 6:
        if x+y >= maxJug2 and x > 0:
            x = x - (maxJug2 - y)
            y = maxJug2
        else:
            return node
    elif rule == 7:
        if x+y <= maxJug1 and y >= 0:
            x = x+y
            y = 0
        else:
            return node
    elif rule == 8:
        if x+y <= maxJug2 and x >= 0:
            y = x+y
            x = 0
        else:
            return node
    else:
        temp_node = node(currentNode,x,y)
        return temp_node


class BsfAlgo:
    def __init__(self):
        self.bsfq = []

    def isEmpty(self, l):
        return len(l) == 0

    def generateAllSuccessorNode(self, currentNode):
        node_list = []
        for rule in range(1, 9):
            nextNode = operation(currentNode, rule)

        if nextNode != None:
            node_list.append(nextNode)
        return node_list

    def popNode(currentNode):
        pass

    def isGoalNode(self, node, goalNode):
        return node.x == goalNode.x and node.y == goalNode.y

    def pushList(self, visitedNode):
        self.visitedNode.append(visitedNode)

    def bsfMain(self, initialNode, goalNode):
        self.bsfq.append(initialNode)
        while not self.isEmpty(self.bsfq):
            visitedNode = self.bsfq.pop(0)
            if visitedNode.x == initialNode.x and visitedNode.y == initialNode.y:
                return visitedNode
            else:
                successorNode = self.generateAllSuccessorNode(visitedNode)
                # self.isGoalNode(successorNode,goalNode)
                for node in successorNode:
                    if node not in self.visited:
                        self.pushList(node)

maxJug1 = int(input("Enter Max Value Of Jug1 : "))
maxJug2 = int(input("Enter Max Value Of Jug2 : "))

initialnode = node(None)

goalnode = node(None)
goalnode.x = int(input("Enter Goal For Jug 1 : "))

print("BFS Algorithm is running...💨")

start_time = time.time()
solutionNode = BsfAlgo().bsfMain(initialnode, goalnode)
end_time = time.time()
