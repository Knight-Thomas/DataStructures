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

    def extractor(self):
        '''method to remove items within the list'''
        try:
            index = int(input('Enter the index of the item to remove: '))
            #check if the index passed is within the range
            if index > self.lengthOf() or index<0:
                return None
            elif index == 0:
                self.head = self.head.next
            else:
                i=0
                while i<index:
                    previous = current_node
                    current_node = current_node.next
                    i+=1
                previous.next = current_node.next
                current_node.next = None
        except ValueError:
            print('Index must be a number')
            return None
    
    def lengthOf(self):
        'method to get length of list'
        current = self.head
        nodesVisited = 0
        while current.next != None:
            nodesVisited += 1
            current = current.next
        print(nodesVisited)
    
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
listy.appender(15)
listy.appender(75)
listy.display()
listy.lengthOf()
listy.extractor()