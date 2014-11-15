#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        base, top = 0, len(A) - 1
        while base <= top:
            mid = base+ (top - base) / 2
            if target < A[mid]:
                top = mid - 1
            elif target > A[mid]:
                base = mid + 1
            else:
                return mid
        return base
