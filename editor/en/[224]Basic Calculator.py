"""
<p>Given a string <code>s</code> representing a valid expression, implement a basic calculator to evaluate it, and return <em>the result of the evaluation</em>.</p>

<p><strong>Note:</strong> You are <strong>not</strong> allowed to use any built-in function which evaluates strings as mathematical expressions, such as <code>eval()</code>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "1 + 1"
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = " 2-1 + 2 "
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = "(1+(4+5+2)-3)+(6+8)"
<strong>Output:</strong> 23
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li> 
 <li><code>s</code> consists of digits, <code>'+'</code>, <code>'-'</code>, <code>'('</code>, <code>')'</code>, and <code>' '</code>.</li> 
 <li><code>s</code> represents a valid expression.</li> 
 <li><code>'+'</code> is <strong>not</strong> used as a unary operation (i.e., <code>"+1"</code> and <code>"+(2 + 3)"</code> is invalid).</li> 
 <li><code>'-'</code> could be used as a unary operation (i.e., <code>"-1"</code> and <code>"-(2 + 3)"</code> is valid).</li> 
 <li>There will be no two consecutive operators in the input.</li> 
 <li>Every number and running calculation will fit in a signed 32-bit integer.</li> 
</ul>

<div><div>Related Topics</div><div><li>Math</li><li>String</li><li>Stack</li><li>Recursion</li></div></div><br><div><li>👍 6066</li><li>👎 452</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num, sign = 0, 1
        result = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                num, sign = 0, 1
            elif char == '-':
                result += sign * num
                num, sign = 0, -1
            elif char == '(':
                stack.append((result, sign))
                result, sign = 0, 1
            elif char == ')':
                result += sign * num
                num = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result

        return result + sign * num

# leetcode submit region end(Prohibit modification and deletion)
