import datetime as time
from TreeNode import TreeNode


class MyBinarySearchTree:
    def __init__(self, root=None):
        self._root = root
        self._size = 0

    def insert(self, new_node):
        """@params new_node to insert.
        @return success if the insert operation was successful.
        @raises ValueError if Node is None.
        Insert the element elem into the tree and return True if it was successful.
        Elements with the same key are not allowed, in this case False is returned.
        None-elements are not allowed, in this case an exception is thrown.
        """
        if new_node is None:
            raise ValueError("Node to be inserted must not be None")
        if self.find(new_node.key):
            return False
        if self._root is None:
            self._root = new_node
        else:
            self._insert_helper(self._root, new_node)
        self._size += 1
        return True


    def get_parent(self, key):
        """@param key
        @return key of parent.
        @raises ValueError if key is None.
        Search the parent node of a given key and return its key or None if not found.
        """
        if key == None:
            raise ValueError("You Donkey! Key is not None!")
        parent = None
        node = self._root

        while node.key != key:
            parent = node
            if key < node.key:
                node = node.left_node
                if node == None:
                    return None # not found in all lefts
            elif key > node.key:
                node = node.right_node
                if node == None:
                    return None # not found in all rights

        return parent.key

    def is_root(self, key):
        if key is None:
            raise ValueError("The key can't be None")
        if key == self._root.key:
            return True
        elif key != self._root.key:
            return False
        """@params key
        @return boolean
        @raises ValueError if key is None.
        Returns True if the node of any given key is the root node, else returns False.
        """
        #TODO


    def get_size(self):
        return self._size

    """@return Tree size
    returns the number of items in the tree
    """


    def find(self, key):
        """@params key
        @return The corresponding element of the node with the given key.
        @raises ValueError if key is None
        Returns the element of the node found with the given key, or None if element was not found.
        """
        # 1. key can't be empty
        if key == None:
            raise ValueError("You donkey! Key is not allowed to be None!")

        # 2. if tree is empty
        node = self._root

        if node == None:
            return
        # 3. check if the node already exists and
        # return the desired node
        else:
            while node.key != key:
                if key < node.key:
                    node = node.left_node
                    if node == None:
                        return None
                elif key > node.key:
                    node = node.right_node
                    if node == None:
                        return None

        return node.element ,node.key

    def remove(self, key):
        """@params key
        @return success of the remove operation.
        @raises ValueError if key is None.
        Removes the element with the given key, and returns True if element was found AND removed, else False.
        """
        # empty tree
        if self._root is None:
            return False

        if key is None:
            raise ValueError("You DONKEY! Key is not allowed to be None!")

        parent = None
        rem_node = self._root

        # find node to remove
        while rem_node.key != key:
            # obtain the parent
            parent = rem_node
            if key < rem_node.key:
                rem_node = rem_node.left_node
                if rem_node == None:  # case 1: key does not exist in left_nodes
                    return False
            elif key > rem_node.key:
                rem_node = rem_node.right_node
                if rem_node == None:  # case 1: if key does not exist in right_nodes
                    return False

        # IMPORTANT: obtained rem_node and its parent with while loop!
        c_ll, c_lr, c_rr, c_rl = self.control_upper_next(rem_node)

        # Case 1: key is root node
        if self._root.key == key:
            # if the root has no children
            if self._root.left_node is None and self._root.right_node is None:
                self._root = None
            # if left exists, but not right child
            elif self._root.left_node and self._root.right_node is None:
                self._root = self._root.left_node
            # if right exists, but no left child
            elif self._root.left_node is None and self._root.right_node:
                self._root = self._root.right_node
            # if right and left exists

            elif self._root.left_node and self._root.right_node:
                # enter the right subtree
                next_biggest = self._root.right_node
                # find next_biggest in right subtree
                while next_biggest.left_node:
                    next_biggest = next_biggest.left_node

                # remove node in forelast height and
                # node's children have no children (forelast height)
                if c_rl is None and c_rr is None:
                    self._rem_node_forelast_height(self._root, next_biggest, None)

                # next_biggest.parent is same as rem_node
                elif next_biggest.parent.key == rem_node.key:
                    next_biggest.left_node = self._root.left_node
                    self._root.left_node.parent = next_biggest
                    self._root = next_biggest

                else:  # right node of next_biggest exists
                    if next_biggest.right_node:
                        self._next_big_right_node_exists(self._root, next_biggest, None)
                    else:  # no next_biggest.right_node exists
                        self._next_big_no_right_node(self._root, next_biggest, None)
            self._size -= 1
            return True

        # case 2: remove_node has no children
        if rem_node.left_node is None and rem_node.right_node is None:
            if key < parent.key:
                parent.left_node = None
            else:
                parent.right_node = None
            self._size -= 1
            return True

        # case 3: remove-node has only left child
        elif rem_node.left_node and rem_node.right_node is None:
            if key < parent.key:
                # set children
                parent.left_node = rem_node.left_node
                # set parent
                rem_node.left_node.parent = parent
            else:
                parent.right_node = rem_node.left_node
                # set parent
                rem_node.left_node.parent = parent
            self._size -= 1
            return True

        # case 4: remove-node has only right child
        elif rem_node.left_node is None and rem_node.right_node:
            # check the root child's
            if key < parent.key:
                # set children
                parent.left_node = rem_node.right_node
                # set parent
                rem_node.right_node.parent = parent
            else:
                # set children
                parent.right_node = rem_node.right_node
                # set parent
                rem_node.right_node.parent = parent
            self._size -= 1
            return True

        # case 5: remove-node has left and right children
        else:
            next_biggest = rem_node.right_node
            # obtain next biggest node in right subtree
            while next_biggest.left_node:
                next_biggest = next_biggest.left_node

            # case 5.1: remove node in forelast height and
            # node's children have no children (forelast height)
            if c_ll is None and c_lr is None and c_rl is None and c_rr is None:
                self._rem_node_forelast_height(rem_node, next_biggest, parent)

            # case 5.2: next_biggest.parent is same as rem_node
            elif next_biggest.parent.key == rem_node.key:
                self._next_big_right_no_left_node(rem_node, next_biggest, parent)

            else:  # Case 5.3.1: right node of next_biggest exists
                if next_biggest.right_node:
                    self._next_big_right_node_exists(rem_node, next_biggest, parent)

                else:  # Case 5.3.2: no next_biggest.right_node exists
                    self._next_big_no_right_node(rem_node, next_biggest, parent)

        self._size -= 1
        return True


    def is_external(self, key):
        """@params key
        @return boolean
        @raises ValueError if key is None.
        Return True if the node with the given key is an external node, otherwise return False.
        """
        if key == None:
            raise ValueError("You Donkey! The key can't be None!")

        node = self._return_node(key)
        # check if the node has children
        if node.left_node is None and node.right_node is None:
            return True
        else:
            return False

       #TODO

    def is_internal(self, key):
        """@params key
        @return boolean
        @raises ValueError if key is None.
        Return True if the node with the given key is an internal node, otherwise return False.
        """
        if key == None:
            raise ValueError("You Donkey! The key can't be None!")

        node = self._return_node(key)
        if node.left_node or node.right_node:
            return True
        else:
            return False

    def to_array_inorder(self, curr_node, print_array):
        """@return array
        Returns an array-representation of the stored elements (Inorder traversal).
        """
        if curr_node:
            self.to_array_inorder(curr_node.left_node, print_array)
            print_array.append(curr_node.key)
            self.to_array_inorder(curr_node.right_node, print_array)
        return print_array

    def to_array_preorder(self, curr_node, print_array):
        """@return array
        Returns an array-representation of the stored elements (Preorder traversal).
        """
        if curr_node:
            print_array.append(curr_node.key)
            self.to_array_preorder(curr_node.left_node, print_array)
            self.to_array_preorder(curr_node.right_node, print_array)

    def to_array_postorder(self, curr_node, print_array):
        """@return array
        Returns an array-representation of the stored elements (Postorder traversal).
        """
        if curr_node:
            self.to_array_postorder(curr_node.left_node, print_array)
            self.to_array_postorder(curr_node.right_node, print_array)
            print_array.append(curr_node.key)
        return print_array


    def is_bst(self, tree):
        """@params tree is an instance of binary search tree.
        @return True if the given tree is a binary search tree, else False.
        @raises ValueError if the tree is empty or None.
        This method verifies a given BianryTree, if it is a correct Binary Search Tree.
        """
        if tree is None or tree._root is None:
            raise ValueError("Tree is empty or None!")

        return self._help_bst(tree._root)

    def return_min_key(self):
        """@return element of the minium key.
        Searches and returns the element of the smallest key in the bst.
        """
        smallest_key = self._return_node(min(self.to_array_inorder(self._root, [])))
        return smallest_key.element

    def runtime_comparison(self, linear_list, key):
        """Creates a binary search tree based on the given (linear) list and then determines runtime and number
        of comparisons needed to search a key in both, the internal BST and in the list. The time needed for the
        search in list and BST shall be printed on the terminal, the number of comparisons needed shall be returned
        in an array (index 0 = BST, index 1 = list)
        @param linear_list
        @param key The key to be search in list and BST.
        @return The number of comparisons needed to find the given key in the BST.
        @raises ValueError if one of the parameters is None.
        """
        if key is None or linear_list is None:
            raise ValueError("Invalid key or linear list")
        else:
            for i in linear_list:
                self.insert(TreeNode(key= i ))

    def get_depth(self, node):
        """@param node The node of which the depth should be determined.
        @return The depth of the node.
        Determines the depth of a node in the tree.
        """
        if node == self._root:
            return 0

        cur = self._root
        if node is None:
            raise ValueError("You Donkey! The node can't be None!")
        else:
            return self._depth_helper(cur, node)

    def is_tree_complete(self):
        """Analyses the tree and determines if it is complete.
        @return True if the tree is complete, False otherwise.
        """
        # attain max depth of the tree
        max_depth = self._max_depth(self._root)
        # check if the formula holds
        num_nodes = (2 ** (max_depth)) - 1
        if num_nodes is self._size:
            return True
        else:
            return False

    ''''''''''''''''''
    '''Support Functions'''
    ''''''''''''''''''

    def _insert_helper(self, cur, new_node):
        if cur.key < new_node.key:
            if cur.right_node is None:
                cur.right_node = new_node
                new_node.parent = cur
            else:
                self._insert_helper(cur.right_node, new_node)
        else:
            if cur.left_node is None:
                cur.left_node = new_node
                new_node.parent = cur
            else:
                self._insert_helper(cur.left_node, new_node)

    def _max_depth(self, node, depth=0):
        if node is None:
            return depth
        else:
            # returns integer with max depth
            return max(self._max_depth(node.left_node, depth + 1), self._max_depth(node.right_node, depth + 1))

    def _depth_helper(self, cur, node):
        if node.key == cur.key:
            depth = self._depth
            self._depth = 0
            return depth

        elif node.key < cur.key and cur.left_node:
            self._depth += 1
            return self._depth_helper(cur.left_node, node)

        else:
            self._depth += 1
            return self._depth_helper(cur.right_node, node)

    def _return_node(self, key):
        node = self._root

        while node.key != key:
            if key < node.key:
                node = node.left_node
                if node == None:
                    return None  # not found in all lefts
            elif key > node.key:
                node = node.right_node
                if node == None:
                    return None  # not found in all rights

        return node

    # prints all keys in ascending order
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left_node)
            print(node.key,end=' ')
            self.inorder_traversal(node.right_node)

    def control_upper_next(self, rem_node):
        control_node_left = rem_node.left_node
        control_node_right = rem_node.right_node

        if control_node_left:
            c_ll = control_node_left.left_node
            c_lr = control_node_left.right_node
        else:
            c_ll = None
            c_lr = None

        if control_node_right:
            c_rr = control_node_right.left_node
            c_rl = control_node_right.right_node
        else:
            c_rr = None
            c_rl = None
        return c_ll, c_lr, c_rr, c_rl

    def _rem_node_forelast_height(self, rem_node, next_biggest, parent):
        if rem_node == self._root:
            self._root.right_node = None
            next_biggest.left_node = self._root.left_node
            self._root.left_node.parent = next_biggest
            self._root = next_biggest

        else:
            if rem_node.key < parent.key:
                rem_node.right_node = None
                next_biggest.left_node = rem_node.left_node
                # set parent
                rem_node.left_node.parent = next_biggest
                rem_node = next_biggest
                rem_node.parent = parent
                # left side of the tree
                parent.left_node = rem_node

            else:
                rem_node.right_node = None
                next_biggest.left_node = rem_node.left_node
                # set parent
                rem_node.left_node.parent = next_biggest
                rem_node = next_biggest
                rem_node.parent = parent
                # right side of the tree
                parent.right_node = rem_node

    # case next_biggest.parent.key == rem_node.key
    def _next_big_right_no_left_node(self, rem_node, next_biggest, parent):
        if rem_node.key < parent.key:
            next_biggest.left_node = rem_node.left_node
            # set parent
            rem_node.left_node.parent = next_biggest
            rem_node = next_biggest
            rem_node.parent = parent
            # left side of the tree
            parent.left_node = rem_node

        else:  # problem here
            next_biggest.left_node = rem_node.left_node
            # set parent
            rem_node.left_node.parent = next_biggest
            rem_node = next_biggest
            rem_node.parent = parent
            # right side of the tree
            parent.right_node = rem_node

    def _next_big_right_node_exists(self, rem_node, next_biggest, parent):
        if rem_node == self._root:
            # connect right node of rem_node with rem_node.parent
            next_biggest.parent.left_node = next_biggest.right_node
            next_biggest.right_node.parent = next_biggest.parent
            # set children of rem_node
            next_biggest.right_node = self._root.right_node
            next_biggest.left_node = self._root.left_node
            # set parent of all nodes
            self._root.right_node.parent = next_biggest
            self._root.left_node.parent = next_biggest
            self._root = next_biggest

        else:
            if rem_node.key < parent.key:
                # connect the right node of rem_node with rem_node.parent
                next_biggest.parent.left_node = next_biggest.right_node
                next_biggest.right_node.parent = next_biggest.parent
                # set children of rem_node
                next_biggest.right_node = rem_node.right_node
                next_biggest.left_node = rem_node.left_node
                # set parent of all nodes
                rem_node.right_node.parent = next_biggest
                rem_node.left_node.parent = next_biggest
                parent.left_node = next_biggest  # left tree
                next_biggest.parent = parent

            else:
                # connect the right node of rem_node with rem_node.parent
                next_biggest.parent.left_node = next_biggest.right_node
                next_biggest.right_node.parent = next_biggest.parent
                # set children of rem_node
                next_biggest.right_node = rem_node.right_node
                next_biggest.left_node = rem_node.left_node
                # set parent of all nodes
                rem_node.right_node.parent = next_biggest
                rem_node.left_node.parent = next_biggest
                parent.right_node = next_biggest  # right tree
                next_biggest.parent = parent

    def _next_big_no_right_node(self, rem_node, next_biggest, parent):
        if rem_node == self._root:
            # empty the node
            next_biggest.parent.left_node = None
            # set children of rem_node
            next_biggest.right_node = self._root.right_node
            next_biggest.left_node = self._root.left_node
            # set parent of all nodes
            self._root.right_node.parent = next_biggest
            self._root.left_node.parent = next_biggest
            self._root = next_biggest

        else:
            if rem_node.key < parent.key:
                # empty the node
                next_biggest.parent.left_node = None
                # set children of rem_node
                next_biggest.right_node = rem_node.right_node
                next_biggest.left_node = rem_node.left_node
                # set parent of all nodes
                rem_node.right_node.parent = next_biggest
                rem_node.left_node.parent = next_biggest
                parent.left_node = next_biggest  # left tree
                next_biggest.parent = parent

            else:
                # empty the node
                next_biggest.parent.left_node = None
                # set children of rem_node
                next_biggest.right_node = rem_node.right_node
                next_biggest.left_node = rem_node.left_node
                # set parent of all nodes
                rem_node.right_node.parent = next_biggest
                rem_node.left_node.parent = next_biggest
                parent.right_node = next_biggest  # right tree
                next_biggest.parent = parent

    def _help_bst(self, current_node):
        if current_node is None:
            return True
        if current_node.left_node is not None and current_node.key <= current_node.left_node.key:
            return False
        if current_node.right_node is not None and current_node.key >= current_node.right_node.key:
            return False

        return self._help_bst(current_node.left_node) and self._help_bst(current_node.right_node)


''''''''''''''''''
'''Test Code'''
''''''''''''''''''
if __name__ == "__main__":
    test_bst = MyBinarySearchTree()
    test_bst.insert(TreeNode(key=10, element="a"))
    test_bst.insert(TreeNode(key=5, element="b"))
    test_bst.insert(TreeNode(key=7, element="c"))

    # test_bst.insert(None)

    # test_bst.inorder_traversal(test_bst._root)
    # test_bst.print_elements()

    # print(test_bst.to_array_inorder(test_bst._root, []))
    # print(test_bst.to_array_preorder(test_bst._root, []))
    # print(test_bst.to_array_postorder(test_bst._root, []))
    # print(test_bst.find(1))
    # test_bst.remove(2)
    # print(test_bst.to_array_inorder(test_bst._root, []))
    # test_bst.remove(2)
    # test_bst.remove(None)
    # print(test_bst.is_bst(test_bst))

    # empty_bst = MyBinarySearchTree()
    # print(test_bst.is_bst(empty_bst))
