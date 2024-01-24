"""
<p>You have a set of integers <code>s</code>, which originally contains all the numbers from <code>1</code> to <code>n</code>. Unfortunately, due to some error, one of the numbers in <code>s</code> got duplicated to another number in the set, which results in <strong>repetition of one</strong> number and <strong>loss of another</strong> number.</p>

<p>You are given an integer array <code>nums</code> representing the data status of this set after the error.</p>

<p>Find the number that occurs twice and the number that is missing and return <em>them in the form of an array</em>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<pre><strong>Input:</strong> nums = [1,2,2,4]
<strong>Output:</strong> [2,3]
</pre>
<p><strong class="example">Example 2:</strong></p> 
<pre><strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> [1,2]
</pre> 
<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li> 
 <li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Hash Table</li><li>Bit Manipulation</li><li>Sorting</li></div></div><br><div><li>👍 4524</li><li>👎 1099</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1
        res = [0, 0]
        for i in range(1, len(nums) + 1):
            if i not in hash_map:
                res[1] = i
            elif hash_map[i] == 2:
                res[0] = i
        return res



# leetcode submit region end(Prohibit modification and deletion)
