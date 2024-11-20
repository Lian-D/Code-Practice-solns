class Solution(object):
    def reverseListIterative(self, head):
        prevNode = None # Create Previous Node Pointer
        currNode = head # Create Currend Pointer

        while currNode:
            nextNode = currNode.next # Create Next Node Pointer 
            currNode.next = prevNode # Set the next Node to the previous Node
            prevNode = currNode #update the previous node with the currend node
            currNode = nextNode # Make the currend node the archived next node
        return prevNode
    
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        res  = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res