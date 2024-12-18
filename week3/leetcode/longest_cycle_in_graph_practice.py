class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        
        def dfs(node, visited, stack):
            if node in stack:
                return len(stack) - stack.index(node)
            if node in visited:
                return 0
            
            visited.add(node)
            stack.append(node)
            next_node = edges[node]

            max_cycle = 0
            if next_node != -1:
                max_cycle = dfs(next_node, visited, stack)
            stack.pop()
            return max_cycle


        max_cycle = 0
        visited = set()

        for i in range(len(edges)):
            if i not in visited:
                max_cycle = max(max_cycle, dfs(i, visited, []))

        if max_cycle > 0:
            return max_cycle
        else:
            return -1

# Example usage
solution = Solution()
print(solution.longestCycle([1, 2, -1, 4, 5, 6, 3, 0]))  # Example input
