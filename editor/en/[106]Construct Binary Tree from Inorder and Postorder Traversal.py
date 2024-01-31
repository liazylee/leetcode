"""
<p>Given two integer arrays <code>inorder</code> and <code>postorder</code> where <code>inorder</code> is the inorder traversal of a binary tree and <code>postorder</code> is the postorder traversal of the same tree, construct and return <em>the binary tree</em>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="width: 277px; height: 302px;" /> 
<pre>
<strong>Input:</strong> inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
<strong>Output:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> inorder = [-1], postorder = [-1]
<strong>Output:</strong> [-1]
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>1 &lt;= inorder.length &lt;= 3000</code></li> 
 <li><code>postorder.length == inorder.length</code></li> 
 <li><code>-3000 &lt;= inorder[i], postorder[i] &lt;= 3000</code></li> 
 <li><code>inorder</code> and <code>postorder</code> consist of <strong>unique</strong> values.</li> 
 <li>Each value of <code>postorder</code> also appears in <code>inorder</code>.</li> 
 <li><code>inorder</code> is <strong>guaranteed</strong> to be the inorder traversal of the tree.</li> 
 <li><code>postorder</code> is <strong>guaranteed</strong> to be the postorder traversal of the tree.</li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Hash Table</li><li>Divide and Conquer</li><li>Tree</li><li>Binary Tree</li></div></div><br><div><li>👍 7793</li><li>👎 125</li></div>
"""
from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(root.val)
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])
        return root

# leetcode submit region end(Prohibit modification and deletion)
