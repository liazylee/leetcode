"""
<p>Given an array of non-negative integers <code>nums</code>, you are initially positioned at the first index of the array.</p>

<p>Each element in the array represents your maximum jump length at that position.</p>

<p>Your goal is to reach the last index in the minimum number of jumps.</p>

<p>You can assume that you can always reach the last index.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,1,1,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,0,1,4]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>
<div><div>Related Topics</div><div><li>Array</li><li>Dynamic Programming</li><li>Greedy</li></div></div><br><div><li>👍 7536</li><li>👎 281</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> float:
        max_reach, step, end = 0, 0, 0
        for i in range(len(nums)-1):
            if max_reach >= i:
                max_reach = max(max_reach, i + nums[i])
                if i == end:
                    end = max_reach
                    step += 1
        return step

# leetcode submit region end(Prohibit modification and deletion)
