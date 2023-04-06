'''
This file implements the Heap data structure as a subclass of the BinaryTree.
'''

from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''

        super().__init__()
        self.num_nodes = 0
        if xs:
            for x in xs:
                self.insert(x)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"

        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        ret = True
        if node.left:
            ret &= node.value <= node.left.value
            ret &= Heap._is_heap_satisfied(node.left)
        if node.right:
            ret &= node.value <= node.right.value
            ret &= Heap._is_heap_satisfied(node.right)
        return ret

    def insert(self, value):
        '''
        Inserts value into the heap.

        FIXME:
        Implement this function.

        HINT:
        The pseudo code is
        '''
        self.num_nodes += 1
        binary_str = bin(self.num_nodes)[3:]
        if self.root is None:
            self.root = Node(value)
        else:
            print("self.root=", self.root)
            Heap._insert(self.root, value, binary_str)
            print("self.root22=", self.root)

    @staticmethod
    def _insert(node, value, binary_str):
        if binary_str:
            if binary_str[0] == '0':
                if len(binary_str) == 1:
                    node.left = Node(value)
                else:
                    Heap._insert(node.left, value, binary_str[1:])
                if node.value > node.left.value:
                    node.value, node.left.value = node.left.value, node.value
            if binary_str[0] == '1':
                if len(binary_str) == 1:
                    node.right = Node(value)
                else:
                    Heap._insert(node.right, value, binary_str[1:])
                if node.value > node.right.value:
                    node.value, node.right.value = node.right.value, node.value
        else:
            node = Node(value)

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.
        '''
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        '''
        if self.root:
            return self.root.value
        else:
            return 0

    def remove_min(self):
        '''
        Removes the minimum value from the Heap.
        If the heap is empty, it does nothing.

        FIXME:
        Implement this function.

        '''

        binary_str2 = bin(self.num_nodes)[3:]
        # print('test')
        # print("binary_str2=", binary_str2)
        # print("self.root=", self.root)
        if self.root:
            last_val = self._remove(self.root, binary_str2)
            # print("last_val=", last_val)
            self.num_nodes -= 1
            self.root.value = last_val
            # print("self.root22=", self.root)
            self._Reagan(self.root)

    @staticmethod
    def _remove(node, binary_str2):
        if node:
            if node.left:
                if binary_str2[0] == '0':
                    if len(binary_str2) == 1:
                        last_val = node.left.value
                        node.left = None
                        return last_val
                    else:
                        last_val = Heap._remove(node.left, binary_str2[1:])
                if binary_str2[0] == '1':
                    if len(binary_str2) == 1:
                        last_val = node.right.value
                        node.right = None
                        return last_val
                    else:
                        last_val = Heap._remove(node.right, binary_str2[1:])
                return last_val

    @staticmethod
    def _Reagan(node):
        if node:
            if node.right and node.left:
                if node.value > node.right.value < node.left.value:
                    node.value, node.right.value = node.right.value, node.value
                    Heap._Reagan(node.right)
                if node.value > node.left.value < node.right.value:
                    node.value, node.left.value = node.left.value, node.value
                    Heap._Reagan(node.left)
            if node.left:
                if node.value > node.left.value:
                    node.value, node.left.value = node.left.value, node.value
                    Heap._Reagan(node.left)
