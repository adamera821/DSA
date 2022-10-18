''''A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer. Python does not have linked lists in its standard library. We implement the concept of linked lists using the concept of nodes as discussed in the previous chapter.

We have already seen how we create a node class and how to traverse the elements of a node.In this chapter we are going to study the types of linked lists known as singly linked lists. In this type of data structure there is only one link between any two data elements. We create such a list and create additional methods to insert, update and remove elements from the list.''''

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node
    
class Linkedlist:
    def __init__(self, value=None):
        self.head_value = Node(value)
    
    def get_head(self):
        return self.head_value
    
    def inser_begining(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_value)
        self.head_value = new_node
    
    def stringify(self):
        stringfying = ""
        current_node = self.get_head()
        while current_node:
            if current_node.get_value() !=None:
                stringfying += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return stringfying
   ''' Code Removing node'''
    def remove_node(self, node_to_remove):
        current_node = self.get_head()
        if current_node.get_value() == node_to_remove:
            self.head_value = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == node_to_remove:
                    next_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
           
           
        
ll = Linkedlist(80)
ll.inser_begining(89)
ll.inser_begining(83)
ll.inser_begining(81)
ll.remove_node(89)
