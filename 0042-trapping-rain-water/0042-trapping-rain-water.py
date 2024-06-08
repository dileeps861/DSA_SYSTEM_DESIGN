class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        res = 0
        left = 0
        right = 0
        while i < j:
            
            left = max(left, height[i])
            right = max(right, height[j])
            
            if  height[i] < height[j]:
                if left > height[i] and right >= height[i]:
                    res += min(left, right) - height[i]
                i += 1
            else:
                if left > height[j] and right >= height[j]:
                    res += min(left, right) - height[j]
                j -= 1
        return res

