class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_dict={}
        i=0
        while i<len(nums):
            num=nums[i]
            if num in target_dict.keys():
                return [target_dict[num],i]
            target_dict[target-num]=i
            i+=1