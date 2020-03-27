"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        if self.node == None:
            self.height = -1
            return self.height
        elif not self.node.left and not self.node.right:
            self.height = 0
            return 0

        try:
            left_height = self.node.left.update_height()
        except:
            left_height = 0
        try:
            right_height = self.node.right.update_height()
        except:
            right_height = 0
        depth = 1 + max(left_height, right_height)
        self.height = depth
        return self.height

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        if self.node == None:
            self.balance = 0
            return self.balance
        try:
            left_height = self.node.left.update_height()
        except:
            left_height = 0
        try:
            right_height = self.node.right.update_height()
        except:
            right_height = 0
        self.balance = left_height - right_height
        return self.balance

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        pass

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        pass

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        pass
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        new_node = Node(key)
        if self.node == None:
            self.node = new_node
            return
        else:
            current_node = self.node
            while True:
                if key < current_node.key:
                    if current_node.left:
                        current_node = current_node.left.node
                    else:
                        current_node.left = AVLTree(new_node)
                        break
                else:
                    if current_node.right:
                        current_node = current_node.right.node
                    else:
                        current_node.right = AVLTree(new_node)
                        break
            # check if need to rebalance, then do so if needed


# tree = AVLTree()
# print(tree.update_height())
# tree.insert(5)
# print(tree.update_height())
# tree.insert(10)
# print(tree.update_height())
# tree.insert(3)
# print(tree.update_height())
# tree.insert(2)
# print(tree.update_height())
# tree.insert(1)
# print(tree.update_height())
# tree.display()