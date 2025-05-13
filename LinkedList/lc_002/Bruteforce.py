'''
- one node at a time go through the two lists and add values + carry from previous addition
- at end if there is left over carry, add necessary node
- iterative

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ListNode() #head, for return
        tail = sum #for iteration
        carry = 0

        while l1 or l2:
            #add sum of digit + carry to result node
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            tail.val = total%10

            #update carry
            carry = int(total/10)

            #iterate two numbers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 or l2:
                #iterate to next node
                tail.next = ListNode()
                tail = tail.next
        
        # If carry = 1 after going through lists, carrying digit is added
        if carry:
            tail.next = ListNode(1)
        
        return sum
