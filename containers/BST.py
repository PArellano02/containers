'''
This file implements the Binary Search Tree data structure.
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    The BST is a superclass of BinaryTree.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''

        super().__init__()
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Thus, if you create a variable using the command BST([1,2,3])
        it's __repr__ will return "BST([1,2,3])"

        For the BST, type(self).__name__ will be the string "BST",
        but for the AVLTree, this expression will be "AVLTree".
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'


    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        are actually working.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        The current implementation has a bug:

        HINT:
        Use the _find_smallest and _find_largest functions to fix the bug.
        '''
        ret = True
        if node.left:
            if node.value >= BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        '''
        Inserts value into the BST.

        FIXME:
        Implement this function.

        HINT:
        '''
        if self.root:
            BST._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):
        if value <= node.value:
            if node.left:
                BST._insert(node.left, value)
            else:
                node.left = Node(value)
        if value >= node.value:
            if node.right:
                BST._insert(node.right, value)
            else:
                node.right = Node(value)

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.

        HINT:
        Repeatedly call the insert method.
        '''
        for x in xs:
            if self.root:
                BST._insert(self.root, x)
            else:
                self.root = Node(x)

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.

        FIXME:
        Implement this function.
        '''
        if self.root:
            return BST._find(value, self.root)
        else:
            return None

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        '''

        if value == node.value:
            return True
        if value > node.value:
            if node.right:
                return BST._find(value, node.right)
            else:
                return False
        if value < node.value:
            if node.left:
                return BST._find(value, node.left)
            else:
                return False

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''

        if not self.root:
            return None
        else:
            return BST._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):

        assert node is not None
        if not node.left:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.

        FIXME:
        Implement this function.

        HINT:
        Follow the pattern of the _find_smallest function.
        '''
        if not self.root:
            return None
        else:
            return BST._find_largest(self.root)

    @staticmethod
    def _find_largest(node):
        assert node is not None
        if node.right is None:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        '''
        Removes value from the BST.
        If value is not in the BST, it does nothing.

        FIXME:

        Implement this function.

        HINT:

        HINT:
        Use a recursive helper function.
        '''

        if self.root:
            if BST.find(self, value):
                self.root = self._remove(self.root, value)
                return self.root
            else:
                return self.root
        else:
            return self.root

    @staticmethod
    def _remove(node, value):
        if node:
            if value < node.value:
                node.left = BST._remove(node.left, value)
                return node
            if value > node.value:
                node.right = BST._remove(node.right, value)
                return node
            if value == node.value:
                if not node.right and not node.left:
                    node = None
                    return node
                if not node.left:
                    node = node.right
                    return node
                if not node.right:
                    node = node.left
                    return node
                else:
                    replacer = BST._find_smallest(node.right)
                    node.value = replacer
                    node.right = BST._remove(node.right, replacer)
                    return node
        else:
            return node

    def remove_list(self, xs):
        '''
        Given a list xs, remove each element of xs from self.

        FIXME:
        Implement this function.

        HINT:
        See the insert_list function.
        '''
        if self.root:
            for x in xs:
                self.root = BST._remove(self.root, x)
        else:
            return self.root
