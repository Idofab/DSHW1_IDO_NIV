import avl_template_new as avl
import random
import time
import datetime
import LinkedList as ll

def q1():
	ans_list = []
	for i in range(10):
		print(f'================i = {i + 1}===============')
		print(f'Starting time {datetime.datetime.now()}')
		start = time.time()
		K = 1500 * (2 ** (i+1))
		
		#a
		a_tree = avl.AVLTreeList()
		a_rotation_cnt = 0
		for j in range(K):
			rand_ind = random.randint(0, a_tree.length())
			temp = a_tree.insert(rand_ind, j)
			a_rotation_cnt += temp
			if((j/K * 100) % 1 == 0):
				print(f'{i+1}a - {j/K*100}% - {datetime.datetime.now()}')
		
		#b
		b_rotation_cnt = 0
		for j in range(K):
			rand_ind = random.randint(0, a_tree.length() - 1)
			temp = a_tree.delete(rand_ind)
			b_rotation_cnt += temp
			if((j/K * 100) % 1 == 0):
				print(f'{i+1}b - {j/K*100}% - {datetime.datetime.now()}')
		#c
		c_tree = avl.AVLTreeList()
		c1_rotation_cnt = 0
		c2_rotation_cnt = 0
		for j in range(K // 2):
			rand_ind = random.randint(0, c_tree.length())
			temp = c_tree.insert(rand_ind, j)
			c1_rotation_cnt += temp
			if((j/K * 100) % 1 == 0):
				print(f'{i+1}c1 - {j/(K//2)*100}% - {datetime.datetime.now()}')

		for j in range(K // 4):

			rand_ind = random.randint(0, c_tree.length())
			temp = c_tree.insert(rand_ind, j)
			c2_rotation_cnt += temp

			rand_ind = random.randint(0, c_tree.length() - 1)
			temp = c_tree.delete(rand_ind)
			if((j/K * 100) % 1 == 0):
				print(f'{i+1}c2 - {j/(K//4)*100}% - {datetime.datetime.now()}')
			c2_rotation_cnt += temp
		
		ans_list.append([a_rotation_cnt, b_rotation_cnt, c1_rotation_cnt, c2_rotation_cnt])
		print(f'K={K}\na - Insert: {a_rotation_cnt}\nb - Delete: {b_rotation_cnt}\nc1 - insert: {c1_rotation_cnt}\nc2 - both: {c2_rotation_cnt}')
		end = time.time()
		print(f'Total time running: {end - start}')

	return ans_list

def insert_first():
	for i in range(10):
		K = 1500 * (i+1)
		print(f'\n================i = {i + 1}===============')
		print(f'Insert objects to first')

		########
		avl_tree = avl.AVLTreeList()
		avl_tot_time = 0
		for j in range(K):
			avl_start = time.perf_counter()
			avl_tree.insert(0, j)
			avl_end = time.perf_counter()
			avl_tot_time += (avl_end - avl_start)
		print(f"Avl tree average time: {avl_tot_time / K}")
		
		######
		linked_list = ll.LinkedList()
		ll_tot_time = 0
		for j in range(K):
			ll_start = time.perf_counter()
			linked_list.add_first(ll.Node(j))
			ll_end = time.perf_counter()
			ll_tot_time += (ll_end - ll_start)

		print(f"Linked list average time: {ll_tot_time / K}")
		
		######
		theo_list = []
		list_tot_time = 0
		for j in range(K):
			list_start = time.perf_counter()
			theo_list.insert(0, j)
			list_end = time.perf_counter()
			list_tot_time += (list_end - list_start)
		print(f"Python list average time: {list_tot_time / K}")

	return

def insert_last():
	for i in range(10):
		K = 1500 * (i+1)
		print(f'\n================i = {i + 1}===============')
		print(f'Insert objects to last')

		########
		avl_tree = avl.AVLTreeList()
		avl_tot_time = 0
		for j in range(K):
			avl_start = time.perf_counter()
			avl_tree.insert(avl_tree.length(), j)
			avl_end = time.perf_counter()
			avl_tot_time += (avl_end - avl_start)
		print(f"Avl tree average time: {avl_tot_time / K}")
		
		######
		linked_list = ll.LinkedList()
		ll_tot_time = 0
		for j in range(K):
			ll_start = time.perf_counter()
			linked_list.add_last(ll.Node(str(j)))
			ll_end = time.perf_counter()
			ll_tot_time += (ll_end - ll_start)

		print(f"Linked list average time: {ll_tot_time / K}")
		
		
		######
		theo_list = []
		list_tot_time = 0
		for j in range(K):
			list_start = time.perf_counter()
			theo_list.append(j)
			list_end = time.perf_counter()
			list_tot_time += (list_end - list_start)
		print(f"Python list average time: {list_tot_time / K}")

	return

def insert_random():
	for i in range(10):
		K = 1500 * (i+1)
		print(f'\n================i = {i + 1}===============')
		print(f'Enter objects to random')

		########
		avl_tree = avl.AVLTreeList()
		avl_tot_time = 0
		for j in range(K):
			avl_start = time.perf_counter()
			avl_tree.insert(random.randint(0, avl_tree.length()), j)
			avl_end = time.perf_counter()
			avl_tot_time += (avl_end - avl_start)
		print(f"Avl tree average time: {avl_tot_time / K}")
		
		######
		linked_list = ll.LinkedList()
		ll_tot_time = 0
		linked_list.add_first(ll.Node("0"))
		for j in range(K):
			ll_start = time.time()
			index = random.randint(0, j)
			linked_list.add_index(ll.Node(str(j)), index)
			ll_end = time.time()
			ll_tot_time += (ll_end - ll_start)

		print(f"Linked list average time: {ll_tot_time / K}")
		
		
		######
		theo_list = []
		list_tot_time = 0
		theo_list.append(0)
		for j in range(K):
			list_start = time.time()
			theo_list.insert(random.randint(0, len(theo_list) - 1), j)
			list_end = time.time()
			list_tot_time += (list_end - list_start)
		print(f"Python list average time: {list_tot_time}")
	return



ans = q1()
for i, vals in enumerate(ans):
	print(f'========={i+1}=========')
	print("a", vals[0])
	print("b", vals[1])
	print("c1", vals[2])
	print("c2", vals[3])

# res1 = insert_first()
# res2 = insert_random()
# res3 = insert_last()
