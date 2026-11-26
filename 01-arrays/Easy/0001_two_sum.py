"""
Problem: Two Sum
LeetCode: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: 01 – Arrays
Pattern: Hash Map / Array Lookup

Time Complexity: [Your analysis]
Space Complexity: [Your analysis]

"""

class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        # Iterate through each element
        for i in range(n):
            # Check every element after i to avoid duplicates and using the same element twice
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

        
"""
Approach: Use two nested loops to check every possible pair of elements in the array and see if their sum equals the target. 
If a matching pair is found, return their indices; otherwise, return an empty list.
"""

