from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    ## Need to remind that each element in list is a node itself!!!
    ## Need to connect each node by node by initiate as a Node
    lists = [[1,4,5],[1,3,4],[2,6]]
    l1 = ListNode(1)
    l2 = ListNode(4)
    l3 = ListNode(5)
    l1.next = l2
    l2.next = l3
    temp = l1
    while temp.next is not None: 
        print(temp.val)
        temp = temp.next
    print(temp.val)
    l21 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)
    l21.next = l22
    l22.next = l23

    l31 = ListNode(2)
    l32 = ListNode(6)
    l31.next = l32

    lists = [l1, l21, l31]

    def mergeKLists(self, lists):
        min = 0
        for i, subList in enumerate(lists):
            
            lists[i]