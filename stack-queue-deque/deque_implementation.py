'''
DEQUE :
addLeft
addRight
removeLeft
removeRight
size
isempty
'''
class Deque :
    
    def __init__(self) :
        self.d = []
        
    def addLeft(self , item) :
        self.d.insert(0,item)
        
    def addRight(self , item) :
        self.d.append(item)
        
    def removeLeft(self) :
        self.d.pop(0)
    
    def removeRight(self) :
        self.d.pop()
        
    def isEmpty(self) :
        return self.d == []
    
    def size(self) :
        return len(self.d)
    
    def print_deque(self):
        print(self.d)
        
d = Deque()
d.addLeft(10)
d.print_deque() #Output : [10]
d.addLeft(20)
d.print_deque() #Output : [20, 10]
d.addRight(30)
d.print_deque() #Output : [20, 10, 30]

d.removeLeft()
d.print_deque() #Output : [10, 30]
d.removeRight()
d.print_deque() #Output : [10]

print("isEmpty : " , d.isEmpty()) #Output : isEmpty :  False
print("Size    : " , d.size()) #Output : Size    :  1