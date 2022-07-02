//Runtime: 63 ms, faster than 97.15% of TypeScript online submissions for Middle of the Linked List.
//Memory Usage: 42.5 MB, less than 95.99% of TypeScript online submissions for Middle of the Linked Li

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function middleNode(head: ListNode | null): ListNode | null {
    let totalIndex: number = 0;
    let curr: ListNode = head;
    while (curr != null) {
        totalIndex++;
        curr = curr.next;
    }
    totalIndex = Math.floor(totalIndex / 2);
    curr = head;
    while (totalIndex > 0) {
        curr = curr.next;
        totalIndex--;
    }
    return curr;
};
