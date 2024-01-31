"""
<p>Given the <code>head</code> of a linked&nbsp;list, rotate the list to the right by <code>k</code> places.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg" style="width: 450px; height: 191px;" /> 
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [4,5,1,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg" style="width: 305px; height: 350px;" /> 
<pre>
<strong>Input:</strong> head = [0,1,2], k = 4
<strong>Output:</strong> [2,0,1]
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li>The number of nodes in the list is in the range <code>[0, 500]</code>.</li> 
 <li><code>-100 &lt;= Node.val &lt;= 100</code></li> 
 <li><code>0 &lt;= k &lt;= 2 * 10<sup>9</sup></code></li> 
</ul>

<div><div>Related Topics</div><div><li>Linked List</li><li>Two Pointers</li></div></div><br><div><li>👍 9252</li><li>👎 1426</li></div>
"""
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n = 1
        cur = head
        while cur.next:
            n += 1
            cur = cur.next
        cur.next = head
        cur = head
        for _ in range(n - k % n - 1):
            cur = cur.next  # new tail
        new_head = cur.next  # new head
        cur.next = None  # cut the linked list
        return new_head


# print(Solution().rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))
# leetcode submit region end(Prohibit modification and deletion)
