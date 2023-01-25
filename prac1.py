class HashTable:
   def __init__(self):
      self.MAX = 100
      self.arr = [None for i in range(self.MAX)] #list comprehension, making a null list
      
   def get_hash(self,key):
      sum = 0
      for char in key:
         sum += ord(char)
      return sum % self.MAX

   def add(self,key,value):
      h = self.get_hash(key)
      self.arr[h] = value
   
   def get(self,key):
      h = self.get_hash(key)
      print(self.arr[h])
      return self.arr[h]
   
 
if '__name__' == '__main__':  
   t = HashTable()
   t.get_hash("march 6")
   t.add("march 6",130)
   t.get("march 6")
   print('po')
      
   

