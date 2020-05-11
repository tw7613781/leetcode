import sys

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append((x,min(x,self.getMin())))

    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1][1]
        else:
            return sys.maxsize



# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(-3)
minStack.push(-4)
print(minStack.getMin())
minStack.pop()
minStack.pop()
print(minStack.top())
print(minStack.getMin())