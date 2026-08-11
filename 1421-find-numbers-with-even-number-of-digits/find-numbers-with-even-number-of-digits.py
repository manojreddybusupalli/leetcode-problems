class Solution(object):
    def findNumbers(self, nums):
        count = 0

        for i in nums:
            digits = 0
            n = i

            while n > 0:
                n = n // 10
                digits += 1

            if digits % 2 == 0:
                count += 1

        return count