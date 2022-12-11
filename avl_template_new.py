#username - idofabian
#id1      - 208604660 
#name1    - Ido Fabian
#id2      - 206170219
#name2    - Niv Sagie Tenenbaum  


"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value=""):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.rank = 1	

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left

	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node
		node.setParent(self)
		node.getParent().setHeight(node.getHeight() + 1)

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node
		node.setParent(self)
		node.getParent().setHeight(node.getHeight() + 1)

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node


	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height = h

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		if self.value == None:
			return False
		return True

	"""
	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getPredecessor(self):
		node = self.left
		while(node.right.rank != 0):
			node = node.gerLeft()
		
		while(node.right.rank != 0):
			node = node.getRight()

		return node
	
	def balanceFactor(self):
		return self.getLeft().getHeight() - self.getRight().getHeight()
	
	def leftRotate(father):
		#0      father
		#  0    rightSon
		#     0 rightGrandson
		rightSon= father.getRight()
		father_parent= father.getParent()
		father.setRight(rightSon.getLeft())
		rightSon.setLeft(father)
		if(father_parent == None):
			rightSon.setParent(None)
		else:
			father_parent.setLeft(rightSon)
		#   0        rightSon
		# 0   0  father    rightGrandson
		father.setHeight(father.left.getHeight() - father.right.getHeight())
		rightSon.setHeight(rightSon.getLeft().getHeight() - rightSon.getRight().getHeight())


	def rightRotate(father):
		#     0  father
		#   0    leftSon
		# 0     leftGrandson
		leftSon= father.getLeft()
		father_parent= father.getParent()
		father.setLeft(leftSon.getRight())
		leftSon.setRight(father)
		if(father_parent == None):
			leftSon.setParent(None)
		else:
			father_parent.setRight(leftSon)
		#   0        leftSon
		# 0   0  father    leftGrandson
		leftSon.setHeight(max(leftSon.getLeft().getHeight(), leftSon.getRight().getHeight()) + 1)
		leftSon.rank = leftSon.left.rank + leftSon.right.rank+1

"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.size = 0
		self.root = None
		self.maxnode = None

	"""sets tree max node

	@type TreeList: AVLTreeList
	@param TreeList: a TreeList
	"""

	def setMaxNode(self):
		maxnode = self.root
		while maxnode.getRight != None:
			maxnode = maxnode.getRight
		self.maxnode = maxnode
	
	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return (self.size == 0)


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the value of the i'th item in the list
	"""
	def retrieve_val_rec(self, node, i):
		
		left_son = True
		if (node.rank // 2 > i):
			next_node = node.getLeft()
		else:
			next_node = node.getRight()
			left_son = False
			
		if(left_son):
			if(((node.rank == 1) and (i == 0)) or ((node.rank == 2) and (i == 1))):
				return node.value
			elif(i == (next_node.rank - 1 - next_node.getLeft().rank)):
				return next_node.value
			else:
				return self.retrieve_val_rec(next_node, i)
				
		else:
			if(node.getLeft().rank + 1 == i):
				return next_node.value
			else:
				return self.retrieve_val_rec(next_node, i - (node.left.rank + 1))
	
	def retrieve(self, i):
		if not(0 <= i < self.size):
			return None

		
		if(self.root.getLeft().rank == i):
			return self.root.value
	
		return self.retrieve_val_rec(self.root, i)
	
	"""retrieves the node of the i'th item in the tree

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: AVLNode
	@returns: the node of the i'th item in the tree
	"""

	def retrieve_node(self, i):
		if not(0 <= i < self.size):
			return None

		if(self.root.getLeft().rank == i):
			return self.root
		
		return self.retrieve_node_rec(self.root, i)

	def retrieve_node_rec(self, node, i):
		left_son = True
		if (node.rank // 2 > i):
			next_node = node.getLeft()
		else:
			next_node = node.getRight()
			left_son = False
			
		if(left_son):
			if(((node.rank == 1) and (i == 0)) or ((node.rank == 2) and (i == 1))):
				return node
			elif(i == (next_node.rank - 1 - next_node.getLeft().rank)):
				return next_node
			else:
				return self.retrieve_node_rec(next_node, i)
				
		else:
			if(node.getLeft().rank == i):
				return node
			else:
				return self.retrieve_node_rec(next_node, i - (node.getLeft().rank + 1))

	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		insert_node = AVLNode(val)
		insert_node.setLeft(self.virtual_node(insert_node))
		insert_node.setRight(self.virtual_node(insert_node))
		insert_node.setHeight(0)
		
		if not(0 <= i <= self.size):
			return "The intended index have to be between 0 and tree size"
		
		if(self.root == None):
			self.root = insert_node
			self.maxnode = insert_node

		elif (i == self.size):
			max_node = self.maxnode
			max_node.setRight(insert_node)
		
		elif (i < self.size):
			node_a = self.retrieve_node(i)
			if (node_a.left.rank == 0):
				node_a.setLeft(insert_node)
			else:
				predecessor_node = node_a.getPredecessor()
				predecessor_node.setRight(insert_node)
		
		self.size += 1
		self.fixTree(insert_node.parent, True)

		return

	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		if not(self.empty()):
			return self.retrieve(0)
		return None

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		if not(self.empty()):
			return self.retrieve(self.size - 1)
		return None

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		return None

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return self.size - 1

	"""sort the info values of the list

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	"""
	def sort(self):
		return None

	"""permute the info values of the list 

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	"""
	def permutation(self):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return None



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return self.root

	def fixTree(self, father, insert):
		if(father == None):
			return
		balanceFactor = father.balanceFactor()
		if (-1 <= balanceFactor <= 1):
			self.fixTree(father.parent, insert)

		if balanceFactor < -1:
			if father.right.balanceFactor() == -1: #left
				father.leftRotate()
			else: #right then left
				father.right.rightRotate()
				father.leftRotate()

		elif balanceFactor > 1:
			if father.getLeft().balanceFactor() == 1: #right
				father.rightRotate()
			else: #left then right
				father.getLeft().leftRotate()
				father.rightRotate()
		
		father.setHeight(max(father.getLeft().getHeight(), father.getRight().getHeight()) + 1)
		father.rank = father.left.rank+father.right.rank+1

		
		if(father.parent == None):
			self.root = father
			return
		self.fixTree(father.parent, insert)
	
	def virtual_node(self, father):
		node = AVLNode()
		node.rank = 0
		node.parent = father
		return node