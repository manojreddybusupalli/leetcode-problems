class Solution(object):
    def findMissingElements(self, nums):
         mis = []

         for i in range(min(nums) +1,max(nums)):
             if i not in nums:
                mis.append(i)


         return mis
  
        