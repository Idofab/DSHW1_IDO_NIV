import avl_template_new as avl

def print_tree(node):
	if (node.height > 0):
		print("value:",node.value)
	if(node != None and node.left.rank != 0):
		print("left:", node.left.value)
	if(node != None and node.right.rank != 0):
		print("right:", node.right.value)
	if(node != None and node.left.rank != 0):
		print_tree(node.left)
	if(node != None and node.right.rank != 0):
		print_tree(node.right)
avl_list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

avl_tree = avl.AVLTreeList()

avl_tree.insert(0, 'G')
avl_list = ['A', 'B', 'C', 'D', 'E', 'F']

# Build tree - Insert test
for i, val in enumerate(avl_list):
	# print_tree(avl_tree.root)
	print(i , "--------------------------------------")
	avl_tree.insert(0, val)

print_tree(avl_tree.root)

# Retrive test
for i in range(len(avl_list1)):
	if(avl_tree.retrieve(i) != (avl_list1[i])):
		print(f'Error in retrieve test! i={i}: TreeNode value: {avl_tree.retrieve(i)}. List value (Real): {avl_list1[i]}.')
# Predecessor
for i in range(len(avl_list1) - 1):
	if(avl_tree.retrieve_node(i+1).getPredecessor().value != (avl_list1[i])):
		print(f'Error in Predeccessor test! i={i+1}: TreeNode value: {avl_tree.retrieve_node(i+1).getPredecessor().value}. List value (Real): {avl_list1[i]}.')

# First and Last
if (avl_tree.first() != avl_list1[0]):
	print(f'Error in First Test!: TreeNode value: {avl_tree.first()}. List value (Real): {avl_list1[0]}.')
if (avl_tree.last() != avl_list1[-1]):
	print(f'Error in Last Test!: TreeNode value: {avl_tree.last()}. List value (Real): {avl_list1[-1]}.')

print("---Finish----")
