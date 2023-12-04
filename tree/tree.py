class TreeNode:
    def __init__(self,data) -> None:
        self.data=data
        self.left=None
        self.right=None


class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root=self._insert(self.root,data)
    def _insert(self,root,data):
        temp=TreeNode(data)
        if root is None:
            root=temp
            return root
        else:
            current=root
            while current is not None:
                if current.data>data:
                    if current.left is None:
                        current.left=temp
                        break
                    else:
                        current=current.left
                elif current.data<data:
                    if current.right is None:
                        current.right=temp
                        break
                    else:
                        current=current.right
            return root
    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, root, level):
        if root is not None:
            self._print_tree(root.right, level + 1)
            print("   " * level + str(root.data))
            self._print_tree(root.left, level + 1)
    def search(self,data): 
        if self.root is None:
            print("tree is empty")
        elif data==self.root.data:
            return 1
        else:
            current=self.root
            while current is not None:
                if current.data>data:
                    current=current.left
                elif current.data<data:
                    current=current.right
                elif current.data==data:
                    return 1
            return -1
    
    def preorder(self):
        self._preorder(self.root)
    def _preorder(self,root):
        if root is None:
            return None
        print(root.data,end=" ")
        self._preorder(root.left)
        self._preorder(root.right)
        





if __name__=="__main__":
    bt=BinaryTree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    bt.insert(3)
    bt.insert(7)
    bt.insert(12)
    bt.insert(18)
    # bt.print_tree()
    # result=bt.search(14)
    # print(result)
    bt.preorder()

