""" Basic BST code for inserting (i.e. building) and printing a tree

    Your ***second standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the STD_2 task sheet for Week 5. 

    Your ***first advanced viva task*** (of 3) will be to implement a remove (delete) method
    into the class Binary Tree from partial pseudocode. See the ADV_1 task sheet for Week 5.

    Since the given code is in python it is strongly suggested you stay with python; but
    if you want to reimplement as C++ this is also OK (see the lab sheet guidance). 
"""

import math

""" Node class
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

""" BST class with insert and display methods. display pretty prints the tree
"""

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def find_i(self, target):                   #This function takes target as input, returns a boolean indicating if target is in BST or not.
        cur_node = self.root                    #set cur_node to tree root
        while cur_node != None:                 #loop through bst if root is not null
            if cur_node.data == target:         #if object attribute (data) is target
                print('True')                   #for checking purposes 
                return True
            elif cur_node.data > target:        #if target is less than current node, make current node = left node
                cur_node = cur_node.left        #make current node the node on the left. (go down left on tree)
            else:                               #if target is not root and not less than current node (target is more than current node)
                cur_node = cur_node.right       #current node is the node on the right (go down right on tree)
        print('False')                          #for checking purposes
        return False                            #return false if while not executed tree.root is null

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)

    def _display(self, cur_node):
        
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def find_r(self, target):                       #This recursive function takes target as input returns a boolean indicating weather target is found in tree or not 
        if self.root:                               #
            if self._find_r(target, self.root):     #
                return True
            return False
        else:
            print('none')
            return None
        
    def _find_r(self, target, cur_node):
        if target > cur_node.data and cur_node.right:
            return self._find_r(target, cur_node.right)
        elif target < cur_node.data and cur_node.left:
            return self._find_r(target, cur_node.left)
        if target == cur_node.data:
            return True 
        
    def remove(self, target):                                           #function remove takes target and removes it from BST
        if self.root is None:                                           #if no tree
            return False
        elif self.root.data == target:                                  #if root is target
            if self.root.left is None and self.root.right is None:      #if target has no children
                self.root = None                                        #set node to none
            elif self.root.left and self.root.right is None:            #if target has left child but no right child
                self.root = self.root.left                              #set the root to left child
            elif self.root.left is None and self.root.right:            #if target has no left children but right children
                self.root = self.root.right                             #set root as right child
            elif self.root.left and self.root.right:                    #if target has left and right children
                parent = None                                           ##set parent/target to none
        node = self.root                                                #set node as root
        while node and node.data != target:                             #while there is a node and node data is not target
            parent = node                                               #set parent to node
            if target < node.data:                                      #if target is less than node data (parent data)
                node = node.left                                        #go left
            elif target > node.data:                                    #if target is more than parent
                node = node.right                                       #go right
        if node is None or node.data != target:                         ##CASE 1: Target not found
            return False
        elif node.left is None and node.right is None:                  ##CASE 2: Target has no children
            if target < parent.data:                                    #target is less than parent
                parent.left = None                                      #set parent’s left child to none
            else:
                parent.right = None                                     #else set right child to none
            return True
        elif node.left and node.right is None:                          #CASE 3: Target has left child only
            if target < parent.data:                                    #if target is more than parent
                parent.left = node.left                                 #set left child as parent
            else:
                parent.right = node.left                                #set right child as parent
            return True
            
        elif node.left is None and node.right:                          #CASE 4: TARGET HAS RIGHT CHILD ONLY
            if target > parent.data:                                    #target is greater than parent
                parent.right = node.right                               #move nodes to the right of target to be parent (target's node)
            else:
                parent.right = node.left                                #else move nodes to the left of target to be parent
            return True
            
        else:                                                           #CASE 5: Target has right and left children
            if node.left and node.right:                                #called if delete node whether root or otherwise
                delNodeParent = node                                    #set current node as delNode Parent                    

                while delNode.left:                                     #while there are left children to right child
                    delNodeParent = delNode                             #set current node as parent
                    delNode = delNode.left                              #set current node as left child
                node.data = delNode.data                                #pass the value of node data to current node data
                if delNode.right:                                       #if current node has right child
                    if delNodeParent.data > delNode.data:               #if current node parent data is more than current node data            
                        delNodeParent.left = delNode.right              #set left child as current node right child
                    else:
                        delNodeParent.right = delNode.right             #else set right child as current node right child
                else:
                    if delNode.data < delNodeParent.data:               #if current node data is less than parent data
                        delNodeParent.left = None                       #set parent left child to none
                    else:
                        delNodeParent.right = None                      #otherwise, set parent right child to none
            
                


#example calls, which construct and display the tree       
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(0)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
bst.insert(9)
bst.insert(10)
bst.insert(11)
bst.insert(12)
bst.insert(13)
bst.insert(14)
bst.insert(15)
bst.insert(100)
bst.insert(200)

#print("find_i(13):")
#bst.find_i(13)
#print("find_r(1000):")
#r = bst.find_r(1000)
#print(r)
print("remove(13):")
bst.remove(13)
bst.display(bst.root)
