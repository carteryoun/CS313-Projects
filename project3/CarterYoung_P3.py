# ============================== Exceptions =====================================
class TreeIsEmpty(Exception):
    """This exception is raised when the tree is empty."""
    pass


# ============================== Aux Classes ====================================
class BSTNode():
    """ This class implements a node for the BST. """
    def __init__(self, item):
        """
        Description: The constructor for the Node class.
        Usage: node = BSTNode(item)
               item == (<int>, <value>)
        """
        self._parent = None
        self._lChild = None
        self._rChild = None
        self._value = item
        self._key = item[0]

    def __str__(self):
        """ Returns a string rep of the node (for debugging ^,^) """
        returnValue = "Node: {}\n".format(self._key)
        returnValue += f"Parent: {self._parent._key if self._parent != None else self._parent}\n"
        returnValue += f"Left Child: {self._lChild._key if self._lChild != None else self._lChild}\n"
        returnValue += f"Right Child: {self._rChild._key if self._rChild != None else self._rChild}\n"
        return returnValue
    # Accessor Methods

    def getParent(self):
        """
        Description: Accessor method for the Node. Returns parent.
        Usage: <node>.getParent()
        """
        return self._parent

    def getRChild(self):
        """
        Description: Accessor method for the Node. Returns right child.
        Usage: <node>.getRChild()
        """
        return self._rChild

    def getLChild(self):
        """
        Description: Accessor method for the Node. Returns left child.
        Usage: <node>.getLChild()
        """
        return self._lChild

    def getValue(self):
        """
        Description: Accessor method for the Node. Returns the item.
        Usage: <node>.getValue()
        """
        return self._value
    # Mutator methods

    def setParent(self, node):
        """
        Description: Mutator method. Sets the parent reference.
        Usage: <node>.setParent(<BSTNode>)
        """
        self._parent = node

    def setLChild(self, node):
        """
        Description: Mutator method. Sets the lchild reference.
        Usage: <node>.setLChild(<BSTNode>)
        """
        self._lChild = node

    def setRChild(self, node):
        """
        Description: Mutator method. Sets the rchild reference.
        Usage: <node>.setRChild(<BSTNode>)
        """
        self._rChild = node
    # comparison operators

    def __gt__(self, other):
        """
        Description: Overloads the > operator to allow direct comparison of
                     nodes.
        Usage: node1 > node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key > other._key
        return returnValue

    def __lt__(self, other):
        """
        Description: Overloads the < operator to allow direct comparison of
                     nodes.
        Usage: node1 < node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key < other._key
        return returnValue

    def __eq__(self, other):
        """
        Description: Overloads the == operator to allow direct comparison of
                     nodes.
        Usage: node1 == node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key == other._key
        return returnValue

    def __ne__(self, other):
        """
        Description: Overloads the != operator to allow direct comparison of
                     nodes.
        Usage: node1 != node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key != other._key
        if (other == None):
            returnValue = True
        return returnValue

    def __le__(self, other):
        """
        Description: Overloads the <= operator to allow direct comparison of
                     nodes.
        Usage: node1 <= node2
        """
        returnValue = False
        if (other != None):
            returnValue = self._key <= other._key
        return returnValue

    def __ge__(self, other):
        """
        Description: Overloads the >= operator to allow direct comparison of
                     nodes.
        Usage:  node1 >= node2
        Input: Another instance of the node class.
        """
        returnValue = False
        if (other != None):
            returnValue = self._key >= other._key
        return returnValue
    # Some helper methods to make things easy in the BST

    def hasLeftChild(self):
        """
        Description: This method returns true if the current node
                     has a left child.
        Usage: <node>.hasLeftChild()
        """
        returnValue = False
        if (type(self._lChild) == BSTNode and self._lChild._parent is self):
            returnValue = True
        return returnValue

    def hasRightChild(self):
        """
        Description: This method returns true|false depending on if the current
                     node has a right child or not.
        Usage: <node>.hasRightChild()
        """
        returnValue = False
        if (type(self._rChild) == BSTNode and self._rChild._parent is self):
            returnValue = True
        return returnValue

    def hasOnlyOneChild(self):
        """
        Description: Returns True if the current node has only one child.
        Usage: <node>.hasOnlyOneChild()
        """
        LC = self.hasLeftChild()
        RC = self.hasRightChild()
        return (LC and not RC) or (not LC and RC)

    def hasBothChildren(self):
        """
        Description: Returns True if the current node has both children
        Usage: <node>.hasBothChildren()
        """
        return self.hasLeftChild() and self.hasRightChild()

    def isLeaf(self):
        """
        Description: Returns true if the current node is a leaf node.
        Usage: <node>.isLeaf()
        """
        returnValue = False
        if (self._rChild == None and self._lChild == None):
            returnValue = True
        return returnValue

    def isLeftChild(self):
        """
        Description: Returns true if the current node is a left child
        Usage: <node>.isLeftChild()
        """
        returnValue = False
        if (self._parent != None):
            if (self._parent._lChild is self):
                if (self._parent._rChild is not self):
                    returnValue = True
        return returnValue

    def isRightChild(self):
        """
        Description: Returns true if the current node is a right child
        Usage: <node>.isRightChild()
        """
        returnValue = False
        if (self._parent != None):
            if (self._parent._rChild is self):
                if (self._parent._lChild is not self):
                    returnValue = True
        return returnValue
# ===============================================================================
# ================================ BST Class ====================================


class BinarySearchTree:
    """
    Description: A Binary Search Tree (BST).
    Note: Algorithms for the BST can be found in ch. 12 of the book.
    """
    def __init__(self):
        """ The constructor for our BST """
        self._root = None
        # Add any other instance variables you need.

    def _isValid(self, item):
        """
        Description: Checks to see if a tuple is valid
        Usage: (outside) BST.isValid(item) (inside) self.isValid(item)
        """
        returnValue = True
        if (type(item) != tuple):
            returnValue = False
        elif (type(item[0]) != int):
            returnValue = False
        elif (len(item) != 2):
            returnValue = False
        return returnValue

    def _transplantR(self, cNode):
        """
        Description: This transplant attaches the currentNodes right child
                     to the current nodes parent.
        Notes:
                1. Do not call this method when cNode is the root.
                2. Don't forget to handle the cNodes references in your func.
        """
        parent = cNode.getParent()
        child = cNode.getRChild()
        if (cNode.isLeftChild()):
            parent.setLChild(child)
            child.setParent(parent)
        else:
            parent.setRChild(child)
            child.setParent(parent)

    def _transplantL(self, cNode):
        """
        Description: This transplant attaches the currentNodes right child
                     to the current nodes parent.
        Notes:
                1. Do not call this method when cNode is the root.
                2. Don't forget to handle the cNodes references in your func.
        """
        parent = cNode.getParent()
        child = cNode.getLChild()
        if (cNode.isLeftChild()):
            parent.setLChild(child)
            child.setParent(parent)
        else:
            parent.setRChild(child)
            child.setParent(parent)

    def traverse(self, mode):
        """
        Description: The traverse method returns a string rep
                     of the tree according to the specified mode
        """
        self.output = ""
        if (type(mode) == str):
            if (mode == "in-order"):
                self.inorder(self._root)
            elif (mode == "pre-order"):
                self.preorder(self._root)
            elif (mode == "post-order"):
                self.postorder(self._root)
        else:
            self.output = "ERROR: Unrecognized mode..."
        return self.output[:-2]

    def inorder(self, node):
        """ computes the inorder traversal """
        if (node != None):
            self.inorder(node.getLChild())
            self.output += str(node._key) + ", "
            self.inorder(node.getRChild())

    def preorder(self, node):
        """computes the pre-order traversal"""
        if (node != None):
            self.output += str(node._key) + ", "
            self.preorder(node.getLChild())
            self.preorder(node.getRChild())

    def postorder(self, node):
        """ compute postorder traversal"""
        if (node != None):
            self.postorder(node.getLChild())
            self.postorder(node.getRChild())
            self.output += str(node._key) + ", "

    def _findNode(self, id):
        """ Return: A node if found, else, return none
            Starting at the root, compares the node and key.
            Goes right if the key is higher, goes left if it is lower.
            Returns the key once it matches."""
        if self._root == None:
            raise TreeIsEmpty('Can not call find on an empty tree.')
        cur = self._root
        while cur:
            if cur._key == id:
                return cur
            elif cur._key > id:
                cur = cur.getLChild()
            else:
                cur = cur.getRChild()
        return None

    def find(self, id):
        """Complexity: O(lg(n)) ~ O(n)
           Input: Takes an int id
           Returns: Success: The tuple in the tree whose ID matches that value
           Failure: If no tuple exists in the tree, returns false.
           Raises: TreeIsEmpty if the method is called when the tree is empty"""
        found_node = self._findNode(id)
        if found_node:
            return found_node.getValue()
        else:
            return False

    def transplant(self, u, v):
        """u is the current node, v is the node that replaces u"""
        parent = u.getParent()
        if parent == None:
            self._root = v
        elif u == parent.getLChild():
            parent.setLChild(v)
        else:
            parent.setRChild(v)
        if v != None:
            v.setParent(parent)

    def delete (self, id):
        """ The delete method will remove a node from the tree whose
            id matches that of the id from the input parameter.
            Complexity: O(lg(n)) ~ O(n)"""
        if self._root == None:
            raise TreeIsEmpty('Can not call delete on an empty tree.')
        z = self._findNode(id)

        p = z.getParent()
        left = z.getLChild()
        right = z.getRChild()

        if left == None:
            self.transplant(z, right)
        elif right == None:
            self.transplant(z, left)
        else:
            y = right
            while y.getLChild():
                y = y.getLChild()
                """y = successor"""
            if y.getParent() != z:
                self.transplant(y, y.getRChild())
                y.setRChild(right)
                y.getRChild().setParent(y)

            self.transplant(z, y)
            y.setLChild(z.getLChild())
            y.getLChild().setParent(y)

        """detach z"""
        z.setParent(None)
        z.setLChild(None)
        z.setRChild(None)

    def insert(self, item):
        """ The insert method will insert a new item into the tree.
            It does so by creating a new node with the tuple then adding
            it to the tree. It preserves the characteristics of parent-child
            relation essential for a BST. It then returns true or false based
            on whether the insert was successful.
            Complexity: O(lg(n)) ~ O(n)"""
        if self._isValid(item):
            new_node = BSTNode(item)
        else:
            return False

        if self._root == None:
            self._root = new_node
            return True
        else:
            cur = self._root
            parent = None
            while cur != None:
                parent = cur
                if cur._key < new_node._key:
                    cur = cur.getRChild()
                else:
                    cur = cur.getLChild()

            if parent == None:
                return False

            if new_node._key < parent._key:
                parent.setLChild(new_node)
            else:
                parent.setRChild(new_node)
            new_node.setParent(parent)
            return True


if __name__ == '__main__':
    v = 'a'
    n1 = BSTNode((1, v))
    n5 = BSTNode((5, v))
    n9 = BSTNode((9, v))
    n17 = BSTNode((17, v))
    n10 = BSTNode((10, v))
    n15 = BSTNode((15, v))
    n20 = BSTNode((20, v))
    n22 = BSTNode((22, v))
    n25 = BSTNode((25, v))
    n30 = BSTNode((30, v))
    n35 = BSTNode((35, v))
    n40 = BSTNode((40, v))
    n45 = BSTNode((45, v))

    """Creates the tree and its connections"""
    n1.setParent(n5)
    n5.setParent(n9)
    n9.setParent(n10)
    n10.setParent(n15)
    n17.setParent(n15)
    n15.setParent(n20)
    n25.setParent(n20)
    n22.setParent(n25)
    n35.setParent(n25)
    n40.setParent(n35)
    n45.setParent(n40)

    n5.setLChild(n1)
    n9.setLChild(n5)
    n10.setLChild(n9)
    n15.setRChild(n17)
    n15.setLChild(n10)
    n20.setLChild(n15)
    n20.setRChild(n25)
    n25.setLChild(n22)
    n25.setRChild(n35)
    n35.setRChild(n40)
    n40.setRChild(n45)

    tree = BinarySearchTree()
    tree._root = n20

    print("In-order traversal: ", tree.traverse('in-order'))
    print("Pre-order traversal: ", tree.traverse('pre-order'))
    print("Post-order traversal: ", tree.traverse('post-order'))

    tree.delete(20)

    print("   ------------------------------------------------------------   ")
    print("In-order after deletion of n20: ", tree.traverse('in-order'))
    print("Pre-order after deletion of n20: ", tree.traverse('pre-order'))
    print("Post-order after deletion of n20: ", tree.traverse('post-order'))
