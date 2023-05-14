# This is a class for creating nodes in a red-black tree with attributes for data, color, parent, left
# child, and right child.
class Node:
    def __init__(self, data, color=1, parent=None, left=None, right=None):
        """
        This is the initialization function for a node in a red-black tree, which sets the node's data,
        color, parent, left child, and right child.
        
        :param data: The value to be stored in the node
        :param color: The color of the node in a red-black tree. It can be either 0 (black) or 1 (red),
        defaults to 1 (optional)
        :param parent: The parent parameter is a reference to the parent node of the current node in a
        binary tree. It is used to navigate up the tree from a given node. If the current node is the
        root node, then the parent parameter will be set to None
        :param left: The left child node of the current node in a binary tree. If there is no left
        child, it is set to None
        :param right: The right child node of the current node in a binary tree. If there is no right
        child, it is set to None
        """
        self.data = data
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


# The RedBlackTree class is a Python implementation of a red-black tree data structure with methods
# for insertion, rotation, and height calculation.
class RedBlackTree:
    def __init__(self):
        """
        This is the initialization function for a binary search tree with a root node and a NIL node.
        """
        self.NIL = Node(0, 0)
        self.root = self.NIL

    def left_rotate(self, x):
        """
        This function performs a left rotation on a binary search tree.
        
        :param x: a node in a binary search tree that we want to left rotate
        """
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        """
        This function performs a right rotation on a binary search tree.
        
        :param x: a node in a binary search tree that we want to right rotate
        """
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, node):
        """
        This function inserts a new node into a binary search tree and fixes the tree to maintain the
        properties of a red-black tree.
        
        :param node: The node to be inserted into the binary search tree. It should have a "data"
        attribute that can be compared to other nodes in the tree, as well as "left", "right", and
        "parent" attributes that will be set during the insertion process. The "color" attribute is also
        :return: The function does not explicitly return anything, but it may return early if certain
        conditions are met.
        """
        node.parent = None
        node.data = node.data
        node.left = self.NIL
        node.right = self.NIL
        node.color = 1  # new node must be red

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # if new node is a root node, simply return
        if node.parent is None:
            node.color = 0
            return

        # if the grandparent is None, simply return
        if node.parent.parent is None:
            return

        # fix the tree
        self.fix_insert(node)

    def fix_insert(self, node):
        """
        This is an implementation of the fix_insert function for a red-black tree data structure.
        
        :param node: The node that was just inserted into the binary search tree and may have caused a
        violation of the red-black tree properties
        """
        while node.parent.color == 1:
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left  # uncle
                if u.color == 1:
                    u.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
            else:
                u = node.parent.parent.right  # uncle

                if u.color == 1:
                    u.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = 0

    def print_in_order(self, node):
        """
        This function prints the data of a binary search tree in ascending order.
        
        :param node: The node parameter is a reference to a node object in a binary search tree. The
        function print_in_order recursively traverses the tree in order (left subtree, root, right
        subtree) and prints the data of each node in that order. The function stops when it reaches a
        NIL node, which represents
        """
        if node != self.NIL:
            self.print_in_order(node.left)
            print(node.data)
            self.print_in_order(node.right)

    def calculate_height(self, node):
        """
        This function calculates the height of a binary tree recursively.
        
        :param node: The node for which we want to calculate the height in a binary tree
        :return: the height of a binary search tree rooted at the given node. It recursively calculates
        the height of the left and right subtrees and returns the maximum height plus one, which
        represents the height of the current node. If the node is None or a sentinel node, the function
        returns 0.
        """
        if node is None or node == self.NIL:
            return 0
        else:
            left_height = self.calculate_height(node.left)
            right_height = self.calculate_height(node.right)
            return max(left_height, right_height) + 1


def main():
    """
    The main function reads 10 files containing random numbers, inserts them into a Red-Black Tree,
    calculates the height of the tree after each insertion, and prints the final result.
    """
    bst = RedBlackTree()

    for i in range(10):
        filename = f'random_numbers_{i}.txt'
        with open(filename, 'r') as file:
            line = file.readline()
            numbers = map(int, line.strip().split())
            for num in numbers:
                bst.insert(Node(num))
        print(f"Height of tree after reading file {filename}: {bst.calculate_height(bst.root)}")

    # bst.print_in_order(bst.root)
    print("done")


if __name__ == "__main__":
    main()
