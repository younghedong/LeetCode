#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def twoSum(self, num, target):
        mp = {}
        #construct the dict
        for index, value in enumerate(num):
            mp.setdefault(value, []).append(index +1)
        #is has key
        for key in mp.keys():
            if mp.has_key(target-key):
                if target - key != key:
                    return sorted((mp[key][0], mp[target-key][0]))
                else:
                    return sorted((mp[key][0], mp[key][1]))
