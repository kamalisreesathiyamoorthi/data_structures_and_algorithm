'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
'''

from queue import deque
class MyStack:

    def __init__(self):
        self.s = deque()

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        for i in range(len(self.s) - 1) :
            self.s.append(self.s.popleft()) 
        return self.s.popleft()

    def top(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return len(self.s) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()