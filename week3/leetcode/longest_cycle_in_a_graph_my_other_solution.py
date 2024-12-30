class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """

        cycles = []

        def dfs(node, start, path):
            for cycle in cycles:
                if node in cycle:
                    return
            if node == -1:
                return
            if node in path:
                if node == start:
                    cycles.append(path[path.index(node):])
                return

            path.append(node)
            neighbor = edges[node]
            dfs(neighbor, start, path)
            path.pop()

        for start_node in edges:
            dfs(start_node, start_node, [])

        print(cycles)

        if len(cycles) == 0:
            return -1
        else:
            max_cycle = 0
            for cycle in cycles:
                max_cycle = max(max_cycle, len(cycle))
            return max_cycle
