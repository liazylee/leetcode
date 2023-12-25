"""
@author:liazylee
@license: Apache Licence
@time: 22/12/2023 15:56
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
"""
You are given a string letters made of N English letters. Count the number of different 
letters that appear in both uppercase and lowercase where all lowercase occurrences of the 
given letter appear before any uppercase occurrence.

For example, for letters = "aaAbcCABBc" the answer is 2. The condition is met for letters 
‘a’ and ‘b’, but not for ‘c’.

Write a function:

def solution(letters)

that, given a string letters, returns the number of different letters fulfilling the conditions above.

Examples:

1. Given letters = "aaAbcCABBc", the function should return 2, as explained above.

2. Given letters = "xyzXYZabcABC", the function should return 6.

3. Given letters = "ABCabcAefG", the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];

string letters is made only of letters (a−z and/or A−Z).
"""


def solution(letters):
    # letters_len = len(letters)
    # fullfill_letters = set()
    # lower_idxs = [0, 0]
    # upper_idxs = [0, 0]
    # last_lower = set()
    # lower_list = []
    # upper_list = []
    # for i, v in enumerate(letters):
    #     if i == 0 and v.isupper():
    #         break
    #     elif v.islower() and i + 1 < letters_len and letters[i + 1].isupper():
    #         lower_idxs[1] = i + 1
    #         upper_idxs = [i + 1, i + 2]
    #     elif v.isupper() and i + 1 < letters_len and letters[i + 1].islower():
    #         upper_idxs[1] = i + 1
    #         lower_list.append(set(letters[lower_idxs[0]:lower_idxs[1]]))
    #         upper_list.append(set(letters[upper_idxs[0]:upper_idxs[1]].lower()))
    #         lower_idxs = [i + 1, i + 2]
    #     elif v.islower() and i + 1 == letters_len:
    #         lower_idxs[1] = i + 1
    #         last_lower = set(letters[lower_idxs[0]:i + 1])
    #     elif v.isupper() and i + 1 == letters_len:
    #         upper_idxs[1] = i + 1
    #         lower_list.append(set(letters[lower_idxs[0]:lower_idxs[1]]))
    #         upper_list.append(set(letters[upper_idxs[0]:upper_idxs[1]].lower()))
    #
    # for i, v in enumerate(lower_list):
    #     diff_set = lower_list[i] - upper_list[i]
    #     fullfill_letters = (fullfill_letters | lower_list[i]) - diff_set
    #
    # fullfill_letters -= last_lower
    #
    # return len(fullfill_letters)
    lower_dict = {}
    upper_dict = {}
    count = 0
    for i, v in enumerate(letters):
        if v.isupper() and v not in upper_dict:
            upper_dict[v] = i
        elif v.islower():
            lower_dict[v] = i
    print(lower_dict, upper_dict)
    for i, index in lower_dict.items():
        if i.upper() in upper_dict and index < upper_dict[i.upper()]:
            count += 1
    return count


print(solution("aaAabcCABBc") == 1)
print(solution("xyzXYZabcABC") == 6)
print(solution("ABCabcAefG") == 0)
"""

You are given a task to fix potholes in a road. The road is described by a string S 
consisting of N characters. Each character represents a single fragment of the road.
Character '.' denotes a smooth surface and 'x' denotes a pothole. For example, S = 
 "...xxx..x" means that the road starts with three smooth fragments, followed by three
  potholes, followed by two smooth fragments and ending with one pothole.

You can choose any number of consecutive potholes and fix all of them. Fixing a segment 
consisting of K consecutive potholes costs K + 1. In the example above, fixing the first
 two consecutive potholes costs 2 + 1 = 3 and fixing the last pothole costs 1 + 1 = 2. 
 After these fixes, the road would look like this: ".....x...".

You are given a budget B. You can fix multiple segments containing potholes as long as
 you fit in the budget. What is the maximum number of potholes you can fix?

Write a function:

def solution(S, B)

that, given the string S of length N and the integer B, returns the maximum number 
of potholes that can be fixed.

Examples:

1. Given S = "...xxx..x....xxx." and B = 7, the function should return 5. You can 
start by fixing the first three consecutive potholes for a cost of 4, obtaining the
 road: "........x....xxx.". Then, you can fix the last two potholes for a cost of 3, 
 obtaining the road: "........x....x...". The total cost is 7, which fits in the budget,
  and you fix 5 potholes in total.

2. Given S = "..xxxxx" and B = 4, the function should return 3. One way is to fix the
 middle three potholes, which costs the whole budget and makes the road look as 
 follows: "..x...x". Alternatively, you could fix the first three potholes or the last three potholes.

3. Given S = "x.x.xxx...x" and B = 14, the function should return 6. You can fix 
all the potholes, which costs 2 + 2 + 4 + 2 = 10, leaving you with the spare budget
 of 4. This fixes the entire road.

4. Given S = ".." and B = 5, the function should return 0. There are no potholes to fix.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];

B is an integer within the range [0..200,000];

string S consists only of characters '.' and 'x'.
"""


# Test the function with the provided examples
# example1 = solution("...xxx..x....xxx.", 7)  # 5
# example2 = solution("..xxxxx", 4)  # 3
# example3 = solution("x.x.xxx...x", 14) # 6

# example4 = solution("..", 5) # 0

def solution1(S: str, B: int) -> int:
    x_remove = []
    x_efforts = 0
    for i in range(len(S)):
        if S[i] == 'x' and x_efforts == 0:
            x_efforts = 2
        elif S[i] == 'x' and x_efforts != 0:
            x_efforts += 1
        else:
            if x_efforts != 0:
                x_remove.append(x_efforts)
            x_efforts = 0
    x_remove.append(x_efforts)
    if sum(x_remove) <= B:
        return sum(x_remove) - len(x_remove)
    x_remove.sort(reverse=True)
    for i in range(len(x_remove)):
        sum_x = sum(x_remove[:i + 1])
        if sum_x > B:
            return sum_x - (sum_x - B) - i - 1

# print(solution1("...xxx..x....xxx.", 7))  # 5
# print(solution1("..xxxxx", 4))  # 3
# print(solution1("x.x.xxx...x", 14))  # 6
