from linkList import node, linkedList

def main():
    myList = linkedList()
    for i in range(5):
        val = input("enter an int")
        myList.addEnd(val)
    myList.printList()
    #myList.removeIndex(2)
    #myList.printList()
    newNode = myList.getIndex(2)
    print(newNode.payload)

if __name__ == "__main__":
    main()
