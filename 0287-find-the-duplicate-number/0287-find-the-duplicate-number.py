class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Modifying the original array:
        # res = -1
        # for i in range(len(nums)):
        #     idx = abs(nums[i])
        #     if nums[idx] < 0:
        #         res = abs(idx)
        #         break
        #     nums[idx] =  -nums[idx]
        # for i in range(len(nums)):
        #     nums[i] = abs(nums[i])
        # return res

        # without modifying original array:

        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow