class Solution(object):
    def twoSum(self, nums, target): 
        h_table = {}
        for index, number in enumerate(nums):
            value = target - number
            if value in h_table:
                return [h_table[value], index]
            h_table[number] = index
