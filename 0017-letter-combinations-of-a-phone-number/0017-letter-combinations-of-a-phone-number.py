class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # build the number to char map
        # get first number and do dfs through each char in the map of respective number
        # add to res set when i reache the len of the digits
        # iterste through each char of the number in the digits list
        #   call recursive dfs by i+1 and adding char

        n = len(digits)
        if not n:
            return []
        mapD = {
            2: ("a", "b", "c"),
            3: ("d", "e", "f"),
            4: ("g", "h", "i"),
            5: ("j", "k", "l"),
            6: ("m", "n", "o"),
            7: ("p", "q", "r", "s"),
            8: ("t", "u", "v"),
            9: ("w", "x", "y", "z"),
        }
        res = []

        def dfs(i, lst):
            if i >= n:
                res.append("".join(lst))
                return
            
            digit = int(digits[i])
            
            for char in mapD[digit]:
                if len(lst) < i + 1:
                    lst.append("")
                lst[i] = char
                dfs(i + 1, lst)

        dfs(0, [])

        return res
