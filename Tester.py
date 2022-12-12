import avl_template_new as avl

def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)

def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = str(t.value)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))
def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = left.height
    rwid = right.height
    rootwid = 1

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result

def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1

def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


avl_list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

avl_tree = avl.AVLTreeList()

avl_tree.insert(0, 'G')
avl_list = ['A', 'B', 'C', 'D', 'E', 'F']
# Build tree - Insert test
for i, val in enumerate(avl_list):
	avl_tree.insert(i, val)
printree(avl_tree.root)

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
