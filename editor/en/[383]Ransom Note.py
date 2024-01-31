"""
<p>Given two strings <code>ransomNote</code> and <code>magazine</code>, return <code>true</code><em> if </em><code>ransomNote</code><em> can be constructed by using the letters from </em><code>magazine</code><em> and </em><code>false</code><em> otherwise</em>.</p>

<p>Each letter in <code>magazine</code> can only be used once in <code>ransomNote</code>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<pre><strong>Input:</strong> ransomNote = "a", magazine = "b"
<strong>Output:</strong> false
</pre>
<p><strong class="example">Example 2:</strong></p> 
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "ab"
<strong>Output:</strong> false
</pre>
<p><strong class="example">Example 3:</strong></p> 
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "aab"
<strong>Output:</strong> true
</pre> 
<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= ransomNote.length, magazine.length &lt;= 10<sup>5</sup></code></li> 
 <li><code>ransomNote</code> and <code>magazine</code> consist of lowercase English letters.</li> 
</ul>

<div><div>Related Topics</div><div><li>Hash Table</li><li>String</li><li>Counting</li></div></div><br><div><li>👍 4772</li><li>👎 485</li></div>
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map = {}
        for c in magazine:
            hash_map[c] = hash_map.get(c, 0) + 1

        for c in ransomNote:
            if c not in hash_map or hash_map[c] == 0:
                return False
            hash_map[c] -= 1

        return True


tuple
# leetcode submit region end(Prohibit modification and deletion)
