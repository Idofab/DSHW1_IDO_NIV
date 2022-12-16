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

def build_tree(final_list, insert_list, index_order):
	avl_tree = avl.AVLTreeList()
	# Build tree - Insert test
	for i, val in enumerate(insert_list):
		avl_tree.insert(index_order[i], val)
	print(f'--final tree--')
	print_tree(avl_tree.root)

	# Retrive test
	for i in range(len(final_list)):
		if(avl_tree.retrieve(i) != (final_list[i])):
			print(f'Error in retrieve test! i={i}: TreeNode value: {avl_tree.retrieve(i)}. List value (Real): {final_list[i]}.')
	print('Retrive Done')
	
	# Predecessor
	for i in range(len(final_list) - 1):
		if(avl_tree.retrieve_node(i+1).getPredecessor().value != (final_list[i])):
			print(f'Error in Predeccessor test! i={i+1}: TreeNode value: {avl_tree.retrieve_node(i+1).getPredecessor().value}. List value (Real): {final_list[i]}.')
	print('Predecessor Done')

	# First and Last
	if (avl_tree.first() != final_list[0]):
		print(f'Error in First Test!: TreeNode value: {avl_tree.first()}. List value (Real): {final_list[0]}.')
	if (avl_tree.last() != final_list[-1]):
		print(f'Error in Last Test!: TreeNode value: {avl_tree.last()}. List value (Real): {final_list[-1]}.')
	print('First and Last Done')


build_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['G', 'F', 'E', 'D', 'C', 'B', 'A'], [0 for _ in range(7)])
build_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['C', 'D', 'A', 'B', 'E', 'G', 'F'], [0, 1, 0, 1, 4, 5, 5])
build_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['C', 'A', 'B', 'E', 'D', 'G', 'F'], [0, 0, 1, 3, 3, 5, 5])
build_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], ['F', 'H', 'G', 'E', 'A', 'B', 'C', 'D'], [0, 1, 1, 0, 0, 1, 2, 3])
print("---Finish----")
