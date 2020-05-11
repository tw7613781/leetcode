## https://leetcode.com/problems/water-and-jug-problem/
## Time Limit Exceeded

from collections import defaultdict

import sys
class Solution:
    def __init__(self):
        # state queue in case there is a duplicate state
        self.state = defaultdict(lambda: False)

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # define two jugs with capacity and current litres of water
        self.state[(0, 0)] = True
        if self.dfs((0, 0), x, y, z):
            print(True)
            return True
        else:
            print(False)
            return False
        

    def dfs(self, state, limit_a, limit_b, target):
        '''
         fs between six state transition actions:
         A -> Full, B -> Full, A -> B, B -> A, A -> 0, B -> 0
        '''
        # print(state)
        # successful conditon
        if state[0] == target or state[1] == target or state[0] + state[1] == target:
            return True
        # A -> Full
        new_state = (limit_a, state[1])
        if self.state[new_state] == False:
            self.state[new_state] = True
            return self.dfs(new_state, limit_a, limit_b, target)
        # B -> Full
        new_state = (state[0], limit_b)
        if self.state[new_state] == False:
            self.state[new_state] = True
            return self.dfs(new_state, limit_a, limit_b, target)
        # A -> B
        temp_a = state[0]
        temp_b = state[1]
        if temp_a != 0 and temp_b != limit_b:
            aval = limit_b - temp_b
            if temp_a <= aval:
                new_state = (0, temp_a + temp_b)
            else:
                new_state = (temp_a - aval, limit_b)
            if self.state[new_state] == False:
                self.state[new_state] = True
                return self.dfs(new_state, limit_a, limit_b, target)
        # B -> A
        temp_a = state[0]
        temp_b = state[1]
        if temp_b != 0 and temp_a != limit_a:
            aval = limit_a - temp_a
            if temp_b <= aval:
                new_state = (temp_a + temp_b, 0)
            else:
                new_state = (limit_a, temp_b - aval)
            if self.state[new_state] == False:
                self.state[new_state] = True
                return self.dfs(new_state, limit_a, limit_b, target)
        # A -> 0
        new_state = (0, state[1])
        if self.state[new_state] == False:
            self.state[(new_state)] = True
            return self.dfs(new_state, limit_a, limit_b, target)      
        # B -> 0
        new_state = (state[0], 0)
        if self.state[new_state] == False:
            self.state[(new_state)] = True
            return self.dfs(new_state, limit_a, limit_b, target)         
        
sys.setrecursionlimit(34000)
solution = Solution()
# solution.canMeasureWater(5,2,4)
# solution.canMeasureWater(2,6,5)
solution.canMeasureWater(22003,31237,1)
        
