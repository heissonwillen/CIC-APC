'''https://leetcode.com/problems/two-sum/
'''


# def two_sum(nums, target):
#     for i, num_i in enumerate(nums):
#         for j, num_j in enumerate(nums[i+1:]):
#             if num_i + num_j == target:
#                 return [i, i+j+1]


# def two_sum(nums, target):
#     complement_dict = {}
#     for i, num in enumerate(nums):
#         complement_dict[num] = i

#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in complement_dict and complement_dict[complement] != i:
#             return [i, complement_dict[complement]]


def two_sum(nums, target):
    complement_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement not in complement_dict:
            complement_dict[num] = i
        else:
            return [i, complement_dict[complement]]


print(two_sum([2, 7, 11, 15], 9))
'''Output: [0,1]
'''

print(two_sum([3, 2, 4], 6))
'''Output: [1,2]
'''

print(two_sum([3, 3], 6))
'''Output: [0,1]
'''
