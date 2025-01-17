class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1={}
        
        maj_element_cond=len(nums)//2

        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
            if dict1[i] > maj_element_cond:
                return i
                

        