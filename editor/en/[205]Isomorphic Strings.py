"""
<p>Given two strings <code>s</code> and <code>t</code>, <em>determine if they are isomorphic</em>.</p>

<p>Two strings <code>s</code> and <code>t</code> are isomorphic if the characters in <code>s</code> can be replaced to get <code>t</code>.</p>

<p>All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<pre><strong>Input:</strong> s = "egg", t = "add"
<strong>Output:</strong> true
</pre>
<p><strong class="example">Example 2:</strong></p> 
<pre><strong>Input:</strong> s = "foo", t = "bar"
<strong>Output:</strong> false
</pre>
<p><strong class="example">Example 3:</strong></p> 
<pre><strong>Input:</strong> s = "paper", t = "title"
<strong>Output:</strong> true
</pre> 
<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li> 
 <li><code>t.length == s.length</code></li> 
 <li><code>s</code> and <code>t</code> consist of any valid ascii character.</li> 
</ul>

<div><div>Related Topics</div><div><li>Hash Table</li><li>String</li></div></div><br><div><li>👍 8057</li><li>👎 1877</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map ={}
        for i,c in zip(s,t):
            if i in hash_map and hash_map[i]!=c:
                return False
            if i not in hash_map and c in hash_map.values():
                return False
            hash_map[i]=c
        return True

        
# leetcode submit region end(Prohibit modification and deletion)
