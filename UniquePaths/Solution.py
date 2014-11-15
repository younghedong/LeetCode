#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
            return self.combiantion(m+n-2, m-1)

    #排列组合
    def combiantion(self, m, n):
        mcount = 1
        ncount = 1
        for i in range(m, m-n, -1):
            mcount = mcount * i
        for i in range(n, 1, -1):
            ncount = ncount * i
        return mcount/ncount
