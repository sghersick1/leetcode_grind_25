#imports
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# create linked list
def linkedList(values, pos):
    size = len(values)

    #create last node
    tail = ListNode(values[size-1])
    prev = tail
    for i in range(size-2, 0, -1):
        cur = ListNode(values[i])
        cur.next = prev
        prev = cur
        
        if i == pos:
            tail.next = cur
    
    return cur

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       visited = set()
       current = head

       while current:
           if current in visited:
               return True 
           visited.add(current)
           current = current.next 

       return False
# main method
def main():
    head = linkedList([3,2-1,0,4], -1)
    sol = Solution()
    print(sol.hasCycle(head))

if __name__ == "__main__":
    main()
