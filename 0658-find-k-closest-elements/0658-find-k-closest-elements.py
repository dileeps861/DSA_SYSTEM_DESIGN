class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []

        leftI = bisect_left(arr, x)
        rightI = leftI
        leftI -= 1
        # print(leftI)
        while len(res) < k:
            if leftI >= 0 and rightI < len(arr):
                a = arr[leftI]
                b = arr[rightI]
                if abs(a - x) < abs(b - x):
                    res.append(a)
                    leftI -= 1
                elif a < b and abs(a - x) == abs(b - x):
                    res.append(a)
                    leftI -= 1
                else:
                    res.append(b)
                    rightI += 1
            elif leftI >= 0:
                res.append(arr[leftI])
                leftI -= 1
            elif rightI < len(arr):
                res.append(arr[rightI])
                rightI += 1
            else:
                break
        res.sort()
        return res
