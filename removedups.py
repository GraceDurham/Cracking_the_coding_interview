class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    class Node(object):

        def __init__(self, data):
            self.data = data
            self.next = None
    
    def append(self, data):
        
        new_node = self.Node(data)
        
        if self.head is None:
            self.head = new_node
            
        if self.tail is not None:
            self.tail.next = new_node
        
        self.tail = new_node
        
    def grab_head(self):
        head_node = self.head
        return head_node
        
    def delete_dups(self):
        
        current = self.head
        
        while current is not None:
            runner = current
        
            while runner.next is not None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                
                runner = runner.next

                current = current.next    

        
my_ll = LinkedList()
my_ll.append("apple")
my_ll.append("berry")
my_ll.append("berry")
my_ll.append("cherry")
my_ll.append("durian")
my_ll.append("durian")
my_ll.delete_dups()

def print_my_ll(current):
    if current is None:
        return
    print(current.data)
    print_my_ll(current.next)
    

print_my_ll(my_ll.grab_head())



        






        