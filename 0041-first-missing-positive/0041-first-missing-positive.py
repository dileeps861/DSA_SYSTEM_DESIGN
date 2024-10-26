class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            # Check if the current number is in the range and not in the correct position
            if (
                1 <= nums[i] <= len(nums)
                and nums[i] != (i + 1)
                and nums[nums[i] - 1] != nums[i]
            ):
                # Swap nums[i] with the correct index position nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                # Move to the next index only if no swap was made
                i += 1

        # Second loop to find the first missing positive
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        # If all positions are correct, the missing number is len(nums) + 1
        return len(nums) + 1
