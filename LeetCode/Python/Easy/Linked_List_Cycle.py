# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def hasCycle(self, head):
        if ( head == None or head.next == None):
            return False
        else: 
            slow = head
            fast = head
            while (fast and fast.next):
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False
    

    