import avl_template_new as avl


avl_list = ['A', '-2', '3', '4', '20', '-13', 'abc']

avl_tree = avl.AVLTreeList()

avl_tree.insert(0, avl_list[0])
avl_list = ['B', 'c', 'd', 'e', 'f', 'g']

for i, val in enumerate(avl_list):
	avl_tree.insert(i, val)

# avl_tree.findMaxNode()