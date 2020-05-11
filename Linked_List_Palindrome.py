class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def CheckLinkPalindrome(self,head):
        # type head: ListNode
        # rtype: bool
        run = head
        count = 0
        while run:
            run = run.next
            count += 1
        if count == 1 or count == 0:
            return True
        half = int(count/2)
        tail = head
        front = head.next
        print(half)
        print(count)
        while half:
            front = front.next
            tail = tail.next
            half -= 1
        tail.next = None
        while front:
            temp = front.next
            front.next = tail
            tail = front
            front = temp
        run = head
        while tail:
            if run.val != tail.val:
                return False
            run = run.next
            tail = tail.next
        return True

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

s = []
s = [1,2,1]
s = ['a','b']
solution = Solution()
s = solution.buildLinkedList(s)
solution.printLinkedList(s)
print('--------------------------')
ans = solution.CheckLinkPalindrome(s)
print(ans)
