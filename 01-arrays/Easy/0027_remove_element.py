"""
Problem: Remove Element
LeetCode: https://leetcode.com/problems/remove-element/
Difficulty: Easy
Topic: 01 – Arrays
Pattern: Two Pointers

Time Complexity: [Your analysis]
Space Complexity: [Your analysis]

Approach:
Write your own explanation after solving.
"""

class Solution(object):
    def removeElement(self, nums, val):

        k = 0

        for i in range(len(nums)):

            if nums[i] != val:

                nums[k] = nums[i]

                k += 1

        return k
