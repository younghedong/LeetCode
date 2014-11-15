# Search Insert Position

算法

---

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
>[1,3,5,6], 5 → 2
>[1,3,5,6], 2 → 1
>[1,3,5,6], 7 → 4
>[1,3,5,6], 0 → 0

```python
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        base, top = 0, len(A) - 1
        while base <= top:
            mid = (top + base) / 2
            if target < A[mid]:
                top = mid - 1
            elif target > A[mid]:
                base = mid + 1
            else:
                return mid
        return base
```
#解题思路
### 1.折半查找
### 2.mid网上也有等于
(base + (top - base) / 2)
或
(base + (top - base) >> 2)的.
### 3.返回base的情况

[cmd Markdown](https://www.zybuluo.com/hetong/note/46393)
