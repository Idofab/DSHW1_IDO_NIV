import avl_template_new as avl
import random
import time
import datetime
from collections import deque

def q1():
	ans_list = []
	for i in [0, 1, 6]:
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
				print(f'i = {i+1}, a - {j/K*100}% - {datetime.datetime.now()}')
		
		#b
		b_rotation_cnt = 0
		for j in range(K):
			rand_ind = random.randint(0, a_tree.length() - 1)
			temp = a_tree.delete(rand_ind)
			b_rotation_cnt += temp
			if((j/K * 100) % 1 == 0):
				print(f'i = {i+1}, b - {j/K*100}% - {datetime.datetime.now()}')
		#c
		c_tree = avl.AVLTreeList()
		c_rotation_cnt = 0
		for j in range(K // 2):
			rand_ind = random.randint(0, c_tree.length())
			temp = c_tree.insert(rand_ind, j)
			c_rotation_cnt += temp
			if((j/K * 100) % 1 == 0):
				print(f'i = {i+1}, c1 - {j/(K//2)*100}% - {datetime.datetime.now()}')

		for j in range(K // 4):
			del_ins = random.randint(0, 1)
			if del_ins == 1:
				rand_ind = random.randint(0, c_tree.length())
				temp = c_tree.insert(rand_ind, j)
			else:
				rand_ind = random.randint(0, c_tree.length() - 1)
				temp = c_tree.delete(rand_ind)
			if((j/K * 100) % 1 == 0):
				print(f'i = {i+1}, c2 - {j/(K//4)*100}% - {datetime.datetime.now()}')
			c_rotation_cnt += temp
		
		ans_list.append((a_rotation_cnt, b_rotation_cnt, c_rotation_cnt))
		print(f'K={K}\na - Insert: {a_rotation_cnt}\nb - Delete: {b_rotation_cnt}\nc - both: {c_rotation_cnt}')
		end = time.time()
		print(f'Total time running: {end - start}')

	return ans_list
def q2():
	for i in range(10):
		K = 1500 * i


	return
##main##
print(q1())