class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        current=self.head
        if self.head is None and self.tail is None:
            print("list is empty")
        else:
            while current is not None:
                print(current.data)
                current=current.next
    def insert_at_front(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp