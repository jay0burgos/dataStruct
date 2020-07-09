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

        


                





                



