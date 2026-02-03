class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     num = nums[i]
        #     while nums[i] != i + 1:
        #         target = nums[i] - 1          # where nums[i] belongs
        #         if nums[target] == nums[i]:   # duplicate found
        #             return nums[i]
        #         nums[i], nums[target] = nums[target], nums[i]  # swap into place

        # # print(nums)
        # return nums[- 1]

        # for i in range(len(nums)):
        #     j = abs(nums[i]) - 1      # use abs in case nums[i] was already negated
        #     if nums[j] < 0:
        #         return j + 1           # j+1 is the duplicate value
        #     nums[j] = -1 * nums[j]

        # for i in range(len(nums)):
        #     nums[i] = abs(nums[i])

        # return -1

        # i = 0
        # j = 1
        # n = len(nums)
        # while nums[i] != nums[j] or i == j:
        #     if i == j:
        #         i += 1
        #         j += 1
        #     i += 1
        #     j += 2
        #     # print (i, j)
        #     j = (j % n)
        #     i = (i % n)
        
        # return nums[j]
        # i = nums[0]
        # j = nums[nums[0]]
        # n = len(nums)
        # while i != j:
        #     i = nums[i]
        #     j = nums[nums[j]]
        #     i = i % n
        # return i

        # slow = fast = nums[0]

        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # 1(0) -> 3(1) -> 2 (3) -> 4(2) -> 2(4) -> 4(2) -> 2(4) -> 4(2)
            if slow == fast: # it means we are now in the cycle, but not neccessarily it is the duplicate as 
                # they may meet either at 2 or 4 here
                break

        slow = nums[0] # start from o i.e 1
        while slow != fast: # i.e fast can be 2 or 4 so lets find where we start to cross over, as mostly the cycle will of 2 numbers at the end so fast point should meet at the entry point
            slow = nums[slow]
            fast = nums[fast]
        
        return slow





