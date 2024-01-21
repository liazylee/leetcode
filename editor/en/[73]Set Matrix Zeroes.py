"""
<p>Given an <code>m x n</code> integer matrix <code>matrix</code>, if an element is <code>0</code>, set its entire row and column to <code>0</code>'s.</p>

<p>You must do it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in place</a>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg" style="width: 450px; height: 169px;" /> 
<pre>
<strong>Input:</strong> matrix = [[1,1,1],[1,0,1],[1,1,1]]
<strong>Output:</strong> [[1,0,1],[0,0,0],[1,0,1]]
</pre>

<p><strong class="example">Example 2:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg" style="width: 450px; height: 137px;" /> 
<pre>
<strong>Input:</strong> matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
<strong>Output:</strong> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>m == matrix.length</code></li> 
 <li><code>n == matrix[0].length</code></li> 
 <li><code>1 &lt;= m, n &lt;= 200</code></li> 
 <li><code>-2<sup>31</sup> &lt;= matrix[i][j] &lt;= 2<sup>31</sup> - 1</code></li> 
</ul>

<p>&nbsp;</p> 
<p><strong>Follow up:</strong></p>

<ul> 
 <li>A straightforward solution using <code>O(mn)</code> space is probably a bad idea.</li> 
 <li>A simple improvement uses <code>O(m + n)</code> space, but still not the best solution.</li> 
 <li>Could you devise a constant space solution?</li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Hash Table</li><li>Matrix</li></div></div><br><div><li>👍 13807</li><li>👎 695</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m=len(matrix),len(matrix[0])
        row,col=set(),set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        for i in row:
            for j in range(m):
                matrix[i][j]=0
        for j in col:
            for i in range(n):
                matrix[i][j]=0


        
# leetcode submit region end(Prohibit modification and deletion)
