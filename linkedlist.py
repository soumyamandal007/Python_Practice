class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print('LinkedList is empty')
            return
        
        itr = self.head #it is the current node just as we dont want to change the head.
        listr = ''
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next 
        print(listr)
        
    def insert_at_end(self,data):
        if self.head is None:  #when the list is null we have to just put node as the last element
            self.head = Node(data,None)
            return
        #if the list is not null
        itr = self.head
        while itr.next: # while itr.next has some value it will keep on iterating and upto when the itr.next is None
            itr = itr.next
        itr.next = Node(data,None)  # now we have to just assign the node at the end with none as its next 
        
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception('Not a valid index')
        if index == 0:
            self.head = self.head.next
            return
        # need to improvise the memory eak so that none cant get the atter list through the leaked node.
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next #pointing next to the next to next node
                break
            
            itr = itr.next
            count += 1
    
    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid')
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1   
    
    def insert_after_value(self,data_after,data_insert):
        itr = self.head #the current node
        while itr: # while the next is not null
            if itr.data == data_after:
                node = Node(data_insert,itr.next) # here crearting a new node with value and next pointing towards the latest itr instance's next node
                itr.next = node # now we connect the latest itr instance and new created node
                
            itr = itr.next 
    def remove_by_value(self,data_remove):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data_remove:
                self.remove_at(count)
                break
            itr = itr.next 
            count += 1  
         
        

if __name__ == '__main__':
    li = LinkedList()
    # li.insert_at_begining(5)
    # li.insert_at_begining(89)
    # li.insert_at_begining(890)
    # li.insert_at_end(789)
    # li.insert_at_end(89089)
    li.insert_values(["soumya","amar","dhwanil","haarshal"])
    li.print()
    li.insert_after_value("amar","kajal")
    li.print()
    li.remove_by_value("kajal")
    li.print()
    print('Length is ' ,  li.get_length())
    # check