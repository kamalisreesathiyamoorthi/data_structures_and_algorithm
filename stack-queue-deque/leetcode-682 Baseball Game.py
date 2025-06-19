'''
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

1.An integer x - Record a new score of x.
2.'+' - Record a new score that is the sum of the previous two scores.
3.'D' - Record a new score that is the double of the previous score.
4.'C' - Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
'''

class Solution(object):
    def calPoints(self, ops):
        stack = []
        sum = 0
        for i in ops :
            if i == "+" :
                score = stack[-1]+stack[-2]
                stack.append(score)
                sum = sum + score
            elif i == "D" :
                score = stack[-1]*2
                stack.append(score)
                sum = sum + score
            elif i == "C" :
                removed = stack.pop()
                sum = sum - removed
            else :
                score = int(i)
                stack.append(score)
                sum = sum + score
    
        return sum
        


class Solution(object):
    def calPoints(self, ops):
        stack = []
        sum = 0
        for i in ops:
            if i == "+":
                stack.append(stack[-1] + stack[-2])
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        
        # for i in stack:
        #     sum = sum + i
        return sum(stack)