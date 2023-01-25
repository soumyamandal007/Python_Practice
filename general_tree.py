class TreeNode:
   def __init__(self,name,designation):
      self.name = name
      self.designation = designation
      self.children = []
      self.parent = None

   def add_child(self,child):
      #child.parent = self
      self.children.append(child)
   
   def get_level(self):
      level = 0
      p =self.parent
      while p:
         level += 1
         p = p.parent
      return level
      
   def print_tree(self,phrase,level =0):
      spaces = ' ' * (level) * 3
      prefix = spaces 
      #+ "|__" if self.parent else ""
      if phrase == "name":
         print(prefix + self.name)
      elif phrase == "designation":
         print(prefix + self.designation)
      else:
         print(prefix + self.name,self.designation)
      if self.children:
         for child in self.children:
            child.print_tree(phrase,level+1)

def build_tree_method():
   root = TreeNode("Nilupal","CEO")
   
   chinmoy = TreeNode("Chinmoy","CTO")
   vishwa = TreeNode("Vishwa","Infrastructure Head")
   chinmoy.add_child(vishwa)
   vishwa.add_child(TreeNode("Dhaval","Cloud Manager"))
   vishwa.add_child(TreeNode("Abhijit","App Manager"))
   chinmoy.add_child(TreeNode("Aamir","Application Head"))
   gels = TreeNode("Gels","HR Head")
   gels.add_child(TreeNode("Peter","Recruitment Manager"))
   gels.add_child(TreeNode("Waqas", "Policy Manager"))
   
   root.add_child(chinmoy)
   root.add_child(gels)
   
   return root
   

if __name__ == '__main__':
   root_node = build_tree_method()
   root_node.print_tree("name")