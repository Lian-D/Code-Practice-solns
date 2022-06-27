//Runtime: 88 ms, faster than 78.38% of TypeScript online submissions for Merge Two Sorted Lists.
//Memory Usage: 45 MB, less than 43.98% of TypeScript online submissions for Merge Two Sorted Lists.

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    let returnNode: ListNode = new ListNode(0);
    let currNode = returnNode;

    while (list1 && list2) {
        if (list1.val < list2.val) {
            currNode.next = list1;
            list1 = list1.next;
        } else {
            currNode.next = list2;
            list2 = list2.next;
        }
        currNode = currNode.next;
        
    }
    if (list1 != null) {
        currNode.next = list1;
    }
    if (list2 != null) {
        currNode.next = list2;
    }
    return returnNode.next;
};
