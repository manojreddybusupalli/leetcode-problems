class Solution(object):
    def subtractProductAndSum(self, n):
        sum=0
        product=1
        while n>0:
            digit=n%10
            n=n//10
            sum+=digit
            product*=digit
        return product - sum