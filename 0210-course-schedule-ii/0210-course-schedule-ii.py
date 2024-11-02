import unittest


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build order of the courses to take,
        # for each course build its pre req course relation
        # initiate the traversal with the items having 0 in degrees, zero dependencies
        # keep doing so and reduce in degree when a cours is taken

        # courses a-> b, b->c, c->d b -> d a-> c
        # queue based impl will be?
        # intiailly build adj map with nodes dependent on the nodes
        # then build in-degree map
        # then add all the nodes with 0 in degree add it to queue
        # take all those initial courses and reduce each one's in degree and as sson asin degrees
        # beomes 0 add that course to queue, maintain a list to add courses in result
        # if len(res) != numCourses return 0 else num course
        res = []

        adj = {}
        indegs = {}
        for dC, pC in prerequisites:
            if pC not in adj:
                adj[pC] = set()
            if dC not in indegs:
                indegs[dC] = 0
            indegs[dC] += 1
            adj[pC].add(dC)
        # print(adj)
        # print(indegs)
        q = Deque()
        for c in range(numCourses):
            if c not in indegs or indegs[c] == 0:
                q.append(c)
        # print(q)
        while q:
            sz = len(q)
            while sz > 0:
                c = q.popleft()
                res.append(c)
                if c not in adj:
                    sz -= 1
                    continue
                for cD in adj[c]:
                    if cD in indegs:
                        indegs[cD] -= 1
                        if indegs[cD] == 0:
                            q.append(cD)
                sz -= 1
        if len(res) != numCourses:
            return []
        return res


class UnitTestSol(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testWithStraightRelationship(self):
        res = self.sol.findOrder(3, [[2, 1], [1, 0]])
        self.assertEquals([], res)

    def testWithCircularRelationship(self):
        res = self.sol.findOrder(3, [[2, 1], [1, 0], [0, 2]])
        self.assertEquals([], res)

    def testWithComplexButPossible(self):
        res = self.sol.findOrder(4, [[2, 1], [1, 0], [2, 0], [3, 2]])
        self.assertEquals([], res)

    def testWithSingleCourse(self):
        res = self.sol.findOrder(1, [])
        self.assertEquals([0], res)
