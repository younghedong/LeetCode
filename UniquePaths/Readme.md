# Unique Paths
---
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

> How many possible unique paths are there?

```python
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
```
#解题思路
### 1.Robot需要向右走n-1步，向下走m-1步，故只需在总的步数m+n-2中挑选出向右或向下走的方法总数，即
$$C_{m+n-2}^{m-1}$$
或
$$C_{m+n-2}^{n-1}$$




