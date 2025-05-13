'''
Solution first time solving, works fine, code would be simplified.

My choices:
- check edge cases (any empty lists) and return
- initialize new merged node -> make head (for returning)
- go through two lists until both run out of nodes, compare values and add to merged list

Better Solution:
- Create a dummy node -> allows us to not check for edge cases by returning dummy.next (will be None if both lists are empty)
- create tail = dummy, we can iterate through this but still have correct node to return head at end
- Iterate through while both lists arent empty, add to dummy.next
- After atleast 1 list is empty, add remaining list (if applicable) to end of tail + return 

Alternative Option:
- Use recursion and call method recursively with smaller l1 & l2 each time
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Handle edge cases
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        #initialize merged list
        if list1.val < list2.val:
            merged = list1  
            list1 = list1.next
        else:
            merged = list2
            list2 = list2.next

        head = merged
        while list1 or list2:
            if not list2 or (list1 and list1.val < list2.val):
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            
            merged = merged.next

        return head
        
