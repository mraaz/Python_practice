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
        if currentNode.value == value:
            return
        
        if currentNode.value <= value:
            if currentNode.leftChild:
                self.insertNode(currentNode.leftChild, value)
            else:
                currentNode.leftChild = Node(value)
            
        if currentNode.value > value:
            if currentNode.rightChild:
                self.insertNode(currentNode.rightChild, value)
            else:
                currentNode.rightChild = Node(value)
    
    def printTree(self):
        if self.root == None:
            return
        else:
            self.printNode(self.root)
    
    def printNode(self, currentNode):
        if currentNode is not None:
            print(currentNode.value)
            self.printNode(currentNode.leftChild)
            self.printNode(currentNode.rightChild)
            
    
            
def findSecondBiggestNode(tree):
    biggestNode = Node(float('-inf'))
    secondNode = Node(0)
    
    
    def findNode(currentNode):
        if currentNode is not None:
            if currentNode.value > biggestNode.value:
                secondNode.value = biggestNode.value
                biggestNode.value = currentNode.value
                findNode(currentNode.rightChild)
                findNode(currentNode.leftChild)
            elif currentNode.value > secondNode.value:
                secondNode.value = currentNode.value
    
    if tree.root != None:
        findNode(tree.root)
    
    if secondNode.value == float('-inf'):
        print("Error, only one value found")
    print("Biggest Node is %s and second is %s" % (biggestNode.value, secondNode.value))
    
    
            
if __name__ == "__main__":
    myBST = BST()
    myBST.insert(112)
    myBST.insert(33)
    myBST.insert(141)
    myBST.insert(112)
    myBST.insert(84)
    myBST.insert(19)
    myBST.insert(23)
    myBST.insert(5)
    myBST.insert(11110)
    myBST.insert(0)
    myBST.insert(3)
    
    
    findSecondBiggestNode(myBST)
    
    #myBST.printTree()