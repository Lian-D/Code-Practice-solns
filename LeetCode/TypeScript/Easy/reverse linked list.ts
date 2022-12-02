// Runtime: 80 ms, faster than 93.23% of TypeScript online submissions for Reverse Linked List.
//     Memory Usage: 40.6 MB, less than 79.08% of TypeScript online submissions for Reverse Linked List.

 class ListNode {
     val: number
     next: ListNode | null
     constructor(val?: number, next?: ListNode | null) {
         this.val = (val===undefined ? 0 : val)
         this.next = (next===undefined ? null : next)
     }
}

function reverseList(head: ListNode | null): ListNode | null {
    let prev: ListNode = null;
    let curr: ListNode = head;
    while (curr !== null) {
        let next: ListNode = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
};