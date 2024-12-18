class Solution(object):
    def __init__(self):
        self.graph = {}

    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        # for each node, recursively? visit neighbors until end or until you visit starting node again:
        #     keep track of neighbors checked
        #     if no more neighbors:
        #         continue or break
        #     elif neighbor is equal to starting node:
        #         set current highest cycle to number of neighbors checked


        for i in range(len(edges)):
            self.graph[i] = edges[i]

        # print(graph)

        max_cycle = 0

        for i in self.graph:
            running = True
            visited = [i]
            next_node = i
            while running:
                if next_node in self.graph:
                    next_node = self.graph[next_node]
                    if next_node in visited and next_node == i:
                        max_cycle = max(max_cycle, len(visited))
                        back_to_start = True
                    elif next_node not in visited:
                        visited.append(next_node)
                    else:
                        running = False
                else:
                    break
        if max_cycle == 0:
            return -1
        else:
            return max_cycle

# Example Usage
edges = [1, 2, -1, 4, 5, 6, 3, 0]
solution = Solution()
print(solution.longestCycle(edges))
