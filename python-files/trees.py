class FenwickTree:

    def __init__(self, SIZE):  # create fenwick tree with size SIZE
        self.Size = SIZE
        self.ft = [0 for i in range(0, SIZE)]

    def update(self, i, val):  # update data (adding) in index i in O(lg N)
        while (i < self.Size):
            self.ft[i] += val
            i += i & (-i)

    def query(self, i):  # query cumulative data from index 0 to i in O(lg N)
        ret = 0
        while (i > 0):
            ret += self.ft[i]
            i -= i & (-i)
        return ret


class SegmentTree:

    def __init__(self, N):
        import math
        self.N = N
        # approximate the overall size of segment tree with array N
        self.st = [0 for i in range(0, 4 * N)]
        # create array to store lazy update
        self.lazy = [0 for i in range(0, 4 * N)]
        self.flag = [0 for i in range(0, 4 * N)]  # flag for lazy update

    def left(self, idx):
        return idx * 2

    def right(self, idx):
        return idx * 2 + 1

    def build(self, idx, l, r, A):
        if l == r:
            self.st[idx] = A[l - 1]
        else:
            mid = (l + r) // 2
            self.build(self.left(idx), l, mid, A)
            self.build(self.right(idx), mid + 1, r, A)
            self.st[idx] = max(self.st[self.left(idx)],
                               self.st[self.right(idx)])

    # update with O(lg N) (Normal segment tree without lazy update will take O(Nlg N) for each update)
    # update(1, 1, N, a, b, v) for update val v to [a,b]
    def update(self, idx, l, r, a, b, val):
        if self.flag[idx] == True:
            self.st[idx] = self.lazy[idx]
            self.flag[idx] = False
            if l != r:
                self.lazy[self.left(idx)] = self.lazy[idx]
                self.lazy[self.right(idx)] = self.lazy[idx]
                self.flag[self.left(idx)] = True
                self.flag[self.right(idx)] = True

        if r < a or l > b:
            return True
        if l >= a and r <= b:
            self.st[idx] = val
            if l != r:
                self.lazy[self.left(idx)] = val
                self.lazy[self.right(idx)] = val
                self.flag[self.left(idx)] = True
                self.flag[self.right(idx)] = True
            return True
        mid = (l + r) // 2
        self.update(self.left(idx), l, mid, a, b, val)
        self.update(self.right(idx), mid + 1, r, a, b, val)
        self.st[idx] = max(self.st[self.left(idx)], self.st[self.right(idx)])
        return True

    # query with O(lg N)
    # query(1, 1, N, a, b) for query max of [a,b]
    def query(self, idx, l, r, a, b):
        if self.flag[idx] == True:
            self.st[idx] = self.lazy[idx]
            self.flag[idx] = False
            if l != r:
                self.lazy[self.left(idx)] = self.lazy[idx]
                self.lazy[self.right(idx)] = self.lazy[idx]
                self.flag[self.left(idx)] = True
                self.flag[self.right(idx)] = True
        if r < a or l > b:
            return -math.inf
        if l >= a and r <= b:
            return self.st[idx]
        mid = (l + r) // 2
        q1 = self.query(self.left(idx), l, mid, a, b)
        q2 = self.query(self.right(idx), mid + 1, r, a, b)
        return max(q1, q2)

    def showData(self):
        showList = []
        for i in range(1, N + 1):
            showList += [self.query(1, 1, self.N, i, i)]
        print(showList)


class Node:

    def __init__(self, label, parent):
        self.label = label
        self.left = None
        self.right = None
        #Added in order to delete a node easier
        self.parent = parent

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, label):
        # Create a new Node
        new_node = Node(label, None)
        # If Tree is empty
        if self.empty():
            self.root = new_node
        else:
            #If Tree is not empty
            curr_node = self.root
            #While we don't get to a leaf
            while curr_node is not None:
                #We keep reference of the parent node
                parent_node = curr_node
                #If node label is less than current node
                if new_node.getLabel() < curr_node.getLabel():
                    #We go left
                    curr_node = curr_node.getLeft()
                else:
                    #Else we go right
                    curr_node = curr_node.getRight()
            #We insert the new node in a leaf
            if new_node.getLabel() < parent_node.getLabel():
                parent_node.setLeft(new_node)
            else:
                parent_node.setRight(new_node)
            #Set parent to the new node
            new_node.setParent(parent_node)

    def delete(self, label):
        if (not self.empty()):
            #Look for the node with that label
            node = self.getNode(label)
            #If the node exists
            if(node is not None):
                #If it has no children
                if(node.getLeft() is None and node.getRight() is None):
                    self.__reassignNodes(node, None)
                    node = None
                #Has only right children
                elif(node.getLeft() is None and node.getRight() is not None):
                    self.__reassignNodes(node, node.getRight())
                #Has only left children
                elif(node.getLeft() is not None and node.getRight() is None):
                    self.__reassignNodes(node, node.getLeft())
                #Has two children
                else:
                    #Gets the max value of the left branch
                    tmpNode = self.getMax(node.getLeft())
                    #Deletes the tmpNode
                    self.delete(tmpNode.getLabel())
                    #Assigns the value to the node to delete and keesp tree structure
                    node.setLabel(tmpNode.getLabel())

    def getNode(self, label):
        curr_node = None
        #If the tree is not empty
        if(not self.empty()):
            #Get tree root
            curr_node = self.getRoot()
            #While we don't find the node we look for
            #I am using lazy evaluation here to avoid NoneType Attribute error
            while curr_node is not None and curr_node.getLabel() is not label:
                #If node label is less than current node
                if label < curr_node.getLabel():
                    #We go left
                    curr_node = curr_node.getLeft()
                else:
                    #Else we go right
                    curr_node = curr_node.getRight()
        return curr_node

    def getMax(self, root=None):
        if(root is not None):
            curr_node = root
        else:
            #We go deep on the right branch
            curr_node = self.getRoot()
        if(not self.empty()):
            while(curr_node.getRight() is not None):
                curr_node = curr_node.getRight()
        return curr_node

    def getMin(self, root=None):
        if(root is not None):
            curr_node = root
        else:
            #We go deep on the left branch
            curr_node = self.getRoot()
        if(not self.empty()):
            curr_node = self.getRoot()
            while(curr_node.getLeft() is not None):
                curr_node = curr_node.getLeft()
        return curr_node

    def empty(self):
        if self.root is None:
            return True
        return False

    def __InOrderTraversal(self, curr_node):
        nodeList = []
        if curr_node is not None:
            nodeList.insert(0, curr_node)
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getLeft())
            nodeList = nodeList + self.__InOrderTraversal(curr_node.getRight())
        return nodeList

    def getRoot(self):
        return self.root

    def __isRightChildren(self, node):
        if(node == node.getParent().getRight()):
            return True
        return False

    def __reassignNodes(self, node, newChildren):
        if(newChildren is not None):
            newChildren.setParent(node.getParent())
        if(node.getParent() is not None):
            #If it is the Right Children
            if(self.__isRightChildren(node)):
                node.getParent().setRight(newChildren)
            else:
                #Else it is the left children
                node.getParent().setLeft(newChildren)

    #This function traversal the tree. By default it returns an
    #In order traversal list. You can pass a function to traversal
    #The tree as needed by client code
    def traversalTree(self, traversalFunction=None, root=None):
        if(traversalFunction is None):
            #Returns a list of nodes in preOrder by default
            return self.__InOrderTraversal(self.root)
        else:
            #Returns a list of nodes in the order that the users wants to
            return traversalFunction(self.root)

    #Returns an string of all the nodes labels in the list
    #In Order Traversal
    def __str__(self):
        list = self.__InOrderTraversal(self.root)
        str = ""
        for x in list:
            str = str + " " + x.getLabel().__str__()
        return str
