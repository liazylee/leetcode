"""
<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return <em>the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than </em><code>k</code>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,5,2,6], k = 100
<strong>Output:</strong> 8
<strong>Explanation:</strong> The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3], k = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li> 
 <li><code>1 &lt;= nums[i] &lt;= 1000</code></li> 
 <li><code>0 &lt;= k &lt;= 10<sup>6</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Sliding Window</li></div></div><br><div><li>👍 6556</li><li>👎 204</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        ans, l, n = 0, 0, len(nums)
        pro, res = 1, 0
        for r in range(n):
            pro *= nums[r]
            while pro >= k:
                pro /= nums[l]
                l += 1
            res += r - l + 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
