'''
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.


Example 1:
Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

'''


class FreqStack(object):

    def __init__(self):
        self.count_map = {} # to keep track of value-freq pairs
        self.stack_map = {} # to keep track of freq-[values] pairs
        self.max_count = 0  # count of the most frequency element

    def push(self, val):
        new_count = self.count_map.get(val , 0 ) + 1
        self.count_map[val] = new_count
        if new_count > self.max_count :
            self.max_count = new_count 
            self.stack_map[new_count] = []
        
        self.stack_map[new_count].append(val)

    def pop(self):
        value_to_pop = self.stack_map[self.max_count].pop()
        if self.stack_map[self.max_count] == [] :
           self. max_count -= 1
        self.count_map[value_to_pop] -= 1
        return value_to_pop
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()