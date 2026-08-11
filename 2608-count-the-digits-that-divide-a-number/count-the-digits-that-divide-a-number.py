class Solution(object):
    def countDigits(self, num):
        count = 0
        n = num

        while n > 0:
            digit = n % 10
            n = n // 10

            if digit != 0 and num % digit == 0:
                count += 1

        return count