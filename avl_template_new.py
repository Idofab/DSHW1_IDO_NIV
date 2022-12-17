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
	@returns: the predecesso of self
	"""
	def getPredecessor(self):
		if(self.getParent() == None) and (self.getLeft().rank == 0):
			return None
		
		if(self.getLeft().rank != 0):
			predecessor_node = self.getLeft()
			while(predecessor_node.getRight().rank != 0):
				predecessor_node = predecessor_node.getRight()
			return predecessor_node

		elif((self.getLeft().rank == 0) and (self.getParent().getRight() == self)):
			return self.getParent()
		
		elif(self.getParent().getLeft() == self):
			predecessor_node = self.getParent()
			while((predecessor_node.getParent().getLeft() == predecessor_node)):
				predecessor_node = predecessor_node.getParent()
			return predecessor_node.getParent()
	
	def getSuccessor(self):

		if(self.getParent() == None) and (self.getRight().rank == 0):
			return None
	
		if(self.getRight().rank != 0):
			successor_node = self.getRight()
			while(successor_node.getLeft().rank != 0):
				successor_node = successor_node.getLeft()
			return successor_node

		elif((self.getRight().rank == 0) and (self.getParent().getLeft() == self)):
			return self.getParent()
		
		elif(self.getParent().getRight() == self):
			successor_node = self.getParent()
			while((successor_node.getParent().getRight() == successor_node)):
				successor_node = successor_node.getParent()
			return successor_node.getParent()
	
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
			if father_parent.getRight().value == father.value:
				father_parent.setRight(rightSon)
			else:
				father_parent.setLeft(rightSon)
		#   0        rightSon
		# 0   0  father    rightGrandson
		father.setHeight(father.left.getHeight() - father.right.getHeight())
		rightSon.setHeight(rightSon.getLeft().getHeight() - rightSon.getRight().getHeight())


	def rightRotate(father):
		#     3  father
		#   2    leftSon
		# 1     leftGrandson
		leftSon= father.getLeft()
		father_parent= father.getParent()
		father.setLeft(leftSon.getRight())
		leftSon.setRight(father)
		if(father_parent == None):
			leftSon.setParent(None)
		else:
			if father_parent.getRight().value == father.value:
				father_parent.setRight(leftSon)
			else:
				father_parent.setLeft(leftSon)
		#   2               leftSon
		# 1   3  leftGrandson     father
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
		while maxnode.getRight() != None:
			maxnode = maxnode.getRight()
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
	def retrieve(self, i):
		if not(0 <= i < self.size):
			return None

		
		if(self.root.getLeft().rank == i):
			return self.root.value
	
		return self.retrieve_node_rec(self.root, i).value
	
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
		if node.getLeft().rank == i:
			return node
		if i < node.getLeft().rank:
			return self.retrieve_node_rec(node.getLeft(), i)
		return self.retrieve_node_rec(node.getRight(), i-node.getLeft().rank-1)

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
		
		rotate_number = 0

		if not(0 <= i <= self.size):
			return None
		
		if(self.root == None):
			self.root = insert_node
			self.maxnode = insert_node

		elif (i == self.size):
			self.maxnode.setRight(insert_node)
			self.maxnode = insert_node
		
		elif (i < self.size):
			node_a = self.retrieve_node(i)
			if (node_a.getLeft().rank == 0):
				node_a.setLeft(insert_node)
			else:
				predecessor_node = node_a.getPredecessor()
				predecessor_node.setRight(insert_node)
		
		self.size += 1
		rotate_number = self.fixTree(insert_node.parent, 0)

		return rotate_number

	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		
		if not(0 <= i < self.size):
			return None
		
		if(i == 0 and self.size == 1):
			self.size = 0
			self.root = None
			self.maxnode = None
			return 0

		delete_node = self.retrieve_node(i)
		delete_node_parent = delete_node.getParent()
		delete_node_right = delete_node.getRight()
		delete_node_left = delete_node.getLeft()
		
		if(delete_node == self.maxnode):
			self.maxnode = delete_node.getPredecessor()
		
		new_first = self.retrieve(0)
		if(i == 0):
			new_first = self.retrieve_node(1)

		self.size -= 1

		# If delete node is leaf
		if((delete_node_right.rank == 0) and (delete_node_left.rank == 0)):
			if(delete_node_parent.getLeft() == delete_node):
				delete_node_parent.setLeft(self.virtual_node(delete_node_parent))
			else:
				delete_node_parent.setRight(self.virtual_node(delete_node_parent))
			
			rotation_count = self.fixTree(delete_node_parent, 0)
		
		# If delete node has only left child
		elif(delete_node_right.rank == 0):
			if(delete_node_parent.getLeft() == delete_node):
				delete_node_parent.setLeft(delete_node_left)
			else:
				delete_node_parent.setRight(delete_node_left)
			
			rotation_count = self.fixTree(delete_node_parent, 0)

		# If delete node has only right child
		elif(delete_node_left.rank == 0):
			if(delete_node_parent.getLeft() == delete_node):
				delete_node_parent.setLeft(delete_node_right)
			else:
				delete_node_parent.setRight(delete_node_right)

			rotation_count = self.fixTree(delete_node_parent, 0)
		
		# If delete node is has two children
		else:
			succesor_delete_node = delete_node.getSuccessor()
			succesor_delete_node_right = succesor_delete_node.getRight()
			succesor_delete_node_parent = succesor_delete_node.getParent()

			succesor_delete_node_parent.setLeft(succesor_delete_node_right)
			succesor_delete_node.setParent(delete_node_parent)
			succesor_delete_node.setLeft(delete_node_left)

			# Check right child of delete not the succesor 
			if not(succesor_delete_node == delete_node_right):
				succesor_delete_node.setRight(delete_node_right)
			
			else:
				succesor_delete_node.setRight(succesor_delete_node_right)


			# Update succesor parent children 
			if(delete_node_parent == None):
				self.root = succesor_delete_node
			
			else:
				if(delete_node_parent.getLeft() == delete_node):
					delete_node_parent.setLeft(succesor_delete_node)
				
				elif(delete_node_parent.getRight() == delete_node):
					delete_node_parent.setRight(succesor_delete_node)

			succesor_delete_node_parent.setHeight(max(succesor_delete_node_parent.getLeft().getHeight(), succesor_delete_node_parent.getRight().getHeight()) + 1)
			succesor_delete_node_parent.rank = succesor_delete_node_parent.getRight().rank + succesor_delete_node_parent.getLeft().rank + 1
			
			succesor_delete_node.setHeight(max(succesor_delete_node.getLeft().getHeight(), succesor_delete_node.getRight().getHeight()) + 1)
			succesor_delete_node.rank = succesor_delete_node.getRight().rank + succesor_delete_node.getLeft().rank + 1
			
			if(succesor_delete_node != new_first):
				first_rotation_count = self.fixTree(succesor_delete_node.getPredecessor(), 0)

			else:
				first_rotation_count = self.fixTree(succesor_delete_node, 0)

			if(succesor_delete_node == self.maxnode):
				rotation_count = self.fixTree(succesor_delete_node, first_rotation_count)
			else:
				rotation_count = self.fixTree(succesor_delete_node.getSuccessor(), first_rotation_count)

		return rotation_count


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
		return self.size

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

	def fixTree(self, father, counter):
		if(father == None):
			return counter
		balanceFactor = father.balanceFactor()
		if (-1 <= balanceFactor <= 1):
			father.setHeight(max(father.getLeft().getHeight(), father.getRight().getHeight()) + 1)
			father.rank = father.getLeft().rank + father.getRight().rank + 1
			self.fixTree(father.parent, counter)

		if balanceFactor < -1:
			if father.right.balanceFactor() == -1: #left
				father.leftRotate()
				counter += 1
			else: #right then left
				father.right.rightRotate()
				father.leftRotate()
				counter += 2

		elif balanceFactor > 1:
			if father.getLeft().balanceFactor() == 1: #right
				father.rightRotate()
				counter += 1
			else: #left then right
				father.getLeft().leftRotate()
				father.rightRotate()
				counter += 2
		
		father.setHeight(max(father.getLeft().getHeight(), father.getRight().getHeight()) + 1)
		father.rank = father.getLeft().rank + father.getRight().rank + 1

		
		if(father.parent == None):
			self.root = father
			return counter

		self.fixTree(father.parent, counter)
	
	def virtual_node(self, father):
		node = AVLNode()
		node.rank = 0
		node.parent = father
		return node
	
	def print_tree(self, node):
		if (node.height > 0):
			print("value:",node.value)
		if(node != None and node.left.rank != 0):
			print("left:", node.left.value)
		if(node != None and node.right.rank != 0):
			print("right:", node.right.value)
		if(node != None and node.left.rank != 0):
			self.print_tree(node.left)
		if(node != None and node.right.rank != 0):
			self.print_tree(node.right)
	
	def append(self, val):
		self.insert(self.length(), val)
	
	def getTreeHeight(self):
		return self.root.height

