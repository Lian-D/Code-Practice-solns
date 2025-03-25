class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
       
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        l1Curr = l1
        l2Curr = l2
        ret = ListNode(0)
        curr = ret
        
        while(l1Curr or l2Curr or carry > 0):
            valA = l1Curr.val if l1Curr else 0
            valB = l2Curr.val if l2Curr else 0 
            currVal = valA+valB+carry
            carry = 0
            
            if (currVal >= 10):
                curr.next = ListNode(currVal % 10)
                carry = 1
            else:
                curr.next = ListNode(currVal)    
                 
            l1Curr = l1Curr.next if l1Curr else None
            l2Curr = l2Curr.next if l2Curr else None
            
            curr = curr.next
        return ret.next
        
