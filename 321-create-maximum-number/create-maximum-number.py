class Solution:
    def maxNumber(self, nums1, nums2, k):

        def pick(arr, length):
            remove = len(arr) - length
            stack = []

            for digit in arr:
                while remove and stack and stack[-1] < digit:
                    stack.pop()
                    remove -= 1
                stack.append(digit)

            return stack[:length]

        def greater(a, i, b, j):
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1

            if j == len(b):
                return True
            if i == len(a):
                return False

            return a[i] > b[j]

        def merge(a, b):
            i = j = 0
            ans = []

            while i < len(a) or j < len(b):
                if greater(a, i, b, j):
                    ans.append(a[i])
                    i += 1
                else:
                    ans.append(b[j])
                    j += 1

            return ans

        answer = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for x in range(start, end + 1):
            first = pick(nums1, x)
            second = pick(nums2, k - x)
            candidate = merge(first, second)

            if candidate > answer:
                answer = candidate

        return answer