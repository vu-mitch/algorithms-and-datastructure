from avl_node import AVLNode
from remove_avl import _avl_remove

class AVLTree:

    def __init__(self):
        """Default constructor. Initializes the AVL tree.
        """
        self.root = None
        self.size = 0

    def __repr__(self):
        if self.root == None: return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.root.height  # height of nodes at current level
        sep = ' ' * (2 ** (cur_height - 1))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0: break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n == None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.key != None:
                    buf = ' ' * int((5 - len(str(n.key))) / 2)
                    cur_row += '%s%s%s' % (buf, str(n.key), buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left != None:
                    next_nodes.append(n.left)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right != None:
                    next_nodes.append(n.right)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)  # cut separator size in half
        return content

    def print_height(self):
        if self.root == None: return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.root.height  # height of nodes at current level
        sep = ' ' * (2 ** (cur_height - 1))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0: break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n == None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.key != None:
                    buf = ' ' * int((5 - len(str(n.height))) / 2)
                    cur_row += '%s%s%s' % (buf, str(n.height), buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left != None:
                    next_nodes.append(n.left)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right != None:
                    next_nodes.append(n.right)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)  # cut separator size in half
        return content

    def print_parent(self):
        if self.root == None: return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.root.height  # height of nodes at current level
        sep = ' ' * (2 ** (cur_height - 1))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0: break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n == None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.key != None:
                    buf = ' ' * int((5 - len(str(n.parent))) / 2)
                    if n.parent is None:
                        cur_row += '%s%s%s' % (buf, str(n.parent), buf) + sep
                    else:
                        cur_row += '%s%s%s ' % (buf, str(n.parent.key), buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left != None:
                    next_nodes.append(n.left)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right != None:
                    next_nodes.append(n.right)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)  # cut separator size in half
        print("parents")
        return content

    def get_root(self):
        """@returns the root of the AVLTree
        """
        return self.root

    def get_height(self):
        """Retrieves tree height.
    	 @return -1 in case of empty tree, current tree height otherwise.
    	 """
        if self.root is None:
            return -1
        else:
            return self.root.height

    def get_size(self):
        """Yields number of key/element pairs in the tree.
        @return Number of key/element pairs.
        """
        return self.size

    def to_array(self):
        """Yields an array representation of the tree elements (pre-order).
    	@return Array representation of the tree elements.
        """
        array = []
        queue = []
        node = self.root
        while node or queue:
            while node:
                if node.key != None:
                    array.append(node.key)
                queue.append(node)
                node = node.left
            temp = queue[-1]
            queue.pop()
            if temp.right:
                node = temp.right
        return array

    def find(self, key):
        """Returns element of node with given key.
    	 @param key: Key to search.
    	 @return Corresponding element if key was found, None otherwise.
         @raises ValueError if the key is None
    	 """
        if key is None:
            raise ValueError("key cannot be None")
        node = self.root

        while node.key != key:
            if key < node.key:
                node = node.left
                if node is None:
                    return
            elif key > node.key:
                node = node.right
                if node is None:
                    return

        return node.elem

    def insert(self, key, elem):
        """Inserts a new node into AVL tree.
    	 @param key: Key of the new node.
    	 @param elem: Data of the new node. Elements with the same key
    	 are not allowed. In this case false is returned. None-Keys are
    	 not allowed. In this case an exception is thrown.
         @raises ValueError if the key or elem is None.
        """
        if key is None or elem is None:
            raise ValueError("You Donkey! Param mustn't be none!")

        # case: tree is empty
        if self.root is None:
            self.root = AVLNode(key, elem)
            self.size += 1
        else:
            self._insert(self.root, key, elem)
            self.size += 1

    def _insert(self, current, key, elem):
        if current == None:
            return AVLNode(key, elem)
        elif key < current.key:
            current.left = self._insert(current.left, key, elem)
            current.left.parent = current
        elif key > current.key:
            current.right = self._insert(current.right, key, elem)
            current.right.parent = current
        else:
            return False

        current.height = self.findMax(self._height(current.left), self._height(current.right)) + 1

        balance = self.balance(current)
        # left left
        # print(balance)
        if balance > 1 and key < current.left.key:
            return self.rotateRight(current)
        # right right
        if balance < -1 and key > current.right.key: # take care
            return self.rotateLeft(current)
        # left right
        if balance > 1 and key > current.left.key:
            if current is self.root:
                return self.root_doubleRight(current)
            else:
                return self.doubleRight(current)
        # right left
        if balance < -1 and key < current.right.key:
            if current is self.root:
                return self.root_doubleLeft(current)
            else:
                return self.doubleLeft(current)
        return current

    def _height(self, current):
        if current == None:
            return -1
        return current.height

    def findMax(self, a, b):
        if a >= b:
            return a
        else:
            return b

    def balance(self, current):
        if current == None:
            return 0
        return (self._height(current.left) - self._height(current.right))

    def doubleLeft(self, c):
        a = c.right
        b = a.left
        array = [a.right, a, b.right, b, b.left, c, c.left]
        # case distinction for parent pointer
        if array[5].parent.key > array[5].key:
            array[5].parent.left = array[3]  # c.parent.left = b
        else:
            array[5].parent.right = array[3]  # c.parent.right = b

        array[1].left = array[2] # a.right = t1 #changes made here last time
        array[5].right = array[4] # c.left = t2 #changes made here last time

        array[3].left = array[5] # b.right = c
        array[3].right = array[1] # b.left = a

        array[1].parent = array[3] # a.parent = b
        array[5].parent = array[3] # c.parent = b

        array[1].height = self.findMax(self._height(array[1].left), self._height(array[1].right)) + 1
        array[5].height = self.findMax(self._height(array[5].left), self._height(array[5].right)) + 1
        array[3].height = self.findMax(self._height(array[3].left), self._height(array[3].right)) + 1
        return b

    def doubleRight(self, c):
        a = c.left
        b = a.right
        array = [a.left, a, b.left, b, b.right, c, c.right]
        # case distinction for parent pointer
        if array[5].parent.key > array[5].key:
            array[5].parent.left = array[3]  # c.parent.left = b
        else:
            array[5].parent.right = array[3]  # c.parent.right = b

        array[1].right = array[2] # a.right = t1
        array[5].left = array[4] # c.left = t2

        array[3].right = array[5] # b.right = c
        array[3].left = array[1] # b.left = a

        array[1].parent = array[3] # a.parent = b
        array[5].parent = array[3] # c.parent = b

        array[1].height = self.findMax(self._height(array[1].left), self._height(array[1].right)) + 1
        array[5].height = self.findMax(self._height(array[5].left), self._height(array[5].right)) + 1
        array[3].height = self.findMax(self._height(array[3].left), self._height(array[3].right)) + 1
        return b

    def root_doubleRight(self, c):
        a = c.left
        b = a.right
        array = [a.left, a, b.left, b, b.right, c, c.right]
        self.root = array[3]
        self.root.parent = None

        array[1].right = array[2] # a.right = t1
        array[5].left = array[4] # c.left = t2

        self.root.right = array[5] # b.right = c
        self.root.left = array[1] # b.left = a

        array[1].parent = self.root
        array[5].parent = self.root

        array[1].height = self.findMax(self._height(array[1].left), self._height(array[1].right)) + 1
        array[5].height = self.findMax(self._height(array[5].left), self._height(array[5].right)) + 1
        self.root.height = self.findMax(self._height(self.root.left), self._height(self.root.right)) + 1
        return #array[4]

    def root_doubleLeft(self, c):
        a = c.right
        b = a.left
        array = [a.right, a, b.right, b, b.left, c, c.left]
        self.root = array[3]
        self.root.parent = None

        array[1].left = array[2] # a.right = t1
        array[5].right = array[4] # c.left = t2

        self.root.left = array[5] # b.right = c
        self.root.right = array[1] # b.left = a

        array[1].parent = self.root
        array[5].parent = self.root

        array[1].height = self.findMax(self._height(array[1].left), self._height(array[1].right)) + 1
        array[5].height = self.findMax(self._height(array[5].left), self._height(array[5].right)) + 1
        self.root.height = self.findMax(self._height(self.root.left), self._height(self.root.right)) + 1
        return #array[4]

    def rotateRight(self, a):
        b = a.left
        c = b.left
        array = [a.right, a, b.right, b, c.right, c, c.left]
        if array[1] is self.root:  # root case
            self.root = array[3]
            self.root.parent = None
        else:
            array[1].parent = array[3]

        array[3].right = array[1]  # connect b.right = a
        array[1].parent = array[3] # connect a.parent = b
        array[1].left = array[2]  # a.left = b.right(T1)

        if array[2]:
            array[2].parent = array[1] # b.right.parent = a

        array[1].height = self.findMax(self._height(array[1].left), self._height(array[1].right)) + 1
        array[3].height = self.findMax(self._height(array[3].left), self._height(array[3].right)) + 1
        return array[3]

    def rotateLeft(self, a):
        b = a.right
        c = b.right
        array = [a.left, a, b.left, b, c.left, c, c.right]
        if array[1] is self.root:  # root case
            self.root = array[3]
            self.root.parent = None
        else:
            array[1].parent = array[3]
        # temp = array[3].left
        array[3].left = array[1]  # b.right = a
        array[1].parent = array[3] # a.parent = b
        array[1].right = array[2]  # a.right = b.left(T1)

        if array[2]:
            array[2].parent = array[1] # b.right.parent = a

        array[1].height = self.findMax(self._height(array[1].left), self._height(array[1].right)) + 1
        array[3].height = self.findMax(self._height(array[3].left), self._height(array[3].right)) + 1
        return array[3]

    def remove(self, key):
        """Removes node with given key.
    	 @param key: Key of node to remove.
    	 @return true If element was found and deleted.
         @raises ValueError if the key is None
        """
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
                    next_biggest.height = self.findMax(self._height(next_biggest.left), self._height(next_biggest.right)) + 1

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

if __name__ == "__main__":
    avl = AVLTree()
    # avl.insert(50,"")
    # avl.insert(40,"")
    # avl.insert(60,"")
    # avl.insert(70,"")
    # avl.insert(30,"")
    # avl.insert(45,"")
    # avl.insert(35,"")
    # avl.insert(47,"")
    # avl.insert(46,"")

    # import random
    # rand_list = list()
    # for x in range(10):
    #     num = random.randint(0,1000)
    #     if num not in rand_list and num is not 5: rand_list.append(num)
    #
    # for x in rand_list:
    #     avl.insert(x,".")
    #     # print(avl.print_height())
    #     # print(avl.print_parent())
    #     print(avl)

    # print(avl.print_parent())
    # print(avl)
    # print(avl.print_height())

    # avl.insert_kv(22, ".")
    # avl.insert_kv(26, ".")
    # avl.insert_kv(21, ".")
    # avl.insert_kv(25, ".")
    # avl.insert_kv(28, ".")
    # avl.insert_kv(30, ".")

