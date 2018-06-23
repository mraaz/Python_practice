class Nodes:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, value):
        self.nextNode = value

    def setData(self, value):
        self.data = value



class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def addNode(self, data):
        myNode = Nodes(data, self.head)
        self.head = myNode

    def countNodes(self):
        count = 0
        current = self.head
        while current:
            count+=1
            current = current.getNextNode()

        return count

    def pop(self):
        if (self.head):
            self.head = self.head.getNextNode()
        else:
            print("Error unable to pop empty list")

    def deleteNode(self, value):

        current = self.head
        prev = None
        while current:
            if (current.getData() == value):
                if (prev):
                    prev.setNextNode(current.getNextNode())

                else:
                    current.head = current.getNextNode()
            prev = current
            current = current.getNextNode()

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.getData())
            curr = curr.getNextNode()


def main():
    myList = LinkedList()
    myList.addNode(15)
    myList.addNode(12)
    myList.addNode(11)
    myList.pop()

    print (myList.printNode())


if __name__ == "__main__":
    main()

