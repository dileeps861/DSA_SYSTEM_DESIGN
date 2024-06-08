class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)

        res = 0
        for num in nums:
            n = num
            temp = 0
            while n in st:
                temp += 1
                st.remove(n)
                n -= 1
            n = num + 1
            while n in st:
                temp += 1
                st.remove(n)
                n += 1
            res = max(res, temp)
        return res