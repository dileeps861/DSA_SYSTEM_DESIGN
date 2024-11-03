class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Kind of Brute force appraoch
        # for idx, char in enumerate(s):
        #     if s[idx] == goal[0]:
        #         # print(s[idx:] , goal[0: len(goal) - idx - 1] , s[0: idx] , goal[len(goal) - idx:])
        #         if (
        #             s[idx:] == goal[0 : len(goal) - idx]
        #             and s[0:idx] == goal[len(goal) - idx :]
        #         ):
        #             return True

        # return False

        # Optimal apparoach:
        # S+S then do substring search using KMP will help to find
        if len(goal) != len(s):
            return False
        return goal in (s + s)
