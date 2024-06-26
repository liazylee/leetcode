"""
<p>Given a string containing digits from <code>2-9</code> inclusive, return all possible letter combinations that the number could represent. Return the answer in <strong>any order</strong>.</p>

<p>A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.</p>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png" style="width: 200px; height: 162px;" /></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;23&quot;
<strong>Output:</strong> [&quot;ad&quot;,&quot;ae&quot;,&quot;af&quot;,&quot;bd&quot;,&quot;be&quot;,&quot;bf&quot;,&quot;cd&quot;,&quot;ce&quot;,&quot;cf&quot;]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;&quot;
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = &quot;2&quot;
<strong>Output:</strong> [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= digits.length &lt;= 4</code></li>
	<li><code>digits[i]</code> is a digit in the range <code>[&#39;2&#39;, &#39;9&#39;]</code>.</li>
</ul>
<div><div>Related Topics</div><div><li>Hash Table</li><li>String</li><li>Backtracking</li></div></div><br><div><li>👍 9356</li><li>👎 650</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs",
                '8': "tuv", '9': "wxyz"}
        if not digits:
            return []
        res = []

        def backtrack(index, path):
            if len(path) == len(digits):
                res.append(''.join(path))
                return res
            for i in dict[digits[index]]:
                path.append(i)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])

        return res

# leetcode submit region end(Prohibit modification and deletion)
