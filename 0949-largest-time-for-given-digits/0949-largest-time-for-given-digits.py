class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort()
        hhmm = [-1, -1]

        for i in range(4):
            for j in range(4):
                for m in range(4):
                    for n in range(4):
                        if i == j or m == n or n == j or n == i or m == i or m == j:
                            continue
                        else:
                            hh = int(arr[i] * 10 + arr[j])
                            mm = int(arr[m] * 10 + arr[n])
                            if hh < 24 and hhmm[0] < hh and mm < 60:
                                hhmm[0] = hh
                                hhmm[1] = mm
                            elif hhmm[0] == hh and mm < 60:
                                hhmm[1] = mm
        if hhmm[0] == -1 or hhmm[1] == -1:
            return ''
        hh = str(hhmm[0]) if hhmm[0] > 9 else '0' + str(hhmm[0])
        mm = str(hhmm[1]) if hhmm[1] > 9 else '0' + str(hhmm[1])
        return hh + ':' + mm
