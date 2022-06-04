class Tree(object):
    
    def __init__(self, root, left=None, right=None):
        assert root and type(root) == Node
        if left: assert type(left) == Tree and left.root < root
        if right: assert type(right) == Tree and root < right.root

        self.left = left
        self.root = root
        self.right = right
        
    def is_leaf(self):
        return not(self.left or self.right)
        
    
    def __str__(self):
        if not self.left:
            if not self.right:
                return "[" + self.root.value + "]"
            else:
                return "[_ " + self.root.value + " " + self.right.__str__() + "]"
        elif not self.right:
            return "[" + self.left.__str__() + " " + self.root.value + " _]"
        else:
            return "[" + self.left.__str__() + " " + self.root.value + " " + self.right.__str__() + "]"
        return "[]"

    
    def __eq__(self, other):
        if not self or not other:
            return False
        if self.root.value != other.root.value:
            return False
        else:
            return self.left.__eq__(other.left) and self.right.__eq__(other.right)
    
    def __ne__(self, other):
        if not self or not other:
            return True;
        if self.root.value != other.root.value:
            return True
        else:
            return self.left.__ne__(other.left) or self.right.__ne__(other.right)
            

class Node(object):
    
    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight
    
    def __str__(self):
        return str(self.value)   
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __eq__(self, other):
        return self.value == other.value 

    def __ne__(self, other):
        return self.value != other.value
