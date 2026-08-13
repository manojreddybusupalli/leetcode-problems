class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_map={}
        max_pair_sum= -1
        for num in nums:
            d_sum =0
            temp=num
            while temp>0:
                d_sum += temp % 10
                temp //=10
            if d_sum in digit_sum_map:
                pair=num + digit_sum_map.get(d_sum)
                max_pair_sum = max(max_pair_sum,pair)
                digit_sum_map[d_sum] = max(digit_sum_map.get(d_sum),num)
            else:
                digit_sum_map[d_sum] = num

        return max_pair_sum
