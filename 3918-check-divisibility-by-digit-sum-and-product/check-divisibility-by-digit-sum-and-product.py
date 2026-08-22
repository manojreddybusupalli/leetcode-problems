class Solution:
    def checkDivisibility(self, n: int) -> bool:
        product = 1
        sum = 0
        temp = n

        while temp > 0:
            digit = temp % 10
            sum += digit
            product *= digit
            temp //= 10

        return n % (sum + product) == 0