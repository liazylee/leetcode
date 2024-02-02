"""
<p>Given the <code>head</code> of a linked list and a value <code>x</code>, partition it such that all nodes <strong>less than</strong> <code>x</code> come before nodes <strong>greater than or equal</strong> to <code>x</code>.</p>

<p>You should <strong>preserve</strong> the original relative order of the nodes in each of the two partitions.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/partition.jpg" style="width: 662px; height: 222px;" /> 
<pre>
<strong>Input:</strong> head = [1,4,3,2,5,2], x = 3
<strong>Output:</strong> [1,2,2,4,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [2,1], x = 2
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li>The number of nodes in the list is in the range <code>[0, 200]</code>.</li> 
 <li><code>-100 &lt;= Node.val &lt;= 100</code></li> 
 <li><code>-200 &lt;= x &lt;= 200</code></li> 
</ul>

<div><div>Related Topics</div><div><li>Linked List</li><li>Two Pointers</li></div></div><br><div><li>👍 7147</li><li>👎 823</li></div>
"""
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # before_head = before = ListNode(0)
        # after_head = after = ListNode(0)
        # while head:
        #     if head.val < x:
        #         before.next = head
        #         before = before.next
        #     else:
        #         after.next = head
        #         after = after.next
        #     head = head.next
        # after.next = None
        # before.next = after_head.next
        # return before_head.next
        left_node, right_node = ListNode(0), ListNode(0)
        left_head, right_head = left_node, right_node
        while head:
            if head.val < x:
                left_node.next = head
                left_node = left_node.next
            else:
                right_node.next = head
                right_node = right_node.next
            head = head.next
        right_node.next = None
        left_node.next = right_head.next
        return left_head.next
        # while head:
        #     if head.val < x:
        #         left_node.next = head
        #         left_node = left_node.next
        #     else:
        #         right_node.next = head
        #         right_node = right_node.next
        #     head = head.next
        # right_node.next = None
        # left_node.next = right_head.next
        # return left_head.next


print(Solution().partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3))
# leetcode submit region end(Prohibit modification and deletion)
