# First Leet Code Problem Two Sum

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
# My Solution

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        
# logic
# for each number in the list, check if the sum of that number and another number in the
# list is equal to the target. If it is, return the indices of those numbers.
# This solution is O(n^2) time complexity and O(1) space complexity.

# learning reference
# https://www.youtube.com/watch?v=xZFoZvhnVTU