 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

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
    

    