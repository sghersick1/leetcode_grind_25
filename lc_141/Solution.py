#imports
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        print(head[0].val)
        return True   

# create a linked list
def createLinkedList(values, pos):
    # not -> ! (negation)
    # special cases: [] -> True if empty, "" -> true is empty string, 0 -> true "empty" int
    if not values:
        return None
    
    node = []
    # create all of the nodes
    for i,v in enumerate(values):
        node.append(ListNode(v))

    # link the nodes
    for i in range(0, len(values)-1):
        node[i].next = node[i+1]

    #final node links to pos, or None if -1
    if pos == -1:
        node[i+1] = None
    else:
        node[i+1] = node[pos]

    return node

# main method
def main():
    sol = Solution()
    head = createLinkedList([3,2,0,-4], -1)
    res = sol.hasCycle(head)
    print(res)


if __name__ == "__main__":
    main()
