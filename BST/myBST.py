class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.insertNode(self.root, value)

    def insertNode(self, currentNode, value):
        if value == currentNode.value:
            return
        if value <= currentNode.value:
            if currentNode.leftChild:
                self.insertNode(currentNode.leftChild, value)
            else:
                    currentNode.leftChild = Node(value)
        if value > currentNode.value:
            if currentNode.rightChild:
                self.insertNode(currentNode.rightChild, value)
            else:
                currentNode.rightChild = Node(value)

    def printTree(self):
        if self.root is None:
            print("Nothing to print")
        else:
            self.printNode(self.root)

    def printNode(self, currentNode):
        if currentNode is not None:
            self.printNode(currentNode.leftChild)
            print(currentNode.value)
            self.printNode(currentNode.rightChild)


if __name__ == "__main__":
    myBST = BST()
    myBST.insert(112)
    myBST.insert(33)
    myBST.insert(141)
    myBST.insert(112)
    myBST.insert(15)
    myBST.printTree()