// https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
//
// Reverse Linked List
//
// Reverse a singly linked list.
//
// Example:
//
// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL
// Follow up:
//
// A linked list can be reversed either iteratively or recursively. Could you implement both?

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let currentNode = head;
    let tail = null;
    let previousNode = null;

    while (currentNode !== null) {
        previousNode = new ListNode(currentNode.val);
        previousNode.next = tail;
        tail = previousNode;
        currentNode = currentNode.next;
    }

    return previousNode;
};
