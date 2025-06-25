""" 
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        rtype = []
        rtype.extend(list1)
        rtype.extend(list2)
        return sorted(rtype)

test = Solution()
list01 = [1, 2, 4]
list02 = [1, 3, 4]
print(test.mergeTwoLists(list01,list02))