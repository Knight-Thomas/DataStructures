class Node:
    '''Node class implentation'''
    def __init__(self, data=None):
        '''constructor method'''
        self.data = data #data point to be stored
        self.next = None

class LinkedList:
    '''LinkedLinst class implentation'''
    def __init__(self):
        '''constructor method'''
        self.head = Node()
    
    def appender(self, data):
        '''method to add items to the list'''
        self.data = data
        newNode = Node(data)
        current = self.head
        #iterate over existing list until the tail nodde
        while current.next != None:
            #traverse through the list
            current = current.next
        current.next = newNode
        #make the next node the new node
    
    def lengthOf(self):
        'method to get length of list'
    
    def display(self):
        'method to display list'
        myList = []
        current = self.head
        while current.next != None:
            current = current.next
            myList.append(current.data)
        print(myList)

listy = LinkedList()
listy.appender(5)
listy.appender(9)
listy.display()