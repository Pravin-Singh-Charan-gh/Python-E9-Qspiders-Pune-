# Insertion, Deletion, Searching, Traversal(preorder, postorder, inorder, level-order), height of tree, 

from collections import deque

class Node:
    """Represents a single node in a binary tree"""
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Binary_Tree:
    """Implements a Common Binary Tree Operations"""
    def __init__(self):
        self.root = None

    def insert(self,val):
        """Insert a Value into Binary Tree"""
        new_node = Node(val)

        if self.root == None:
            self.root=new_node
            return

        q = deque()
        q.append(self.root)

        while len(q):
            node = q.popleft()
            if node.left == None:
                node.left = new_node
                return
            elif node.right == None:
                node.right = new_node
                return
            q.append(node.left)
            q.append(node.right)

    def search(self,key):
        """Search a value in a binary tree"""
        if self.root == None:
            return False

        q = deque()
        q.append(self.root)

        while q:
            node = q.popleft()

            if node.val == key:
                return True

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False

    def preorder(self):
        """Returns List of Preorder traversal of binary Tree"""
        result = []

        def traverse(node):
            if not node:
                return
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        return result

    def inorder(self):
        """Returns List of Inorder Traversal of a binary Tree"""
        result = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

        traverse(self.root)
        return result

    def postorder(self):
        """Returns List of Postorder Traversal of a binary Tree"""
        result = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)
            traverse(node.right)
            result.append(node.val)

        traverse(self.root)
        return result

    def levelorder(self):
        """Returns List of Level Order traversal of Tree"""
        result = []

        if not self.root:
            return result

        q = deque()
        q.append(self.root)

        while q:
            node = q.popleft()

            result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return result

    def size(self):
        """Returns the size of a binary tree"""
        def traverse(node):
            if not node:
                return 0
            return traverse(node.left) + 1 + traverse(node.right)
        return traverse(self.root)

    def height(self):
        """Returns the height of binary tree"""
        def traverse(node):
            if node is None:
                return 0
            ans = max( traverse(node.left), traverse(node.right))
            if node!= self.root:
                ans= ans+1
            return ans
        return traverse(self.root)

    def count_leaves(self):
        """Returns the number of leaf nodes in a binary tree"""
        def traverse(node):
            if node is None:
                return 0
            if node.left==node.right==None:
                return 1
            return traverse(node.left)+traverse(node.right)
        return traverse(self.root)

    def isEmpty(self):
        """It check whether the binary tree is empty or not"""
        return self.root == None

    def minimum_value(self):
        """It returns the minimum value is a binary tree"""

        if self.root is None:
            return None 
        
        mini = float('inf')
        q = deque()
        q.append(self.root)

        while q:
            node = q.popleft()
            if node.val<mini:
                mini = node.val

            if node.left:q.append(node.left)
            if node.right:q.append(node.right)
        return mini

    
    def maximum_value(self):
        """It returns the maximum value is a binary tree"""

        if self.root is None:
            return None 
         
        maxi = -float('inf')
        q = deque()
        q.append(self.root)

        while q:
            node = q.popleft()
            if node.val>maxi:
                maxi = node.val

            if node.left:q.append(node.left)
            if node.right:q.append(node.right)
            
        return maxi

    def display(self):
        """It prints the binary tree in level order manner"""
        if self.root is None:
            print(None)

        q = deque()
        q.append(self.root)
        q.append('level')

        while q:
            res = []
            while q[0] != 'end':
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

                res.append(node.val)

            q.popleft()
            q.append('end')

            print(' '.join(res))

    # def delete(self,data):
    #     if self.root == None:
    #         return False
        
    #     if self.root.val == data:
    #         prev = self.root

    #     def previous(node):
