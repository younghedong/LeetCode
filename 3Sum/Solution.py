#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        length = len(num)
        num = sorted(num)
        if(length <= 3):
            if length == 3 and sum(num) == 0:
                return [num]
            else:
                return []
                
        result = []
        for i in range(0, length-2):
            if i > 0 and num[i] == num[i-1]:
                continue
            base, top = i + 1, length - 1
            twoSum = 0 - num[i]
            while base < top:
                if num[base] + num[top] < twoSum:
                    base = base + 1
                elif num[base] + num[top] == twoSum:
                    result.append([num[i], num[base], num[top]])
                    base, top = base + 1, top -1
                    while base < top and num[base] == num[base -1]:
                        base = base + 1
                    while base < top and num[top] == num[top + 1]:
                        top = top -1
                else:
                    top = top -1
        return result
