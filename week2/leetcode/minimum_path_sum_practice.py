# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for j in range(1, m):
            dp[j][0] = grid[j][0] + dp[j-1][0]

        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i - 1]

        for j in range(1, m):
            for i in range(1, n):
                dp[j][i] = grid[j][i] + min(dp[j-1][i], dp[j][i-1])

        return dp[m-1][n-1]

# Example usage
solution = Solution()
print(solution.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7
print(solution.minPathSum([[1,2,3],[4,5,6]]))          # Output: 12


# 1 3 1
# 1 5 1
# 4 2 1
# smallest sum path being 1 -> 3 -> 1 -> 1 -> 1 the sume being 7
