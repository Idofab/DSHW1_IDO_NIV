import avl_template_new as avl


avl_list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

avl_tree = avl.AVLTreeList()

avl_tree.insert(0, 'G')
avl_list = ['A', 'B', 'C', 'D', 'E', 'F']

for i, val in enumerate(avl_list):
	# print(avl_tree.retrieve(i))
	avl_tree.insert(i, val)

for i in range(7):
	print(f'{i} tree: {avl_tree.retrieve(i)}. Real: {avl_list1[i]}')
print(avl_tree.first())
print(avl_tree.last())

print("Done")
