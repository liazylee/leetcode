"""


The developers at Amazon employ several algorithms for encrypting passwords. In one algorithm, the developers aim to encrypt palindromic passwords. Palindromic passwords are ones that read the same forward and backward.

The algorithm rearranges the characters to have the following characteristics:

It is a rearrangement of the original palindromic password.
It is also a palindrome.
Among all such palindromic rearrangements, it is the lexicographically smallest.
Given the original palindromic password that consists of lowercase English characters only, find the encrypted password.

A string s is considered to be lexicographically smaller than the string t of the same length if the first character in s that differs from that in t is smaller. For example, "abcd" is lexicographically smaller than "abdc" but larger than "abad"

Note that the encrypted password might be the same as the original password if it is already lexicographically smallest.

Example
The original password is password = "babab".
This can be rearranged to form abbba, which is both a rearrangement of the original password and the lexicographically smallest palindrome.

It satisfies all the requirements so return the string abbba.

Function Description
Complete the function findEncryptedPassword in the editor below.

findEncryptedPassword has the following parameter:

string password: the original palindromic password

"""
from collections import Counter
from typing import List


def findEncryptedPassword(password: str) -> str:
    # Write your code here
    if not password:
        return ''
    n = len(password)
    if n == 1:
        return password
    odd_char = None
    password = Counter(password)
    password_items = sorted(password.items(), key=lambda x: (x[1], x[0],), reverse=False)
    for char, count in password_items:
        if count % 2 != 0:
            if odd_char is not None:
                return "can't form a palindrome."
            odd_char = char
            password[char] -= 1
    half_palindrome = ''.join([c * (n // 2) for c, n in password_items])
    return half_palindrome + odd_char + half_palindrome[::-1]


# print(findEncryptedPassword('babab'))
# print(findEncryptedPassword('yxzzzxy'))

"""
Amazon has multiple delivery centers for the distribution of its goods. In one such center, parcels are arranged in a sequence where the ith
parcel has a weight of  
weight[i]. A shipment is constituted of a contiguous segment of parcels in this arrangement. That is, for 3 parcels 
arranged with weights [3, 6, 3], a shipment can be formed of parcels with weights [3], [6], [3], [3, 6], [6, 3] and 
[3, 6, 3] but not with weights [3, 3]. These shipments are to be loaded for delivery and must be balanced.
A shipment is said to be balanced if the weight of the last parcel of the shipment is not the maximum weight 
among all the weights in that shipment. For example, shipment with weights [3, 9, 4, 7] is balanced since the last
 weight is 7 while the maximum shipment weight is 9. However, the shipment [4, 7, 2, 7] is not balanced.

Given the weights of parcels placed in a sequence, find the maximum number of shipments that can be formed such that each parcel belongs to exactly one shipment, each shipment consists of only a contiguous segment of parcels, and each shipment is balanced. If there are no balanced shipments, return 0.

Example
weight=[1,2,3,2,6,3]

There are 
n=6 parcels to ship. The parcels can be divided into two shipments: 
[1,2,3,2] and [6,3], each of which is balanced. It can also be shown...
that this is the maximum number of shipments that can be formed, thus the function should return 2.

Function Description
Complete the function
findMaximumBalancedShipments in the editor
below.
findMaximumBalancedShipments has the
following parameter:
int weights: the weights of the parcels
Returns
int: the maximum possible number of balanced shipments that can be formed.
"""


def findMaximumBalancedShipments(weights: List) -> int:
    windows = [weights[0]]
    previous, current_max = weights[0], weights[0]
    shipments = 0
    for i in range(1, len(weights)):
        if weights[i] > previous or weights[i] == current_max:
            windows.append(weights[i])
            previous = weights[i]
            current_max = max(windows)
            if i == len(weights) - 1 and len(windows) > 1 and weights[i] != current_max:
                shipments += 1

        else:
            if i == len(weights) - 2 and windows[-1] == current_max:
                windows.append(weights[i])
            else:
                windows.append(weights[i])
                shipments += 1
                windows = []
                previous = 0
    return shipments


# def findMaximumBalancedShipments(weights: List[int]) -> int:
#     # If there's only one weight, it cannot form a balanced shipment.
#     if len(weights) <= 1:
#         return 0
#
#     shipments = 0
#     current_max = weights[0]
#
#     # Start from the second element since the first element initializes current_max.
#     for i in range(1, len(weights)):
#         if weights[i] > current_max:
#             # If current weight is greater than the max in the current shipment,
#             # start a new shipment.
#             shipments += 1
#             current_max = weights[i]
#         else:
#             # Update the max in the current shipment if needed.
#             current_max = max(current_max, weights[i])
#
#         # If it's the last weight and not equal to the current max,
#         # then it should form the end of a balanced shipment.
#         if i == len(weights) - 1 and weights[i] != current_max:
#             shipments += 1
#
#     return shipments


#
print(findMaximumBalancedShipments([1, 2, 3, 2, 6, 3]))  # 2

print(findMaximumBalancedShipments([8, 5, 4, 7, 2]))  # 2

print(findMaximumBalancedShipments([3, 9, 4, 7]))  # 1
print(findMaximumBalancedShipments([4, 7, 2, 7]))  # 0
print(findMaximumBalancedShipments([2, 3, 6, 2, 3, 5]))  # 1
print(findMaximumBalancedShipments([1, 2, 3, 2, 6, 3, 7]))  # 2
