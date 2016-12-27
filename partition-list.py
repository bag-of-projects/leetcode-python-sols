# https://leetcode.com/problems/partition-list/

# Given a linked list and a value x, partition it such that all nodes less than x 
# come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        dummy1, dummy2 = ListNode(None), ListNode(None)
        ptr1, ptr2 = dummy1, dummy2
        node = head
        while node:
            if node.val < x:
                ptr1.next, ptr1 = node, node
            else: # node.val >= x
                ptr2.next, ptr2 = node, node
            node.next, node = None, node.next
        ptr1.next = dummy2.next
        return dummy1.next
            
                