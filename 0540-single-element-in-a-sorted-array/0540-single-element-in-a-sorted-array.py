class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # the number len will be odd
        # so the eaxct once apearing num whichever side is the 
        # num pair will be on odd & even  whereass all the num pair shoudld be even & odd
        #  so use binary search 
        # the mid idx will be od number so if mid +1 & mid values are same then go right 
        #  else go left until left == right that the number which is the culprit
        # but to calcualte ensure the mid and mid+1 are in range
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # Proper pair, move right
                left = mid + 2
            else:
                # Broken pair, move left
                right = mid

        return nums[left]
