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
        
class My_queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def push(self, value):
        item = Node(value)
        print("adding new item:", str(item.get_value()))
        if self.empty():
            self.head = item
            self.tail = item
        else:
            self.tail.set_next_node(item)
            self.tail = item
        self.size += 1
        print("item successfuly added:", str(item.get_value()))
        return item.get_value()
        
    def pop(self):
        if not self.empty():
            to_remove = self.head
            print("removing item:", str(to_remove.get_value()))
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            print("item successfully removed:", str(to_remove.get_value()))
            return to_remove.get_value()
        else:
            print("empty, nothing to remove !")

    def peek(self):
        if not self.empty():
            print("top item:", str(self.head.get_value()))
            return self.head.get_value()  
        else:
            print("queue empty !")                  
                
    def empty(self):
        if self.size == 0:
            return True    
        else:
            return False        
                
my_q = My_queue()
my_q.push(1)
my_q.push(2)
my_q.peek()
my_q.pop()
print(my_q.empty())
my_q.peek()
my_q.pop()
print(my_q.empty())
my_q.peek()