// Runtime: 104 ms, faster than 19.46% of TypeScript online submissions for Merge Two Sorted Lists.
//     Memory Usage: 40.7 MB, less than 84.24% of TypeScript online submissions for Merge Two Sorted Lists.
function mergeTwoLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    let temporaryNode: ListNode = new ListNode(0);
    let currNode: ListNode = temporaryNode

    while (l1 && l2) {

        if (l1.val < l2.val) {
            currNode.next = l1;
            l1 = l1.next;
        } else {
            currNode.next = l2;
            l2 = l2.next
        }

        currNode = currNode.next;
    }

    if (l1 != null) {
        currNode.next = l1;
        l1 = l1.next;

    }
    if (l2 != null) {
        currNode.next = l2;
        l2 = l2.next;
    }

    return temporaryNode.next;
};