class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        array = []

        if n <= 1:
            array.append(n)
            return n

        array.append(0)
        array.append(1)

        for i in range(2, n + 1):
            fib_num = array[i - 1] + array[i - 2]
            array.append(fib_num)
        print(array)
        return array[-1]

solution = Solution()
print(solution.fib(5))
print(solution.fib(6))
print(solution.fib(7))
