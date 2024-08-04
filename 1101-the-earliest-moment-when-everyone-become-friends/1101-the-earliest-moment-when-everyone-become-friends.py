class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs, key=lambda x: x[0])

        class UF:
            def __init__(self, n):
                self.id = [i for i in range(n)]
                self.degree = [1] * n
                self.n = n
                self.disjointsetCount = n

            def connect(self, u, v):
                idxU = self.find(u)
                idxV = self.find(v)
                if idxU == idxV:
                    return False

                self.disjointsetCount -= 1
                if self.degree[idxU] > self.degree[idxV]:
                    self.id[idxV] = idxU
                elif self.degree[idxU] < self.degree[idxV]:
                    self.id[idxV] = idxU
                else:
                    self.id[idxU] = idxV
                    self.degree[idxV] += 1
                return True

            def find(self, u):
                if u != self.id[u]:
                    self.id[u] = self.find(self.id[u])
                return self.id[u]

            def findNoCon(self):
                return self.disjointsetCount

        uf = UF(n)
        dis_set_ct = n
        for ts, a, b in logs:
            uf.connect(a, b)
            if uf.findNoCon() == 1:
                return ts
        return -1
