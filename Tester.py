import avl_template_new as avl


avl_list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

avl_tree = avl.AVLTreeList()

avl_tree.insert(0, 'G')
avl_list = ['A', 'B', 'C', 'D', 'E', 'F']
# Build tree - Insert test
for i, val in enumerate(avl_list):
	avl_tree.insert(i, val)

# Retrive test
for i in range(len(avl_list1)):
	if(avl_tree.retrieve(i) != (avl_list1[i])):
		print(f'Error in retrieve test! i={i}: TreeNode value: {avl_tree.retrieve(i)}. List value (Real): {avl_list1[i]}.')

# First and Last
if (avl_tree.first() != avl_list1[0]):
	print(f'Error in First Test!: TreeNode value: {avl_tree.first()}. List value (Real): {avl_list1[0]}.')
if (avl_tree.first() != avl_list1[0]):
	print(f'Error in Last Test!: TreeNode value: {avl_tree.last()}. List value (Real): {avl_list1[-1]}.')
print(f'Last: {avl_tree.last()}')

print("Finish")
