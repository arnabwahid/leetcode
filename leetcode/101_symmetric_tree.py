# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return (
            other is not None and
            self.val == other.val and
            self.left == other.left and
            self.right == other.right
        )


class Solution(object):
    def isSymmetric(self, root):
        def _isSymmetric(left, right):
            if left is None or right is None:
                return left is None and right is None
            return (
                left.val == right.val and
                _isSymmetric(left.left, right.right) and
                _isSymmetric(left.right, right.left)
            )

        if root is None:
            return True
        return _isSymmetric(root.left, root.right)


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(2)
    t0_3 = TreeNode(3)
    t0_4 = TreeNode(4)
    t0_5 = TreeNode(4)
    t0_6 = TreeNode(3)
    t0_2.left = t0_5
    t0_2.right = t0_6
    t0_1.left = t0_3
    t0_1.right = t0_4
    t0_0.left = t0_1
    t0_0.right = t0_2

    assert solution.isSymmetric(t0_0)
