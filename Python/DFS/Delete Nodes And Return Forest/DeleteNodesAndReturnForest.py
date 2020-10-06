# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def delNodes(self, root, to_delete):
        res = []

        def dfs(node, is_root):
            if not node: return None
            is_delete = node.val in to_delete
            if is_root and not is_delete:
                res.append(node)
            node.left = dfs(node.left, is_delete)
            node.right = dfs(node.right, is_delete)
            return None if is_delete else node

        dfs(root, True)
        return res


root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
to_delete = [3]
main = Solution()
for node in main.delNodes(root, to_delete):
    print(node.val)
