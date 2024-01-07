"""
<p>Implement the <code>RandomizedSet</code> class:</p>

<ul> 
 <li><code>RandomizedSet()</code> Initializes the <code>RandomizedSet</code> object.</li> 
 <li><code>bool insert(int val)</code> Inserts an item <code>val</code> into the set if not present. Returns <code>true</code> if the item was not present, <code>false</code> otherwise.</li> 
 <li><code>bool remove(int val)</code> Removes an item <code>val</code> from the set if present. Returns <code>true</code> if the item was present, <code>false</code> otherwise.</li> 
 <li><code>int getRandom()</code> Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the <b>same probability</b> of being returned.</li> 
</ul>

<p>You must implement the functions of the class such that each function works in&nbsp;<strong>average</strong>&nbsp;<code>O(1)</code>&nbsp;time complexity.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
<strong>Output</strong>
[null, true, false, true, 2, true, false, 2]

<strong>Explanation</strong>
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li> 
 <li>At most <code>2 *&nbsp;</code><code>10<sup>5</sup></code> calls will be made to <code>insert</code>, <code>remove</code>, and <code>getRandom</code>.</li> 
 <li>There will be <strong>at least one</strong> element in the data structure when <code>getRandom</code> is called.</li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Hash Table</li><li>Math</li><li>Design</li><li>Randomized</li></div></div><br><div><li>👍 8333</li><li>👎 493</li></div>
"""
import random


# leetcode submit region begin(Prohibit modification and deletion)
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_table = {}  # {val:index}
        self.arr = []  # [val]

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        """
        if val not in self.hash_table:
            self.hash_table[val] = len(self.arr)  # index of the new element{val:index}
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hash_table:
            self.hash_table[self.arr[-1]] = self.hash_table[val]  # update the index of the last element
            self.arr[self.hash_table[val]] = self.arr[-1]  # update the last element

            self.arr.pop()
            self.hash_table.pop(val)

            return True

        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# leetcode submit region end(Prohibit modification and deletion)
