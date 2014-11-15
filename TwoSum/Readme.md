# Two Sum

------

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.
>Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

```python
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        mp={}
        #construct the dict, with multiple values
        for index, value in enumerate(num):
            mp.setdefault(value, []).append(index+1)
        
        #is has key
        for key in mp.keys():
             if mp.has_key(target - key):
                 if target - key != key:
                    return sorted((mp[key][0], mp[target-key][0]))
                 else:
                    return sorted((mp[key][0], mp[key][1]))
```
   
   解题思路：
### 1：将num的value当做dict的key,index + 1当做dict的value,这样可以用has_key去快速查找
### 2：考虑这样一种情况num = [0, 1, 3, 0], target = 0
>此时dict中key = 0, value = [1, 4]，故dic的value应为list
### 3.返回结果的排序
>拿到结果后**封装为tuble**,然后再调用sorted(),即sor




