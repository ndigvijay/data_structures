class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if(self.isempty):
            print("stack is empty")
        else:
            ele=self.stack.pop()
            print("popped..........",ele,"\n")
    def peek(self):
        if(self.isempty):
            print("stack is empty")
        else:
            ele=self.stack[-1]
        print("peeking ...........",ele,"\n")
    def print(self):
        print(self.stack)
    def isempty(self):
        if self.stack==[]:
            return True
        return False
    



if __name__=="__main__":
    stk1=Stack()
    stk1.push(5)
    stk1.push(10)
    stk1.push(15)
    stk1.pop()
    stk1.peek()
    stk1.print()


