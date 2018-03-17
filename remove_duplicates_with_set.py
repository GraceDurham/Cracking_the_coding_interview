#Remove duplicates with a set and create linked list with list and for loop

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

print_ll(start_node)
      
