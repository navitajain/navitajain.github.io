'''Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #iteratively
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = root = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                root.next = l1
                l1 = l1.next
            else:
                root.next = l2
                l2 = l2.next
            root = root.next
        
        root.next = l1 or l2
        
        return head.next
        #return head.next.val
    
    # recursive
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
            
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
            #return l1.val
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
            #return l2.

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)


l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)


a = Solution()
print(a.mergeTwoLists(l1,l2))
