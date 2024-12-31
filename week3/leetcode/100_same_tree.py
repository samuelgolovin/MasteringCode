# beats 100.00% of runtime


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        p_array = []
        q_array = []

        def dfs(node, array):
            if node == None:
                array.append(None)
                return
            if node.val:
                array.append(node.val)
            else:
                array.append(-1)

            dfs(node.left, array)
            dfs(node.right, array)
        
        dfs(p, p_array)
        dfs(q, q_array)

        if len(p_array) == len(q_array) and p_array == q_array:
            return True
        else:
            return False
