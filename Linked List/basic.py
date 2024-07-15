# single link list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        # print('head', self.head.data)
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print('None')

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete_node(self, value):
        current = self.head
        # delete head
        if current and current.data == value:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if current is None:
            print('Data Not Found')
            return None
        
        # if data found
        prev.next = current.next
        current = None

ll1 = LinkedList()
ll1.insert_end(5)
ll1.insert_end(7)
ll1.insert_end(8)
ll1.insert_start(2)
ll1.print_list()
ll1.delete_node(9)
ll1.print_list()
