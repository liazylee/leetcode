"""
<p>Given an array of integers <code>temperatures</code> represents the daily temperatures, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is the number of days you have to wait after the</em> <code>i<sup>th</sup></code> <em>day to get a warmer temperature</em>. If there is no future day for which this is possible, keep <code>answer[i] == 0</code> instead.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<pre><strong>Input:</strong> temperatures = [73,74,75,71,69,72,76,73]
<strong>Output:</strong> [1,1,4,2,1,1,0,0]
</pre>
<p><strong class="example">Example 2:</strong></p> 
<pre><strong>Input:</strong> temperatures = [30,40,50,60]
<strong>Output:</strong> [1,1,1,0]
</pre>
<p><strong class="example">Example 3:</strong></p> 
<pre><strong>Input:</strong> temperatures = [30,60,90]
<strong>Output:</strong> [1,1,0]
</pre> 
<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;=&nbsp;temperatures.length &lt;= 10<sup>5</sup></code></li> 
 <li><code>30 &lt;=&nbsp;temperatures[i] &lt;= 100</code></li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Stack</li><li>Monotonic Stack</li></div></div><br><div><li>👍 12528</li><li>👎 289</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            while stack and v > temperatures[stack[-1]]:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res




# leetcode submit region end(Prohibit modification and deletion)
