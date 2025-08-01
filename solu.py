class Solution(object):
    def addTwoNumbers(self,l1,l2):
        l1 = list_to_linked_list([2,4,3])
        l2 = list_to_linked_list([5,6,4])
sol = Solution()
result = sol.addTwoNumbers(l1,l2)
print(linked_list_to_list([result]))