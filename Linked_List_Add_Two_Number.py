class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def AddTwoNumber(self,l1,l2):
        # type l1: Linked Node
        # type l2: linked Node
        ans = l2
        while(l1 != None and l2 != None):
            sum = l1.val + l2.val
            carry = 0
            if sum > 9:
                sum = sum % 10
                carry = 1
            l2.val = sum
            if carry == 1 and l2.next != None:
                l2.next.val += 1
            if carry == 1 and l2.next == None:
                l2.next = ListNode(1)
            l1 = l1.next
            if l2.next == None:
                l2.next = l1
                break
            else:
                l2 = l2.next
        while l2.val > 9:
            l2.val = l2.val % 10
            if l2.next != None:
                l2.next.val += 1
            else:
                l2.next = ListNode(1)
                break
            l2 = l2.next
        return ans

    def buildLinkedList(self,s):
        # type s: integer array
        # rtype: ListNode
        if len(s) == 0:
            return None
        i = 1
        head = ListNode(s[0])
        run = head
        while i < len(s):
            node = ListNode(s[i])
            run.next = node
            run = node
            i += 1
        return head

    def printLinkedList(self,head):
        # type head: ListNode
        # rtype: None
        run = head
        while run != None:
            print(run.val)
            run = run.next


a = [1,2,3]
b = [1,2,3]
a = [5,6]
b = [2,4,3,3]
solution = Solution()
l1 = solution.buildLinkedList(a)
solution.printLinkedList(l1)
l2 = solution.buildLinkedList(b)
solution.printLinkedList(l2)
print('--------------------------')
ans = solution.AddTwoNumber(l1,l2)
solution.printLinkedList(ans)

#
# test data
# [2,4,3]
# [5,6,4]
# [1,1,1]
# [9,9,9]
# [1,1,1]
# [0,9,9]
# [2,4,3,3,3,3]
# [5,6,4]
# [5,6,4]
# [2,4,3,3,3,3]
# [0]
# [3,2,4,5]
# [3,2,4,5]
# [0]
# [1]
# [9,9]
# [9,9]
# [1]
# [1]
# [9,9,9,9,9,9,9]
# [9,9,9,9,9,9,9]
# [1]