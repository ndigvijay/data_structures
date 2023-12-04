class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            current=self.head
            while current is not None:
                print(current.data)
                current=current.next
    def insert_at_front(self,data):
        temp=Node(data)
        if self.head is None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp
    def insert_at_back(self,data):
        temp=Node(data)
        if self.head is None:
            self.head=temp
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=temp
    def delete_at_front(self):
        if self.head is None:
            print("list is empty u cant delete")
        else:
            self.head=self.head.next
    def delete_at_back(self):
        if self.head is None:
            print("list is empty, u cant delete")
        elif self.head.next is None:
            self.head=None
        else:
            prev=None
            current=self.head
            while current.next is not None:
                prev=current
                current=current.next
            prev.next=None




if __name__=="__main__":
    ll1=LinkedList()
    ll1.display()
    ll1.insert_at_back(10)
    ll1.delete_at_back()
    ll1.insert_at_back(20)
    ll1.insert_at_back(30)
    ll1.insert_at_back(40)
    ll1.display()
    ll1.delete_at_back()
    ll1.display()




    