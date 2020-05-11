## https://leetcode.com/problems/water-and-jug-problem/
## Time Limit Exceeded

from collections import defaultdict

class Solution:
    def __init__(self):
        # state queue in case there is a duplicate state
        self.state = defaultdict(lambda: False)
        # system q for bfs
        self.q = []

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # define two jugs with capacity and current litres of water
        self.x = x
        self.y = y
        self.target = z
        # push initial statu to system Q
        initial_state = (0, 0)
        self.q.append(initial_state)
        # loop condition, continue whenever system Q has state element
        while len(self.q) != 0:
            # pop out first state
            c_state = self.q.pop(0)
            self.state[c_state] = True
            if c_state[0] == self.target or c_state[1] == self.target or c_state[0] + c_state[1] == self.target:
                return True
            # A -> Full
            new_state = (self.x, c_state[1])
            if self.state[new_state] != True:
                self.q.append(new_state)
            # B -> Full
            new_state = (c_state[0], self.y)
            if self.state[new_state] != True:
                self.q.append(new_state)            
            # A -> B
            aval = self.y - c_state[1]
            if c_state[0] <= aval:
                new_state = (0, c_state[0] + c_state[1])
            else:
                new_state = (c_state[0] - aval, self.y)
            if self.state[new_state] != True:
                self.q.append(new_state)            
            # B -> A
            aval = self.x - c_state[0]
            if c_state[1] <= aval:
                new_state = (c_state[0] + c_state[1], 0)
            else:
                new_state = (self.x, c_state[1] - aval)
            if self.state[new_state] != True:
                self.q.append(new_state)            
            # A -> 0
            new_state = (0, c_state[1])
            if self.state[new_state] != True:
                self.q.append(new_state)            
            # B -> 0
            new_state = (c_state[0], 0)
            if self.state[new_state] != True:
                self.q.append(new_state)        
        return False 