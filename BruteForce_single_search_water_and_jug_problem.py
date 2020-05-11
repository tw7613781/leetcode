
class Solution:

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z > x + y:
            return False
        if x > y:
            x,y=y,x
        state = set()
        max_x = x
        max_y = y
        x= max_x
        y = 0
        while x != z and y != z and (x+y) != z:
            if (x, y) in state:
                return False
            else:
                state.add((x,y))

            if x != 0 and y != max_y:
                temp = min(x, max_y-y)
                x = x-temp
                y = y+temp

            elif x == 0:
                x = max_x
            
            elif y == max_y:
                y = 0
        return True

solution = Solution()
print(solution.canMeasureWater(104693, 104701, 324244))
print(solution.canMeasureWater(104639, 104651, 234))
print(solution.canMeasureWater(104597, 104623, 123))