# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    solution = Solution()

    assert '100' == solution.addBinary('11', '1')
    assert '10101' == solution.addBinary('1010', '1011')
