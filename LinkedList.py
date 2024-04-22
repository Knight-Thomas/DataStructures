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
        node = self.head
        while self.next != None:
            ''

    