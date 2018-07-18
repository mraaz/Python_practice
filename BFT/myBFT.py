from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


def BFT(node):

    queue = deque([node])
    output = []

    while len(queue) > 0:
        current_node = queue.popleft()


        output.append(str(current_node.value))
        output.append("\n")

        if current_node.leftChild != None:
            queue.append(current_node.leftChild)

        if current_node.rightChild != None:
            queue.append(current_node.rightChild)

    return ''.join(output)


if __name__ == "__main__":
    root = Node(9)
    root.leftChild = Node(2)
    root.rightChild = Node(4)

    root.leftChild.leftChild = Node(1)
    root.leftChild.rightChild = Node(3)

    root.rightChild.leftChild = Node(5)
    root.rightChild.rightChild = Node(7)
    print (BFT(root))