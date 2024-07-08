class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return str(numerator)
        negative = (
            False
            if (numerator < 0 and denominator < 0)
            or (numerator > 0 and denominator > 0)
            else True
        )

        numerator = abs(numerator)
        denominator = abs(denominator)
        res = [str(numerator // denominator)]
        numerator = numerator % denominator

        if numerator > 0:
            res.append(".")
        visitedNumber = {}

        while numerator > 0:
            if numerator < denominator:
                numerator *= 10
                while numerator < denominator:
                    numerator *= 10
                    res.append("0")
            else:
                if numerator in visitedNumber:
                    i = visitedNumber[numerator]
                    res.insert(i, "(")
                    res.append(")")
                    break
                else:
                    visitedNumber[numerator] = len(res)
                    res.append(str(numerator // denominator))
                    numerator = numerator % denominator
        joined = "".join(res)

        return "-" + joined if negative else joined
