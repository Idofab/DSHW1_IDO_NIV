import avl_template_new as avl


avl_list1 = ['B', 'C', 'D', 'E', 'F', 'G', 'A']

avl_tree = avl.AVLTreeList()

avl_tree.insert(0, 'A')
avl_list = ['B', 'C', 'D', 'E', 'F', 'G']

for i, val in enumerate(avl_list):
	avl_tree.insert(i, val)

for i in range(7):
	print(f'{i} tree: {avl_tree.retrieve(i)}. Real: {avl_list1[i]}')
print("Done")
# avl_tree.findMaxNode()