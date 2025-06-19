class Stack :
    
    def __init__(self) :
        self.s = []
        
    def push(self , item) :
        self.s.append(item)
        
    def pop(self) :
        self.s.pop()
    
    def showLast(self) :
        return self.s[-1]
    
    def isEmpty(self) :
        return self.s == []
    
    def size(self) :
        return len(self.s)
    
    def printing_stack(self) :
        print(self.s)
        

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.printing_stack() #Output : [10, 20, 30]
s.pop()
s.printing_stack() #Output : [10, 20, 30]
print("ShowLast : " , s.showLast()) #Output : ShowLast :  20
print("IsEmpty  : " , s.isEmpty()) #Output : IsEmpty  :  False
print("Size     : " , s.size()) #Output : Size     :  2

        