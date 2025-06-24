'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

'''

import heapq
class MedianFinder(object):

    def __init__(self):
        self.small = [] # stores smaller elements - follows max heap  
        self.large = [] # stores larger elements - follows min heap 

    def addNum(self, num):
        # since python doesn't have build in max heap ,
        # have all the elements in negative as a minheap for small
        heapq.heappush( self.small , num * -1)

        #every element in small should be lesser than every element in large
        if self.large and self.small[0] * -1  > self.large[0] :
            # pop from the small and add it to large
            val = heapq.heappop(self.small) * -1 
            heapq.heappush( self.large , val)

        # check if uneven size 
        if len(self.small) > len(self.large) + 1 :
            # pop from the small and add it to large
            val = heapq.heappop(self.small) * -1 
            heapq.heappush( self.large , val)
        
        if len(self.large) > len(self.small) + 1 :
            # pop from the large and add it to small
            val = heapq.heappop(self.large)  
            heapq.heappush( self.small , val * -1)

    def findMedian(self):
        if len(self.small) > len(self.large) :
            return self.small[0] * -1
        if len(self.large) > len(self.small) :
            return self.large[0]
        return ( self.small[0] * -1 + self.large[0] ) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()