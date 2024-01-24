"""
<p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = "A man, a plan, a canal: Panama"
<strong>Output:</strong> true
<strong>Explanation:</strong> "amanaplanacanalpanama" is a palindrome.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = "race a car"
<strong>Output:</strong> false
<strong>Explanation:</strong> "raceacar" is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = " "
<strong>Output:</strong> true
<strong>Explanation:</strong> s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li> 
 <li><code>s</code> consists only of printable ASCII characters.</li> 
</ul>

<div><div>Related Topics</div><div><li>Two Pointers</li><li>String</li></div></div><br><div><li>👍 8796</li><li>👎 8208</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l, r = 0, len(s) - 1
        while (l < r):
            while (l < r and not s[l].isalnum()):
                l += 1

            while (l < r and not s[r].isalnum()):
                r -= 1

            if (s[l] != s[r]):
                return False
            else:
                l += 1
                r -= 1

        return True
# leetcode submit region end(Prohibit modification and deletion)
