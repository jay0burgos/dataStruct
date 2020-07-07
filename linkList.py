class node:
    def __init__(self,value = None):
        self.payload = value
        self.next = None
        #None is same as null

class linkedList:
    def __init__(self, value = None):
        if value == None:
            self.head = None
            self.end = None
            self.count = 0
        else:
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
        if currentNode == None:
            return None
        elif currentNode.payload == value:
            return currentNode
        else:
            self.search(value, currentNode.next, index + 1)
    def printList(self):
        currentND = self.head
        for i in range(self.count):
            print(currentND.payload)
            currentND = currentND.next
    def remove(self, value = None):
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
        


                



