import avl_template_new as avl
import random

def print_tree(node):
	if node is None:
		print("Empty tree!")
		return
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

def q1():
	ans_list = []
	for i in range(2):
		print(f'================i = {i + 1}===============')
		K = 1500 * (2 ** (i+1))
		
		#a
		a_tree = avl.AVLTreeList()
		a_rotation_cnt = 0
		for j in range(K):
			rand_ind = random.randint(0, a_tree.length())
			temp = a_tree.insert(rand_ind, j)
			a_rotation_cnt += temp
			if((j/K * 100) % 1 == 0):
				print(f'i = {i+1}, a - {j/K*100}%')
		
		#b
		b_rotation_cnt = 0
		for j in range(K):
			rand_ind = random.randint(0, a_tree.length() - 1)
			temp = a_tree.delete(rand_ind)
			b_rotation_cnt += temp
			if((j/K * 100) % 1 == 0):
				print(f'i = {i+1}, b - {j/K*100}%')
		#c
		c_tree = avl.AVLTreeList()
		c_rotation_cnt = 0
		for j in range(K // 2):
			rand_ind = random.randint(0, c_tree.length())
			temp = c_tree.insert(rand_ind, j)
			c_rotation_cnt += temp
			if((j/K * 100) % 1 == 0):
				print(f'i = {i+1}, c1 - {j/(K//2)*100}%')

		for j in range(K // 4):
			del_ins = random.randint(0, 1)
			if del_ins == 1:
				rand_ind = random.randint(0, c_tree.length())
				temp = c_tree.insert(rand_ind, j)
			else:
				rand_ind = random.randint(0, c_tree.length() - 1)
				temp = c_tree.delete(rand_ind)
			if((j/K * 100) % 1 == 0):
				print(f'i = {i+1}, c2 - {j/(K//4)*100}%')
			c_rotation_cnt += temp
		
		ans_list.append((a_rotation_cnt, b_rotation_cnt, c_rotation_cnt))
		print(f'K={K}\na - Insert: {a_rotation_cnt}\nb - Delete: {b_rotation_cnt}\nc - both: {c_rotation_cnt}')
	return ans_list
##main##
print(q1())