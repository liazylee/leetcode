"""
<p>Given <code>n</code> pairs of parentheses, write a function to <em>generate all combinations of well-formed parentheses</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> ["()"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>
<div><div>Related Topics</div><div><li>String</li><li>Dynamic Programming</li><li>Backtracking</li></div></div><br><div><li>👍 12034</li><li>👎 470</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.list = []

        def _gen(left, right, n, s):
            if left == n and right == n:
                self.list.append(s)
                return
            if left < n:
                _gen(left + 1, right, n, s + '(')
            if right < left:
                _gen(left, right + 1, n, s + ')')

        _gen(0, 0, n, '')
        return self.list

# leetcode submit region end(Prohibit modification and deletion)
