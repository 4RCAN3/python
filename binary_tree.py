#<Binary Tree>

from collections import *

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

class Height:
    def __init__(self):
        self.h = 0

root = Node(1)
root.left = Node(2)
root.right = Node(3)

'''
           1 
         /   \ 
        2      3 
     /    \    /  \ 
   None None None None

'''

root.left.left = Node(4)

'''
           1 
       /       \ 
      2          3 
    /   \       /  \ 
   4    None  None  None 
  /  \ 
None None

'''

#Inorder traversal of tree (DFS)
def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val,end=" ")
        inOrder(root.right)

#Postorder traversal of tree (DFS)
def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val,end=" ")

#Preorder traversal of tree (DFS)
def preOrder(root):
    if root:
        print(root.val,end=" ")
        preOrder(root.left)
        preOrder(root.right)

#Levelorder traversal of tree (BFS)
def levelOrder(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while(len(queue)>0):
        node = queue.popleft()
        print(node.val,end=" ")
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

#Diameter of a tree

def calcDiameter(root, height):
    lh = Height() #height of left sub-tree
    rh = Height() #height of right sub-tree
    if root is None:
        height.h=0
        return 0
    ldiameter = calcDiameter(root.left, lh)  #diameter of left subtree
    rdiameter = calcDiameter(root.right, rh) #diameter of right subtree
    height.h = max(lh.h, rh.h)+1
    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))

def diameter(root):
    height = Height()
    return calcDiameter(root, height)

#Height/Depth of a tree

def maxDepth(node):
    if node is None:
        return 0
    else:
        ldepth = maxDepth(node.left)
        rdepth = maxDepth(node.right)
        if (ldepth>rdepth):
            return ldepth+1
        else:
            return rdepth+1

#Width of a tree

def getMaxWidth(root):
    h = height(root)
    count = [0]*h
    level = 0
    getMaxRec(root, count, level)
    return getMax(count, h)

def getMaxRec(root, count, level):
    if root is not None:
        count[level] += 1
        getMaxRec(root.left, count, level+1)
        getMaxRec(root.right, count, level+1)

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        return (lheight+1) if (lheight > rheight) else (rheight+1)

def getMax(count, n):
    max = count[0]
    for i in range (1,n):
        if (count[i] > max):
            max = count[i]
    return max

#Nodes at k distance

def kDist(root, k):
    if root is None:
        return
    if k==0:
        print(root.val)
    else:
        kDist(root.left, k-1)
        kDist(root.right, k-1)

#Ancestors of a node

def ancestor(root, target):
    if root == None:
        return False
    if root.val == target:
        return True
    if(ancestor(root.left, target) or ancestor(root.left, target)):
        print(root.val)
        return True
    return False
