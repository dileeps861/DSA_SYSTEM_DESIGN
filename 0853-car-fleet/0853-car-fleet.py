class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedList = [(pos, sp) for pos, sp in zip(position, speed)]
        sortedList.sort()
        stack = []
 
        for i in range(len(sortedList) - 1, -1, -1):
            pos, speed = sortedList[i]
            timeNeed = (target - pos) / speed
            if not stack or stack[-1] < timeNeed:
                stack.append(timeNeed)
        return len(stack) 