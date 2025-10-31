class Node:
    def __init__(self, name: str, value: bool, parent=None, children: list=None):
        self.name = name
        self.value = value
        self.parent = parent
        self.children = children or []
        
    def add_parent(self, parent_node):
        self.parent = parent_node    
        
node_6= Node("node_6", False, None, []) 
node_5 = Node("node_5", False, None, [])    
node_4 = Node("node_4", False, None, [node_6])
node_3 = Node("node_3", False, None, [node_5])
node_2 = Node("node_2", False, None, [])    
node_1 = Node("node_1", False, None, [node_2, node_3, node_4])

node_6.add_parent(node_4)
node_5.add_parent(node_3)
node_4.add_parent(node_1)
node_3.add_parent(node_1)
node_2.add_parent(node_1)

def back_to_root(node: Node) -> Node: #checled with AI for return value, didn't know I can put NOde as a return value !
    while node.parent != None:
        node = node.parent
    return node    

def seek_for_truth(node: Node) -> bool:
    if node.value == True:
        return True
    for child in node.children:
        if seek_for_truth(child):
            return True
    return False    
        
def is_public(node: Node) -> bool:
    root = back_to_root(node)
    return seek_for_truth(root) # I also debug with AI at this part of the code to understand that I can just return it that way, previous code a bit more longer.
            
    
    
# Examples:
print(is_public(node_1))
print(is_public(node_2)) 
print(is_public(node_3)) 
print(is_public(node_4)) 
print(is_public(node_5)) 