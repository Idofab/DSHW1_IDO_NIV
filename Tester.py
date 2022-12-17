import avl_template_new as avl

def print_tree(node):
	if (node.height > 0):
		print("value:",node.value, f'(Rank: {node.rank}, Height: {node.height})')
	if(node != None and node.left.rank != 0):
		print("left:", node.left.value, f'(Rank:{node.left.rank}, Height:{node.left.height})')
	if(node != None and node.right.rank != 0):
		print("right:", node.right.value, f'(Rank:{node.right.rank}, Height:{node.right.height})')
	if(node != None and node.left.rank != 0):
		print_tree(node.left)
	if(node != None and node.right.rank != 0):
		print_tree(node.right)

def build_tree(final_list, insert_list, index_order, P=True):
	
	avl_tree = avl.AVLTreeList()
	
	# Build tree - Insert test
	for i, val in enumerate(insert_list):
		avl_tree.insert(index_order[i], val)
	if P:
		print(f'----After insert final tree----')
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

	# Successor
	for i in range(len(final_list) - 1):
		if(avl_tree.retrieve_node(i).getSuccessor().value != (final_list[i+1])):
			print(f'Error in Successor test! i={i}: TreeNode value: {avl_tree.retrieve_node(i).getSuccessor().value}. List value (Real): {final_list[i+1]}.')
	print('Successor Done')

	# First and Last
	if (avl_tree.first() != final_list[0]):
		print(f'Error in First Test!: TreeNode value: {avl_tree.first()}. List value (Real): {final_list[0]}.')
	if (avl_tree.last() != final_list[-1]):
		print(f'Error in Last Test!: TreeNode value: {avl_tree.last()}. List value (Real): {final_list[-1]}.')
	print('First and Last Done')

	# Delete
	delete_list = final_list
	delete_index = [0, 5, 3]
	for i in delete_index:
		delete_list.pop(i)
		avl_tree.delete(i)
		if P:
			print(f'\n****After delete {i} tree*****')
			print_tree(avl_tree.root)

		for i in range(len(delete_list)):
			if(avl_tree.retrieve(i) != (delete_list[i])):
				print(f'Error in delete test! i={i}: TreeNode value: {avl_tree.retrieve(i)}. List value (Real): {delete_list[i]}.')
	
	print(f'\n---After All delete tree---')
	print_tree(avl_tree.root)

def checkTree():
	avl_tree = avl.AVLTreeList()

	for i in range(20):
		if i % 3 == 0:
			avl_tree.insert(avl_tree.length()//2, i)
		elif i % 3 == 1:
			avl_tree.insert(0, i)
		else:
			avl_tree.delete(avl_tree.length()//2)
		print_tree(avl_tree.root)


# build_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['G', 'F', 'E', 'D', 'C', 'B', 'A'], [0 for _ in range(7)], False)
# build_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['C', 'D', 'A', 'B', 'E', 'G', 'F'], [0, 1, 0, 1, 4, 5, 5], True)
# build_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G'], ['C', 'A', 'B', 'E', 'D', 'G', 'F'], [0, 0, 1, 3, 3, 5, 5], False)
# build_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], ['F', 'H', 'G', 'E', 'A', 'B', 'C', 'D'], [0, 1, 1, 0, 0, 1, 2, 3], False)
checkTree()
print("---Finish----")
