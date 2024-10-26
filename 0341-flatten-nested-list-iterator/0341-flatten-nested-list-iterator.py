# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # to solve this use dfs
        # but how to maintain the state? That's is a challenge
        # what if I can flatten the list beforehand using dfs and then hasNext and next be iterating on
        # flattened list?
        self.flattetenedList = []

        def dfsMaking(lst: [NestedInteger]):
            if lst is None:
                return

            for item in lst:
                print(item)
                if item.isInteger():
                    # add to flattetenedList
                    self.flattetenedList.append(item.getInteger())
                else:
                    # do dfs
                    dfsMaking(item.getList())

        dfsMaking(nestedList)
        self.index = 0

    def next(self) -> int:
        num = self.flattetenedList[self.index]
        self.index += 1
        return num

    def hasNext(self) -> bool:
        return self.index < len(self.flattetenedList)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
