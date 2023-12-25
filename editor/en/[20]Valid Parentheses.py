"""
<p>Given a string <code>s</code> containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
</ol>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;()[]{}&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(]&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of parentheses only <code>&#39;()[]{}&#39;</code>.</li>
</ul>
<div><div>Related Topics</div><div><li>String</li><li>Stack</li></div></div><br><div><li>👍 11618</li><li>👎 513</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:

        stack=["?"]
        brackets_dict={")":"(","}":"{","]":"["}
        for i in s:
            if i not in brackets_dict:
                stack.append(i)
            elif brackets_dict[i] !=stack.pop():
                return False
        return len(stack)==1

        # for i in s:
        #     if i not in brackets_dict:
        #         stack.append(i)
        #     elif brackets_dict[i] !=stack.pop(0):
        #         return False
        # return len(stack)==1





# leetcode submit region end(Prohibit modification and deletion)
