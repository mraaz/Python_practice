"""

Purpose of this file is to practice Arrays

"""

class Arrays:

    def __init__(self, array):
        self.array = array

    def PopLastItem(self):

        self.array.pop()

    def removeItemFromArray(self, value):
        self.array.remove(value)


    def addItemtoArray(self, value):
        self.array.append(value)


def main():

    myarray = Arrays([1,2,3,4])
    print(myarray.array)

    myarray.PopLastItem()
    print(myarray.array)

    myarray.removeItemFromArray(2)
    print(myarray.array)

    myarray.addItemtoArray(9)
    print(myarray.array)


    try:
        print("Index of 2: ", myarray.array.index(1))
        myarray.array.remove(4)
        print("GOT here")

    except ValueError:
        print("Index Error; Not Found")

    myarray.array.reverse()

    print(myarray.array)

    print ("Sorted in return ", sorted(myarray.array))

    myarray.array.sort()
    print("Sorted in place ", myarray.array)



if __name__ == "__main__":
    main()



