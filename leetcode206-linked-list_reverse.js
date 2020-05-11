
// Definition for singly-linked list.
function ListNode(val) {
    this.val = val;
    this.next = null;
}

// @param {ListNode} head
// @return {ListNode}

var reverseList = function(head) {
    if(head == null || head.next == null) return head
    a = head
    a_1 = head.next
    a_2 = a_1.next
    while(a_2){
        a_1.next = a
        a = a_1
        a_1 = a_2
        a_2 = a_2.next
    }
    a_1.next = a
    head.next= null
    return a_1
};

var reverseList_recursion = function(head) {
    if(head == null || head.next == null) return head
    const node = reverseList_recursion(head.next)
    node.next = head
    head.next = null
    return node
}

var a = new ListNode(3)

reverseList(a)