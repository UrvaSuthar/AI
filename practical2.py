#starting date 11/01 And Ending Date 18/01
class node:
	def __init__(self,parent,value,childList):
		self.parent = parent
		self.value = value
		self.child= childList 
		self.i = 0 
		self.indent = 0
	def addChildNode(self,childNode):
		self.child.append(childNode)
		childNode.indent = self.indent + 1
	def __repr__(self):
		indent = "\t" * self.indent
		strChild = ""
		for child in self.child:
			strChild += child.__repr__()
		return f"{indent}->{self.value}\n{strChild}"
		

class tree:
	def __init__(self,rootNode):
		self.root = rootNode
	def insertNode(self,nodeValue,parentNode):
		node1 = node(parentNode,nodeValue,[])
		parentNode.addChildNode(node1)
		return node1
	def __repr__(self):
		return str(self.root)	
			
tree1 = tree(node(None,"Electronics",[]))
child1 = tree1.insertNode("Freeze",tree1.root)
child4 = tree1.insertNode("Godrez Freeze",child1)
child5 = tree1.insertNode("LG Freeze",child1)
child6 = tree1.insertNode("Samsung Freeze",child1)

child2 = tree1.insertNode("Mobile",tree1.root)
child7 = tree1.insertNode("Oppo Mobile",child2)
child10 = tree1.insertNode("Samsung Mobile",child2)
child9 = tree1.insertNode("Redmi Mobile",child2)
child8 = tree1.insertNode("Apple Mobile",child2)

child3 = tree1.insertNode("Smart Tv",tree1.root)
child11 = tree1.insertNode("LG Smart Tv",child3)
child12 = tree1.insertNode("55 inch ",child11)
child13 = tree1.insertNode("50 inch",child11)
child14 = tree1.insertNode("Samsung Smart Tv",child3)
child14 = tree1.insertNode("Realme Smart Tv",child3)
child14 = tree1.insertNode("Panasonic Smart Tv",child3)
child14 = tree1.insertNode("Redmi Smart Tv",child3)


print(tree1)
