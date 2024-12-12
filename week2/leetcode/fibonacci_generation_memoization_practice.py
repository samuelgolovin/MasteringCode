class Solution(object):
    def fib(self, n, memo={}):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        if n in memo:
            return memo[n]

        memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)

        print(memo)

        return memo[n]

solution = Solution()
print(solution.fib(5))
print(solution.fib(5))
print(solution.fib(7))
