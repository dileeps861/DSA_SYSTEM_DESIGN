class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # Brute forece approach O(n^2)
        # for i in range(n):
        #     prod = 1
        #     for j in range(i+1):
        #         prod *= nums[j]
        #         res = max(res, prod)
        # return res

        # can we do better? How?
        # Seeing the trend that to get max prod either least negative value multiplied with negative will give highest or highest + value * positive num
        minProd = nums[0]
        maxProd = nums[0]
        res = nums[0]
        for i in range(1, n):
            num = nums[i]
            minProd, maxProd = min(min(minProd * num, maxProd * num), num), max(max(minProd * num, maxProd * num), num)
            res = max(res, maxProd)
        return res
