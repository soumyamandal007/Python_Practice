class Node:
   def __init__(self,value):
      self.value = value
      self.left = None
      self.right = None

class BST:
   def __init__(self):
      self.root = None
   global elements
   elements = []
   def add(self,data):
      if not self.root:
         self.root = Node(data)
      current = self.root
      while True:
         if data < current.value:
            if not current.left:
               current.left = Node(data)
               break
            current = current.left
         else:
            if not current.right:
               current.right = Node(data)
               break
            current = current.right
   
   def buildtree(self,inputdata):
      self.root = Node(inputdata[0])
      for i in range(1,len(inputdata)):
         self.add(inputdata[i])
   
   def in_order_traversal(self,node):
      if not node:
         return
      self.in_order_traversal(node.left)
      elements.append(node.value)
      self.in_order_traversal(node.right)
      return elements
      
   def pre_order_traversal(self,node):
      if not node:
         return 
      self.pre_order_traversal(node.left)
      self.pre_order_traversal(node.right)
      elements.append(node.value)
      return elements
   
   def printtree(self,trav):
      if trav == "inorder":
         ans = self.in_order_traversal(self.root)
         print(ans)
      elif trav == "preorder":
         ans = self.pre_order_traversal(self.root)
         print(ans)
      
   
      

if __name__ == '__main__':
   
   sam = BST()
   sam.buildtree([78,45,34,23,12,89,67])
   # sam.root = Node(10)
   # sam.add(45)
   # sam.add(56)
   # sam.add(89)
   # sam.add(43)
   # sam.add(23)
   # sam.add(78)
   # sam.add(85)
   sam.printtree("preorder")
   