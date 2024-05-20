#      2
#     / \
#    4   5
# construct the binary tree

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = 0
        self.right = 0
    
    def __str__(self):
        return f'Node key is {self.key}'

node0 = TreeNode(2)
node1 = TreeNode(4)
node2 = TreeNode(5)

node0.left = node1
node0.right = node2

# print(node0)

# (left, key, right)
# ((1,3,0),2,((0,3,4),5,(6,7,8))) construct this tree

def parseTuple(data):
    print(data)
    if isinstance(data, tuple) and len(data) == 3:
        
        node = TreeNode(data[1])
        print('node', node)
        node.left = parseTuple(data[0])
        print('left', node.left.key)
        node.right = parseTuple(data[2])
    elif data == 0:
        node = 0
    else:
        node = TreeNode(data)
    return node

parseTuple(((1,3,None),2,((None,3,4),5,(6,7,8))))