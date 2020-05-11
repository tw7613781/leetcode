class ListNode:
    def __init__(self,x):
        self.value = x
        self.next = None

class Solution:
    def deleteDuplicates(self,head):
        # type head: Linked Node
        # rtype: ListNode
        slow = head
        if slow == None:
            return head
        fast = head.next
        while(fast != None):
            if fast.value == slow.value:
                fast = fast.next
                slow.next = fast
            else:
                slow = fast
                fast = fast.next
        return head

    def buildLinkedList(self,s):
        # type s: integer array
        # rtype: ListNode
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
            print(run.value)
            run = run.next


s = [1,2,2,3,3]
s = [1,2,3]
s = [2,2]
s = [2]
s = [1,1,2]
solution = Solution()
head = solution.buildLinkedList(s)
solution.printLinkedList(head)
print('--------------------------')
head = solution.deleteDuplicates(head)
solution.printLinkedList(head)
