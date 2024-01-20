"""
<p>You are given a <strong>sorted unique</strong> integer array <code>nums</code>.</p>

<p>A <strong>range</strong> <code>[a,b]</code> is the set of all integers from <code>a</code> to <code>b</code> (inclusive).</p>

<p>Return <em>the <strong>smallest sorted</strong> list of ranges that <strong>cover all the numbers in the array exactly</strong></em>. That is, each element of <code>nums</code> is covered by exactly one of the ranges, and there is no integer <code>x</code> such that <code>x</code> is in one of the ranges but not in <code>nums</code>.</p>

<p>Each range <code>[a,b]</code> in the list should be output as:</p>

<ul> 
 <li><code>"a-&gt;b"</code> if <code>a != b</code></li> 
 <li><code>"a"</code> if <code>a == b</code></li> 
</ul>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1,2,4,5,7]
<strong>Output:</strong> ["0-&gt;2","4-&gt;5","7"]
<strong>Explanation:</strong> The ranges are:
[0,2] --&gt; "0-&gt;2"
[4,5] --&gt; "4-&gt;5"
[7,7] --&gt; "7"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,2,3,4,6,8,9]
<strong>Output:</strong> ["0","2-&gt;4","6","8-&gt;9"]
<strong>Explanation:</strong> The ranges are:
[0,0] --&gt; "0"
[2,4] --&gt; "2-&gt;4"
[6,6] --&gt; "6"
[8,9] --&gt; "8-&gt;9"
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>0 &lt;= nums.length &lt;= 20</code></li> 
 <li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li> 
 <li>All the values of <code>nums</code> are <strong>unique</strong>.</li> 
 <li><code>nums</code> is sorted in ascending order.</li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li></div></div><br><div><li>👍 3801</li><li>👎 2070</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return ['']
        res, n, result = str(nums[0]), len(nums), []
        for i in range(1, n):
            if nums[i] - nums[i - 1] == 1:

                continue
            else:
                if res != str(nums[i - 1]):
                    res += '->' + str(nums[i - 1])
                result.append(res)
                res = str(nums[i])
        result.append(res)
        return result


print(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))
# leetcode submit region end(Prohibit modification and deletion)
