# https://leetcode.com/problems/single-number/

# Given an array of integers, every element appears twice except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sol = 0
        for n in nums:
            sol = sol ^ n
        return sol