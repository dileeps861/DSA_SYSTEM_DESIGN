class Solution:
    def numTrees(self, n: int) -> int:
        # create a list of 1 to n numbers
        # then do dfs and pass i, j
        # for each dfs loop run throuhg i to j and devide list in further half to create bst
        # whenever we reach currentnodes count, increase res by one
        # need to back track as well for curr node
        # we need to cache if any sub list number of bst are alredy made (Use memoization)

        # cache = {}

        # def dfs(start, end):
        #     # Base case: if the range is invalid, there is one way to form an empty tree
        #     if start > end:
        #         return 1

        #     # Variable to store the count of BSTs for the current range
        #     total_trees = 0

        #     if (start, end) in cache:
        #         return cache[(start, end)]

        #     # Iterate through each number in the range as the root of the BST
        #     for root in range(start, end + 1):
        #         # Count the number of unique BSTs in the left and right subtrees
        #         left_trees = dfs(start, root - 1)  # Numbers less than the root
        #         cache[(start, root - 1)] = left_trees

        #         right_trees = dfs(root + 1, end)  # Numbers greater than the root
        #         cache[(root + 1, end)] = right_trees

        #         # Multiply the possibilities for left and right subtrees
        #         total_trees += left_trees * right_trees
        #         cache[(start, end)] = total_trees

        #     return total_trees

        # # Call the DFS function for the entire range 1 to n
        # return dfs(1, n)

        # DP (Bottom up solution)

        # DP array to store the number of unique BSTs
        dp = [0] * (n + 1)

        # Base cases
        dp[0] = 1  # Empty tree
        dp[1] = 1  # Single-node tree

        # Fill DP array
        for i in range(2, n + 1):
            for root in range(1, i + 1):  # Consider each node as root
                left = dp[root - 1]  # Nodes on the left of the root
                right = dp[i - root]  # Nodes on the right of the root
                dp[i] += left * right  # Cartesian product of left and right

        return dp[n]
