"""
<p>Given a <strong>0-indexed</strong> integer array <code>nums</code>, find a <strong>0-indexed </strong>integer array <code>answer</code> where:</p>

<ul> 
 <li><code>answer.length == nums.length</code>.</li> 
 <li><code>answer[i] = |leftSum[i] - rightSum[i]|</code>.</li> 
</ul>

<p>Where:</p>

<ul> 
 <li><code>leftSum[i]</code> is the sum of elements to the left of the index <code>i</code> in the array <code>nums</code>. If there is no such element, <code>leftSum[i] = 0</code>.</li> 
 <li><code>rightSum[i]</code> is the sum of elements to the right of the index <code>i</code> in the array <code>nums</code>. If there is no such element, <code>rightSum[i] = 0</code>.</li> 
</ul>

<p>Return <em>the array</em> <code>answer</code>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,4,8,3]
<strong>Output:</strong> [15,1,11,22]
<strong>Explanation:</strong> The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> [0]
<strong>Explanation:</strong> The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 1000</code></li> 
 <li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Prefix Sum</li></div></div><br><div><li>👍 933</li><li>👎 75</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lr,rs,ans = 0,sum(nums),[]
        for num in nums:
            rs -= num
            ans.append(abs(lr-rs))
            lr += num
        return ans


# leetcode submit region end(Prohibit modification and deletion)
