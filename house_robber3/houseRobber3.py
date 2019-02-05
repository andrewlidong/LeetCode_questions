class Solution(object):
    def rob(self, root):
        return self.robDFS(root)[1];
    def robDFS(self, node):
        if node is None:
            return (0, 0)
        l = self.robDFS(node.left)
        r = self.robDFS(node.right)
        return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + node.val))
