class Solution:
    def canMeasureWater(self, x, y, z):
        if(z <0 or x+y < z):
            return False

        q = []
        q.append(0)
        s=set()
        while(len(q) is not 0):
            n = q.pop()
            if(n+x <= x+y and (n+x) not in s):
                s.add(n+x)
                q.append(n+x)
            if(n+y <= x+y and (n+y) not in s):
                s.add(n + y)
                q.append(n+y)
            if(n-x >=0 and (n-x) not in s):
                s.add(n - x)
                q.append(n-x)
            if(n-y >=0 and (n-y) not in s):
                s.add(n -y)
                q.append(n-y)
            if(z in s):
                return True

        return False