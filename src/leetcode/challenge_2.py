class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        node = head
        carry = 0
        a, b = l1, l2
        
        while a or b:
            
            a_num = a.val if a else 0
            b_num = b.val if b else 0
            
            tot = a_num + b_num + carry
            carry = tot >= 10
            tot %= 10
            
            node.val = tot
            node.next = ListNode()
            last = node
            node = node.next
            
            a, b = a.next if a else None, b.next if b else None
        
        last.next = None if not carry else ListNode(int(carry))
        
        return head
