"""
<p>You are climbing a staircase. It takes <code>n</code> steps to reach the top.</p>

<p>Each time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 45</code></li>
</ul>
<div><div>Related Topics</div><div><li>Math</li><li>Dynamic Programming</li><li>Memoization</li></div></div><br><div><li>👍 10738</li><li>👎 330</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <=2:
        #     return n
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        # dp = [0] * n
        # dp[1], dp[2] = 1, 2
        # for i in range(2, n):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[-1]
        if n <= 3:
            return n
        f1, f2 = 1, 2
        for _ in range(2, n):
            f1, f2 = f2, f1 + f2
        return f2

# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().climbStairs(5))
