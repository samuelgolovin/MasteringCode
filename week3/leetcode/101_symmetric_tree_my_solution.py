# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def dfs_left(node, array):
            if node == None:
                array.append(None)
                return
            array.append(node.val)

            dfs_left(node.left, array)
            dfs_left(node.right, array)

        def dfs_right(node, array):
            if node == None:
                array.append(None)
                return
            array.append(node.val)

            dfs_right(node.right, array)
            dfs_right(node.left, array)
            

            return array

        left_array = []
        right_array = []

        dfs_left(root.left, left_array)
        dfs_right(root.right, right_array)
        

        return (left_array == right_array)
