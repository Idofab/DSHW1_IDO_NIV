import avl_template_new as avl


avl_list = ['1', '-2', '3', '4', '20', '-13', 'abc']
avl_nodes = []
for i in range(len(avl_list)):
	avl_nodes.append(avl.AVLNode((i, avl_list[i])))

avl_tree = avl.AVLTreeList()

for i, node in enumerate(avl_list):
	avl_tree.insert(i, node)

avl_tree.findMaxNode()