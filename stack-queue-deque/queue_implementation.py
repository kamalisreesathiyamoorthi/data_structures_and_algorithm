'''
QUEUE :
enqueue
dequeue
size
isempty
'''

class Queue :
    
    def __init__(self) :
        self.q = []
        
    def enqueue(self , item) :
        self.q.insert(0,item)
        
    def dequeue(self) :
        self.q.pop()
        
    def isEmpty(self) :
        return self.q == []
        
    def size(self) :
        return len(self.q)
    
    def print_queue(self) :
        print(self.q)
        
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)        
q.print_queue() #Output : [30, 20, 10]
q.dequeue()
q.print_queue() #Output : [30, 20]

print("IsEmpty : " , q.isEmpty()) #Output : IsEmpty :  False
print("size    : " , q.size()) #Output : size    :  2