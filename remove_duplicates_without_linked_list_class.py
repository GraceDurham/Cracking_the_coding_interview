class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_dups(current):

    new_set = set()

    previous = None

    while current is not None:
        if current.data in new_set:
            previous.next = current.next
        else:
            new_set.add(current.data)
            previous = current

        current = current.next     

# You could loop over something like this and create nodes:
example_data = ["apple", "berry", "cherry", "cherry", "durian", "durian"]

start_node = Node(example_data.pop(0))
current_node = start_node

for string in example_data:
    current_node.next = Node(string)
    current_node = current_node.next
    
delete_dups(start_node)
        
    
def print_ll(node):
    if node is None:
        return
    print (node.data)
    print_ll(node.next)
#recursivly print out node 
#recursivly print out list = 

print_ll(start_node)

    
    
    
    
    
    





        
        
        
        
        
        
        
        
        
        

