"""
<p>Given two integers <code>left</code> and <code>right</code> that represent the range <code>[left, right]</code>, return <em>the bitwise AND of all numbers in this range, inclusive</em>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> left = 5, right = 7
<strong>Output:</strong> 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> left = 0, right = 0
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> left = 1, right = 2147483647
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>0 &lt;= left &lt;= right &lt;= 2<sup>31</sup> - 1</code></li> 
</ul>

<div><div>Related Topics</div><div><li>Bit Manipulation</li></div></div><br><div><li>👍 3200</li><li>👎 224</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return right

# leetcode submit region end(Prohibit modification and deletion)
