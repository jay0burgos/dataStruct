class node:
    def __init__(self,value = None):
        self.payload = value
        self.next = None
        #None is same as null

class linkedList:
    def __init__(self, value = None):
        #keeps track of head and end while also keeps count of all the nodes
        if value == None:
            #if no initial value is given, pointers are null and count is set at 0
            self.head = None 
            self.end = None
            self.count = 0
        else:
            #if value is given at initialization, both head and end point to initial node
            self.head = node(value)
            self.end = node(value)
            self.count = 1
    def addEnd(self, value):
        if self.head == None:
            self.head = self.end = node(value)
            self.count +=1
        else:
            current = node(value)
            self.end.next = current
            self.end = current
            self.count +=1
    def search(self, value, currentNode, index = 1):
        #recursive search method, work in progess
        if currentNode == None:
            return None
        elif currentNode.payload == value:
            return currentNode
        else:
            self.search(value, currentNode.next, index + 1)
    
    def getIndex(self, index): #returns the node by its 'index', will eventually turn it into a recursive function
        currentNode = self.head
        for i in range(1,index):
            currentNode = currentNode.next
        return currentNode

    def printList(self):
        currentND = self.head
        for i in range(self.count):
            print(currentND.payload)
            currentND = currentND.next

    def removeIndex(self, value = None):
        #removes index
        if value is None or value <= 0:
            print("Invalid value")
        else:
            if value == 1:
                self.head = self.head.next
                self.count -=1
                return
            priorND = None
            currentND = self.head
            for i in range(value-1):
                priorND = currentND
                currentND = currentND.next
            priorND.next = currentND.next
            self.count-=1

    def prePend(self, value, nodeVal): #prepends the node containing nodeVal in its payload with a node containing value
        #assumes no user error, assumes nodeVal is the same variable type
        parentNode = self.head
        currentNode = self.head
        if self.head.payload == nodeVal:
            NewNode = node(value)
            NewNode.next = self.head
            self.head = NewNode
            return
        while currentNode.payload != nodeVal:
            parentNode = currentNode
            currentNode = currentNode.next
        NewNode = node(value)
        NewNode.next = currentNode
        parentNode.next = NewNode
        return

    def postPend(self, value, nodeVal): #finds node with value nodeVal, and appends it as next on the list
        currentNode = self.head
        while currentNode.payload != nodeVal:
            currentNode = currentNode.next
        newNode = node(value)
        newNode.next = currentNode.next
        currentNode.next = newNode
        return

    def removeVal(self, nodeVal): #finds node with value nodeVal, and deletes it wihtout breaking the link to the rest of the nodes
        parentNode = self.head
        currentNode = self.head
        while currentNode.payload != nodeVal:
            parentNode = currentNode
            currentNode = currentNode.next
        parentNode.next = currentNode.next
        return
    
    def minToFront(self): #tracks four nodes, a current node and its parent 
        minNode = self.head #and the current minNode and its parent containing the node being compared to
        minNodeParent = None

        currentNode = minNode.next
        currentNodeParent = minNode
        while currentNode.next != None:
            if minNode.payload > currentNode.payload:
                minNode = currentNode
                minNodeParent = currentNodeParent
            currentNodeParent = currentNode
            currentNode = currentNode.next
        currentNodeParent.next = currentNode.next
        currentNode.next = self.head
        self.head = currentNode
        return

                

        


        


                





                



