"""
<p>Given an array of strings <code>strs</code>, group <strong>the anagrams</strong> together. You can return the answer in <strong>any order</strong>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<pre><strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre>
<p><strong class="example">Example 2:</strong></p> 
<pre><strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]
</pre>
<p><strong class="example">Example 3:</strong></p> 
<pre><strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]
</pre> 
<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li> 
 <li><code>0 &lt;= strs[i].length &lt;= 100</code></li> 
 <li><code>strs[i]</code> consists of lowercase English letters.</li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Hash Table</li><li>String</li><li>Sorting</li></div></div><br><div><li>👍 18072</li><li>👎 547</li></div>
"""
from collections import defaultdict
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map=defaultdict(list)
        for s in strs:
            st=''.join(sorted(s))
            hash_map[st].append(s)
        return list(hash_map.values())
        
# leetcode submit region end(Prohibit modification and deletion)
