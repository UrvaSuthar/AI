class node:
    def __init__(self, parent, value, childList):
        self.parent = parent
        self.value = value
        self.child = childList
        self.level = 0
        if(self.parent != None):
            self.level = self.parent.level + 1

    def addChildNode(self, childNode):
        self.child.append(childNode)

    def spaceCount(self):
        strParent = ""
        if(self.parent == None):
            strParent = str(self.parent)
        else:
            strParent = "None"
            tempNode = self.parent
            while(tempNode != None):
                strParent += ("->"+tempNode.value)
                tempNode = tempNode.parent
        return len(strParent)+1

    def __repr__(self):
        strParent = ""
        if(self.parent == None):
            strParent = str(self.parent)
        else:
            strParent = str(self.parent.value)
        strReturn = "\n"
        strReturn += " "*self.spaceCount()
        strReturn += "->"+str(self.value)+" "+' '.join(map(str, self.child))
        return strReturn


class tree:
    def __init__(self, rootnode):
        self.root = rootnode

    def insertNode(self, nodeValue, parentNode):
        node1 = node(parentNode, nodeValue, [])
        parentNode.addChildNode(node1)
        return node1

    def __repr__(self):
        return str(self.root)


tree1 = tree(node(None, "Electronics", []))
child1 = tree1.insertNode("Freeze", tree1.root)
child15 = tree1.insertNode("Godrez freeze", child1)
child16 = tree1.insertNode("LG freeze", child1)
child17 = tree1.insertNode("Samsung freeze", child1)
child2 = tree1.insertNode("Mobile", tree1.root)
child11 = tree1.insertNode("Oppo Mobile", child2)
child12 = tree1.insertNode("Samsung Mobile", child2)
child13 = tree1.insertNode("Redmi Mobile", child2)
child14 = tree1.insertNode("Realme Mobile", child2)
child3 = tree1.insertNode("Smart TV", tree1.root)
child4 = tree1.insertNode("LG Smart TV", child3)
child9 = tree1.insertNode("40 inch LG Smart TV", child4)
child10 = tree1.insertNode("50 inch LG Smart TV", child4)
child5 = tree1.insertNode("Samsung Smart TV", child3)
child6 = tree1.insertNode("Panasonic Smart TV", child3)
child7 = tree1.insertNode("Realme Smart TV", child3)
child8 = tree1.insertNode("Redmi Smart TV", child3)


print(tree1)
def bfs(searchString, rootNode):
    node = []
    f = 0
    node.append(rootNode)
    while node:
        tempNode = node.pop(0)
        if tempNode.value == searchString:
            f = 1
            return tempNode
        else:
            node.extend(tempNode.child)
    if f == 0:
        return None
def findCost(self):
    stringDisp = [self.value]
    ndd = self.parent
    while ndd.value != None:
        stringDisp.append(ndd.value)
        if ndd.parent == None:
            break
        ndd = ndd.parent
    stringDisp.reverse()
    return stringDisp


searchSTR = input("\nEnter Item: ")
print("Search Item = ", searchSTR)
breathF = bfs(searchSTR, tree1.root)
if breathF == None:
    print("Sorry we can't find this Item")
else:
    res = findCost(breathF)
    strPath = res[0]
    for i in range(1, len(res)):
        strPath += " -> " + res[i]
    print("Path: " + strPath)
    print("Path Cost: " + str(len(res) - 1))