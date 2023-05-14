# This is a class for creating a binary tree node with a value, left and right child nodes, and a
# height attribute.
class TreeNode(object):
    def __init__(self, val):
        """
        This is the initialization function for a binary tree node, which sets the node's value, left
        and right child nodes to None, and height to 1.
        
        :param val: The value to be stored in the node of a binary search tree
        """
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# This is an implementation of an AVL tree data structure in Python, which includes methods for
# inserting nodes, rotating nodes left and right, and calculating the height and balance of nodes.
class AVL_Tree(object):
    def insert(self, root, key):
        """
        This is an implementation of the AVL tree insertion algorithm in Python.
        
        :param root: The root node of the binary search tree where the key needs to be inserted
        :param key: The value to be inserted into the binary search tree
        :return: a TreeNode object, which represents the root of the binary search tree after the
        insertion of the new key.
        """
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        """
        This function performs a left rotation on a binary search tree.
        
        :param z: The node that needs to be rotated to the left
        :return: the node `y` after performing a left rotation on the input node `z`.
        """
        if z.right is None:
            return z
        
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):
        """
        This is a function that performs a right rotation on a binary search tree.
        
        :param z: The node that needs to be right rotated
        :return: the node `y` which is the new root of the subtree after performing a right rotation on
        the node `z`.
        """
        if z.left is None:
            return z

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, root):
        """
        This function returns the height of a binary tree rooted at the given node.
        
        :param root: The root node of a binary tree
        :return: the height of the input binary tree's root node. If the root is None, it returns 0.
        Otherwise, it returns the height of the root node.
        """
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        """
        This function returns the balance factor of a binary tree node by subtracting the height of its
        right subtree from the height of its left subtree.
        
        :param root: The root node of a binary tree
        :return: The function `getBalance` is returning the balance factor of a given node in an AVL
        tree. The balance factor is calculated as the difference between the height of the left subtree
        and the height of the right subtree.
        """
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)


def main():
    """
    This function reads 10 files containing numbers, inserts them into an AVL tree, and prints the
    height of the tree after each file is read.
    """
    myTree = AVL_Tree()
    root = None

    for i in range(10):
        root = None
        filename = f'numbers_{i + 1}.txt'
        with open(filename, 'r') as file:
            line = file.readline()
            numbers = map(int, line.strip().split())
            for num in numbers:
                root = myTree.insert(root, num)
        print(f"Height of tree after reading file {filename}: {myTree.getHeight(root)}")


if __name__ == "__main__":
    main()
