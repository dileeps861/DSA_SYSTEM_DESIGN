class Solution:
    def myPow(self, x: float, n: int) -> float:
        # something like double every time? until reached half?
        # similar to the way binary search but reverse
        # n = 10
        # n % 2
        # if n <= 2 return x * n 
        # times = 1
        # val = x
        # val = val * val 
        # times = times * 2
        # if times * times <= n:
        # then return val * val 
        # do it recursively 
        # if any left over then do the same for left over start with newval = num and newtimes = 1
        # and newN = n - times
        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            times = 1
            val = x

            # Keep squaring until times * 2 <= n
            while times * 2 <= n:
                val = val * val
                times = times * 2
            
            # Recurse on the remaining part
            remaining = helper(x, n - times)
            return val * remaining

        if n < 0:
            x = 1 / x
            n = -n

        return helper(x, n)
