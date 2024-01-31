"""
<p>Given an <code>m x n</code> <code>board</code>&nbsp;of characters and a list of strings <code>words</code>, return <em>all words on the board</em>.</p>

<p>Each word must be constructed from letters of sequentially adjacent cells, where <strong>adjacent cells</strong> are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/07/search1.jpg" style="width: 322px; height: 322px;" /> 
<pre>
<strong>Input:</strong> board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
<strong>Output:</strong> ["eat","oath"]
</pre>

<p><strong class="example">Example 2:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/07/search2.jpg" style="width: 162px; height: 162px;" /> 
<pre>
<strong>Input:</strong> board = [["a","b"],["c","d"]], words = ["abcb"]
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>m == board.length</code></li> 
 <li><code>n == board[i].length</code></li> 
 <li><code>1 &lt;= m, n &lt;= 12</code></li> 
 <li><code>board[i][j]</code> is a lowercase English letter.</li> 
 <li><code>1 &lt;= words.length &lt;= 3 * 10<sup>4</sup></code></li> 
 <li><code>1 &lt;= words[i].length &lt;= 10</code></li> 
 <li><code>words[i]</code> consists of lowercase English letters.</li> 
 <li>All the strings of <code>words</code> are unique.</li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>String</li><li>Backtracking</li><li>Trie</li><li>Matrix</li></div></div><br><div><li>👍 9149</li><li>👎 435</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # build trie
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = '#'

        # dfs
        def dfs(i, j, node, pre, visited):
            if '#' in node:
                res.add(pre)
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                _i, _j = i + x, j + y
                if 0 <= _i < m and 0 <= _j < n and board[_i][_j] in node and (_i, _j) not in visited:
                    dfs(_i, _j, node[board[_i][_j]], pre + board[_i][_j], visited | {(_i, _j)})

        res = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        return list(res)
        
# leetcode submit region end(Prohibit modification and deletion)
