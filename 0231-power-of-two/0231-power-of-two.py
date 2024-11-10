class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # print(4 >> 2)
        # return n >> 2 == 0
        if n == 1:
            return True
        if n == 0:
            return False
        if n < 0:
            return False

        while n > 1:
            # print(n)
            if n % 2 != 0:
                return False
            n //= 2
        return True
