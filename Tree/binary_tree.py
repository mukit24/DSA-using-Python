#      2
#     / \
#    4   5
# construct the binary tree

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def __str__(self):
        return f'Node key is {self.key}'

node0 = TreeNode(2)
node1 = TreeNode(4)
node2 = TreeNode(5)

node0.left = node1
node0.right = node2

# print(node0.left.key)

# (left, key, right)
# ((1,3,None),2,((None,3,4),5,(6,7,8))) construct this tree

def parseTuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parseTuple(data[0])
        node.right = parseTuple(data[2])
    elif data == None:
        node = None
    else:
        node = TreeNode(data)
    # print('node--',node)
    return node

myNode = parseTuple(((1,3,None),2,((None,3,4),5,(6,7,8))))

# print(myNode.right.left)

def tree_to_tuple(data):
    # print(data)
    listTree = []
    if isinstance(data, TreeNode) and (data.left or data.right):
        listTree.insert(1, data.key)
        listTree.insert(0, tree_to_tuple(data.left))
        listTree.insert(2, tree_to_tuple(data.right))
        listTree = tuple(listTree)
    elif data == None:
        listTree = None
    else:
        listTree = data.key
    return listTree

# print(tree_to_tuple(myNode))

# height of a binary tree
def height(node):
    if not node:
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))

print(height(myNode))

# size of a binary tree
def treeSize(node):
    if not node:
        return 0
    else:
        return 1 + treeSize(node.left)+treeSize(node.right)

print(treeSize(myNode))
