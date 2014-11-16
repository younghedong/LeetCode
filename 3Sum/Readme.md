# 3Sum

算法

---

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

###Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

 >   A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

```python
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
```

#解题思路
### 1.排序
### 2.迭代前len(num)-2个元素
> a.固定该元素
  b.对该元素后面的所有元素，用类似二分法的思想（不同于二分法）：
  当num[i] + num[base] + num[top] < 0 时，后移base;
  当num[i] + num[base] + num[top] > 0 时，前移top;
  当num[i] + num[base] + num[top] == 0时，保存当前结果，并判断base, top的下一位置是否与当前值相同，若相同，则越过，这样保证结果不重复
  c.对特殊情况len(num) <= 3 特殊处理
  
[cmd Markdown](https://www.zybuluo.com/hetong/note/46501)
