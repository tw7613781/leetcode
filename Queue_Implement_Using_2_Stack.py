# [EASY]232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/
# The idea is to simulate a queue using two stacks. I use python list as the underlying data structure for stack: it moves all elements of the "inStack" to the "outStack" when the "outStack" is empty. Here is the code

class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.StackIn = []
        self.StackOut = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.StackIn.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.StackOut:
            return self.StackOut.pop()
        else:
            while self.StackIn:
                temp = self.StackIn.pop()
                self.StackOut.append(temp)
            if self.StackOut:
                return self.StackOut.pop()
            else:
                return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.StackOut:
            return self.StackOut[-1]
        else:
            while self.StackIn:
                temp = self.StackIn.pop()
                self.StackOut.append(temp)
            if self.StackOut:
                return self.StackOut[-1]
            else:
                return None
    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.StackIn or self.StackOut:
            return False
        else:
            return True

myQueue = MyQueue()
myQueue.push(1)
# myQueue.push(2)
# myQueue.push(3)
# myQueue.push(4)
# print(myQueue.pop())
print(myQueue.peek())
print(myQueue.empty())

