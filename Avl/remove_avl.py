
class _avl_remove:
    def __init__(self):
        self.root = None

    def remove(self, key, root, size):
        if self.root is None:
            return False

        if key is None:
            raise ValueError("You DONKEY! Key is not allowed to be None!")

        parent = None
        rem_node = self.root
        # find node to remove
        while rem_node.key != key:
            # obtain the parent
            parent = rem_node
            if key < rem_node.key:
                rem_node = rem_node.left
                if rem_node == None:  # case 1: key does not exist in left_nodes
                    return False
            elif key > rem_node.key:
                rem_node = rem_node.right
                if rem_node == None:  # case 1: if key does not exist in right_nodes
                    return False

        # IMPORTANT: obtained rem_node and its parent with while loop!
        c_ll, c_lr, c_rr, c_rl = self.control_upper_next(rem_node)

        # Case 1: key is root node
        if self.root.key == key:
            # if the root has no children
            if self.root.left is None and self.root.right is None:
                self.root = None
            # if left exists, but not right child
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            # if right exists, but no left child
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            # if right and left exists

            elif self.root.left and self.root.right:
                # enter the right subtree
                next_biggest = self.root.right
                # find next_biggest in right subtree
                while next_biggest.left:
                    next_biggest = next_biggest.left

                # remove node in forelast height and
                # node's children have no children (forelast height)
                if c_rl is None and c_rr is None:
                    self._rem_node_forelast_height(self.root, next_biggest, None)

                # next_biggest.parent is same as rem_node
                elif next_biggest.parent.key == rem_node.key:
                    next_biggest.left = self.root.left
                    self.root.left.parent = next_biggest
                    self.root = next_biggest

                else:  # right node of next_biggest exists
                    if next_biggest.right:
                        self._next_big_right_node_exists(self.root, next_biggest, None)
                    else:  # no next_biggest.right_node exists
                        self._next_big_no_right_node(self.root, next_biggest, None)
            self.size -= 1
            return True

        # case 2: remove_node has no children
        if rem_node.left is None and rem_node.right is None:
            if key < parent.key:
                parent.left = None
            else:
                parent.right = None
            self.size -= 1
            return True

        # case 3: remove-node has only left child
        elif rem_node.left and rem_node.right is None:
            if key < parent.key:
                # set children
                parent.left = rem_node.left
                # set parent
                rem_node.left.parent = parent
            else:
                parent.right = rem_node.left
                # set parent
                rem_node.left.parent = parent
            self.size -= 1
            return True

        # case 4: remove-node has only right child
        elif rem_node.left is None and rem_node.right:
            # check the root child's
            if key < parent.key:
                # set children
                parent.left_node = rem_node.right
                # set parent
                rem_node.right.parent = parent
            else:
                # set children
                parent.right = rem_node.right
                # set parent
                rem_node.right.parent = parent
            self.size -= 1
            return True

        # case 5: remove-node has left and right children
        else:
            next_biggest = rem_node.right
            # obtain next biggest node in right subtree
            while next_biggest.left:
                next_biggest = next_biggest.left

            # case 5.1: remove node in forelast height and
            # node's children have no children (forelast height)
            if c_ll is None and c_lr is None and c_rl is None and c_rr is None:
                self._rem_node_forelast_height(rem_node, next_biggest, parent)

            # case 5.2: next_biggest.parent is same as rem_node
            elif next_biggest.parent.key == rem_node.key:
                self._next_big_right_no_left_node(rem_node, next_biggest, parent)

            else:  # Case 5.3.1: right node of next_biggest exists
                if next_biggest.right:
                    self._next_big_right_node_exists(rem_node, next_biggest, parent)

                else:  # Case 5.3.2: no next_biggest.right_node exists
                    self._next_big_no_right_node(rem_node, next_biggest, parent)

        self.size -= 1
        return True

    def control_upper_next(self, rem_node):
        control_node_left = rem_node.left
        control_node_right = rem_node.right

        if control_node_left:
            c_ll = control_node_left.left
            c_lr = control_node_left.right
        else:
            c_ll = None
            c_lr = None

        if control_node_right:
            c_rr = control_node_right.left
            c_rl = control_node_right.right
        else:
            c_rr = None
            c_rl = None
        return c_ll, c_lr, c_rr, c_rl

    def _rem_node_forelast_height(self, rem_node, next_biggest, parent):
        if rem_node == self.root:
            self.root.right = None
            next_biggest.left = self.root.left
            self.root.left.parent = next_biggest
            self.root = next_biggest

        else:
            if rem_node.key < parent.key:
                rem_node.right = None
                next_biggest.left = rem_node.left
                # set parent
                rem_node.left.parent = next_biggest
                rem_node = next_biggest
                rem_node.parent = parent
                # left side of the tree
                parent.left = rem_node

            else:
                rem_node.right = None
                next_biggest.left = rem_node.left
                # set parent
                rem_node.left.parent = next_biggest
                rem_node = next_biggest
                rem_node.parent = parent
                # right side of the tree
                parent.right = rem_node

        # case next_biggest.parent.key == rem_node.key

    def _next_big_right_no_left_node(self, rem_node, next_biggest, parent):
        if rem_node.key < parent.key:
            next_biggest.left = rem_node.left
            # set parent
            rem_node.left.parent = next_biggest
            rem_node = next_biggest
            rem_node.parent = parent
            # left side of the tree
            parent.left = rem_node

        else:  # problem here
            next_biggest.left = rem_node.left
            # set parent
            rem_node.left.parent = next_biggest
            rem_node = next_biggest
            rem_node.parent = parent
            # right side of the tree
            parent.right = rem_node

    def _next_big_right_node_exists(self, rem_node, next_biggest, parent):
        if rem_node == self.root:
            # connect right node of rem_node with rem_node.parent
            next_biggest.parent.left = next_biggest.right
            next_biggest.right.parent = next_biggest.parent
            # set children of rem_node
            next_biggest.right = self.root.right
            next_biggest.left = self.root.left
            # set parent of all nodes
            self.root.right.parent = next_biggest
            self.root.left.parent = next_biggest
            self.root = next_biggest

        else:
            if rem_node.key < parent.key:
                # connect the right node of rem_node with rem_node.parent
                next_biggest.parent.left = next_biggest.right
                next_biggest.right.parent = next_biggest.parent
                # set children of rem_node
                next_biggest.right = rem_node.right
                next_biggest.left = rem_node.left
                # set parent of all nodes
                rem_node.right.parent = next_biggest
                rem_node.left.parent = next_biggest
                parent.left = next_biggest  # left tree
                next_biggest.parent = parent

            else:
                # connect the right node of rem_node with rem_node.parent
                next_biggest.parent.left = next_biggest.right
                next_biggest.right.parent = next_biggest.parent
                # set children of rem_node
                next_biggest.right = rem_node.right
                next_biggest.left = rem_node.left
                # set parent of all nodes
                rem_node.right.parent = next_biggest
                rem_node.left.parent = next_biggest
                parent.right = next_biggest  # right tree
                next_biggest.parent = parent

    def _next_big_no_right_node(self, rem_node, next_biggest, parent):
        if rem_node == self.root:
            # empty the node
            next_biggest.parent.left = None
            # set children of rem_node
            next_biggest.right = self.root.right
            next_biggest.left = self.root.left
            # set parent of all nodes
            self.root.right.parent = next_biggest
            self.root.left.parent = next_biggest
            self.root = next_biggest

        else:
            if rem_node.key < parent.key:
                # empty the node
                next_biggest.parent.left = None
                # set children of rem_node
                next_biggest.right = rem_node.right
                next_biggest.left = rem_node.left
                # set parent of all nodes
                rem_node.right.parent = next_biggest
                rem_node.left.parent = next_biggest
                parent.left = next_biggest  # left tree
                next_biggest.parent = parent

            else:
                # empty the node
                next_biggest.parent.left = None
                # set children of rem_node
                next_biggest.right = rem_node.right
                next_biggest.left = rem_node.left
                # set parent of all nodes
                rem_node.right.parent = next_biggest
                rem_node.left.parent = next_biggest
                parent.right = next_biggest  # right tree
                next_biggest.parent = parent