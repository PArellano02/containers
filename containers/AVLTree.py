'''
This file implements thiiiiiiiiiiie AVL Tree data structure.
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        '''

        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''

        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        if not node:
            return True
        else:
            right_satisfy = AVLTree._is_avl_satisfied(node.right)
            left_satisfy = AVLTree._is_avl_satisfied(node.left)
        return right_satisfy and left_satisfy

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        however, so you will have to adapt their code.
        '''
        '''
        initial_node = node
        if node.right:
            new_node = node.right
            initial_node.right = new_node.left
            new_node.left = initial_node
            node = new_node
        return node
        '''

        initial_node = node
        if node.right:
            new_node = Node(node.right.value)
            new_node.left = Node(initial_node.value)
            new_node.right = initial_node.right.right
            new_node.left.left = initial_node.left
            new_node.left.right = initial_node.right.left
            node = new_node
        return node

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        however, so you will have to adapt their code.
        '''
        '''
        initial_node = node
        if node.left:
            new_node = node.left
            initial_node.left = new_node.right
            new_node.right = initial_node
            node = new_node
        return node
        '''
        initial_node = node
        if node.left:
            new_node = Node(node.left.value)
            new_node.right = Node(initial_node.value)
            new_node.left = initial_node.left.left
            new_node.right.right = initial_node.right
            new_node.right.left = initial_node.left.right
            node = new_node
        return node

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        and the textbook provides full python code.
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            self.root = AVLTree._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):

        if not node:
            return Node(value)
        if value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
        if AVLTree._balance_factor(node) > 1:
            if value < node.left.value:
                return AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
        if AVLTree._balance_factor(node) < -1:
            if value > node.right.value:
                return AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
        return node

        """
        if not node:
            return Node(value)
        if value < node.value:
            if node.left:
                AVLTree._insert(node.left, value)
            else:
                node.left = Node(value)
                AVLTree._rebalance(node)
        if value >= node.value:
            if node.right:
                AVLTree._insert(node.right, value)
                AVLtree._rebalance
            else:
                node.right = Node(value)
                AVLTree._rebalance(node)
        """

    def insert_list(self, xs):
        for x in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, x)
            else:
                self.root = Node(x)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''

        print('got into _rebalance')
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
            else:
                node = AVLTree._left_rotate(node)
        if AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
            else:
                node = AVLTree._right_rotate(node)
        return node
        """
        if node:
            if AVLTree._balance_factor(node) >= 2:
                if AVLTree._balance_factor(node.left) >= 0:
                    AVLTree._right_rotate(node)

            if AVLTree._balance_factor(node) <= -2:
                if AVLTree._balance_factor(node.right) <= 0:
                    AVLTree._left_rotate(node)
            else:
                AVLTree._rebalance(node.left)
                AVLTree._rebalance(node.right)
        """
