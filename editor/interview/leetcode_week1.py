"""
@author:liazylee
@license: Apache Licence
@time: 06/01/2024 14:39
@contact: li233111@gmail.com
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from collections import deque
from datetime import datetime
from functools import cache

"""
You are given a 0-indexed array of integers nums.

A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.

Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

 

Example 1:

Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
Example 2:

Input: nums = [3,4,5,1,12,14,13]
Output: 15
Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50

"""
from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        if not nums:
            return 1
        if len(nums) == 1:
            return nums[0] + 1
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                prefix.append(nums[i])
            else:
                sum_prefix = sum(prefix)
                if sum_prefix not in nums:
                    return sum_prefix
                else:
                    while sum_prefix in nums:
                        sum_prefix += 1
                    return sum_prefix
        return sum(prefix)


"""

100168. Minimum Number of Operations to Make Array XOR Equal to K
User Accepted:2141
User Tried:2367
Total Accepted:2178
Total Submissions:2626
Difficulty:Medium
You are given a 0-indexed integer array nums and a positive integer k.

You can apply the following operation on the array any number of times:

Choose any element of the array and flip a bit in its binary representation. Flipping a bit means changing a 0 to 1 or vice versa.
Return the minimum number of operations required to make the bitwise XOR of all elements of the final array equal to k.

Note that you can flip leading zero bits in the binary representation of elements. For example, for the number (101)2 you can flip the fourth bit and obtain (1101)2.

 

Example 1:

Input: nums = [2,1,3,4], k = 1
Output: 2
Explanation: We can do the following operations:
- Choose element 2 which is 3 == (011)2, we flip the first bit and we obtain (010)2 == 2. nums becomes [2,1,2,4].
- Choose element 0 which is 2 == (010)2, we flip the third bit and we obtain (110)2 = 6. nums becomes [6,1,2,4].
The XOR of elements of the final array is (6 XOR 1 XOR 2 XOR 4) == 1 == k.
It can be shown that we cannot make the XOR equal to k in less than 2 operations.
Example 2:

Input: nums = [2,0,2,0], k = 0
Output: 0
Explanation: The XOR of elements of the array is (2 XOR 0 XOR 2 XOR 0) == 0 == k. So no operation is needed."""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        current_xor = 0
        for num in nums:
            current_xor ^= num

        # XOR with k to find differing bits
        diff = current_xor ^ k

        # Count the number of set bits in diff
        operations = 0
        while diff:
            operations += diff & 1
            diff >>= 1

        return operations


print(Solution().minOperations([2, 1, 3, 4], 1))  # 2

"""
100159. Minimum Number of Operations to Make X and Y Equal
User Accepted:452
User Tried:892
Total Accepted:459
Total Submissions:1292
Difficulty:Medium
You are given two positive integers x and y.

In one operation, you can do one of the four following operations:

Divide x by 11 if x is a multiple of 11.
Divide x by 5 if x is a multiple of 5.
Decrement x by 1.
Increment x by 1.
Return the minimum number of operations required to make x and y equal."""


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        queue = deque([(x, 0)])
        visited = set([x])

        while queue:
            current, ops = queue.popleft()

            # Check if the current value is equal to y
            if current == y:
                return ops

            # Perform the operations
            next_steps = []
            if current % 11 == 0:
                next_steps.append(current // 11)
            if current % 5 == 0:
                next_steps.append(current // 5)
            next_steps.append(current - 1)
            next_steps.append(current + 1)

            for next_step in next_steps:
                if next_step not in visited and next_step >= 0:
                    visited.add(next_step)
                    queue.append((next_step, ops + 1))

        # If y cannot be reached
        return -1


"""
100163. Count the Number of Powerful Integers
User Accepted:12
User Tried:213
Total Accepted:13
Total Submissions:396
Difficulty:Hard
You are given three integers start, finish, and limit. You are also given a 0-indexed string s representing a positive integer.

A positive integer x is called powerful if it ends with s (in other words, s is a suffix of x) and each digit in x is at most limit.

Return the total number of powerful integers in the range [start..finish].

A string x is a suffix of a string y if and only if x is a substring of y that starts from some index (including 0) in y and extends to the index y.length - 1. For example, 25 is a suffix of 5125 whereas 512 is not.

 

Example 1:

Input: start = 1, finish = 6000, limit = 4, s = "124"
Output: 5
Explanation: The powerful integers in the range [1..6000] are 124, 1124, 2124, 3124, and, 4124. All these integers have each digit <= 4, and "124" as a suffix. Note that 5124 is not a powerful integer because the first digit is 5 which is greater than 4.
It can be shown that there are only 5 powerful integers in this range.
Example 2:

Input: start = 15, finish = 215, limit = 6, s = "10"
Output: 2
Explanation: The powerful integers in the range [15..215] are 110 and 210. All these integers have each digit <= 6, and "10" as a suffix.
It can be shown that there are only 2 powerful integers in this range.
Example 3:

Input: start = 1000, finish = 2000, limit = 4, s = "3000"
Output: 0
Explanation: All integers in the range [1000..2000] are smaller than 3000, hence "3000" cannot be a suffix of any integer in this range.
 

Constraints:

1 <= start <= finish <= 1015
1 <= limit <= 9
1 <= s.length <= floor(log10(finish)) + 1
s only consists of numeric digits which are at most limit.
s does not have leading zeros."""


class Solution:

    # def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
    # if int(s) > finish:
    #     return 0
    #
    # def check_limit(num):
    #     return limit >= int(max(str(num)))
    #
    # prefix, count = 0, 0
    #
    # def next_valid_prefix(prefix):
    #     prefix_str = str(prefix)
    #     for i, digit in enumerate(prefix_str):
    #         if int(digit) > limit:
    #             if i == 0:
    #                 # Handle overflow
    #                 return int('1' + '0' * len(prefix_str))
    #             new_prefix = int(prefix_str[:i]) + 1
    #             new_prefix_str = str(new_prefix) + '0' * (len(prefix_str) - i)
    #             return int(new_prefix_str)
    #     return prefix + 1
    #
    # # print(count)
    # time = datetime.now()
    # while int(str(prefix) + s) <= finish:
    #     res = int(str(prefix) + s)
    #     if res >= start and check_limit(res):
    #         count += 1
    #     prefix = next_valid_prefix(prefix)
    # print(datetime.now() - time, f'prefix:{prefix}')
    # return count
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        time = datetime.now()
        s = [*map(int, str(s))]
        print(s)

        def a(f):
            f = [*map(int, str(f))]
            if len(f) < len(s):
                return 0

            @cache
            def ans(pos, islower):
                if pos == len(f):
                    return 1
                candidates = list(range(limit + 1)) if islower else list(range(min(limit, f[pos]) + 1))
                if len(f) - pos <= len(s):
                    candidates = [s[len(s) - (len(f) - pos)]]
                res = 0
                for d in candidates:
                    if islower or d <= f[pos]:
                        res += ans(pos + 1, islower or d < f[pos])
                return res

            return ans(0, False)

        print(datetime.now() - time, f'prefix:{start}')
        return a(finish) - a(start - 1)


print(Solution().numberOfPowerfulInt(1114,
                                     1864854501,
                                     7,
                                     "26"))  # 5
"""
0:00:18.437401 prefix:18648545
4194295

0:00:09.848413 prefix:20000000
4194295
0:00:00.000010 prefix:11
4194295
0:00:00.000009 prefix:1114
4194295
"""
