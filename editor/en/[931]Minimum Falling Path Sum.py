"""
<p>Given an <code>n x n</code> array of integers <code>matrix</code>, return <em>the <strong>minimum sum</strong> of any <strong>falling path</strong> through</em> <code>matrix</code>.</p>

<p>A <strong>falling path</strong> starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position <code>(row, col)</code> will be <code>(row + 1, col - 1)</code>, <code>(row + 1, col)</code>, or <code>(row + 1, col + 1)</code>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg" style="width: 499px; height: 500px;" /> 
<pre>
<strong>Input:</strong> matrix = [[2,1,3],[6,5,4],[7,8,9]]
<strong>Output:</strong> 13
<strong>Explanation:</strong> There are two falling paths with a minimum sum as shown.
</pre>

<p><strong class="example">Example 2:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg" style="width: 164px; height: 365px;" /> 
<pre>
<strong>Input:</strong> matrix = [[-19,57],[-40,-5]]
<strong>Output:</strong> -59
<strong>Explanation:</strong> The falling path with a minimum sum is shown.
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>n == matrix.length == matrix[i].length</code></li> 
 <li><code>1 &lt;= n &lt;= 100</code></li> 
 <li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Dynamic Programming</li><li>Matrix</li></div></div><br><div><li>👍 5802</li><li>👎 141</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(m):
            dp[0][i] = matrix[0][i]
        for i in range(1, n):
            for j in range(m):
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                elif j == m - 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
        return min(dp[-1])

# leetcode submit region end(Prohibit modification and deletion)
