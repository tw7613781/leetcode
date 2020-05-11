'''
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]
'''

class Solution: 
    def getRange(self, arr, target):
        return [self.find_first(arr, target), self.find_last(arr, target)]

    def find_first(self, arr, target):
        l = 0
        r = len(arr)-1
        while l<=r:
            mid = (l+r+1)//2
            if target <= arr[mid]:
                r = mid-1
            else: l = mid+1
        if l<0 or l>len(arr)-1 or arr[l] != target:
            return -1
        else: return l
    
    def find_last(self, arr, target):
        l = 0
        r = len(arr)-1
        while l<=r:
            mid = (l+r+1)//2
            if target < arr[mid]:
                r = mid-1
            else: l = mid+1
        if r<0 or r>len(arr)-1 or target != arr[r]:
            return -1
        else: return r
    
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]