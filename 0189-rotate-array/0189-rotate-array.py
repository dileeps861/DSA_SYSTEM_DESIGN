class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # swap k items from end to start athen reverse ke items from right
        n = len(nums)
        k = k % n

        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        i = n - k
        j = n - 1
        reverse(i, j)
        i = 0
        j = n - k - 1
        reverse(i, j)
        j = n - 1
        reverse(i, j)
