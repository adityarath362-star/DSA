class Solution(object):
    def removeElement(self, nums, val):
        a=0
        for b in range(len(nums)):
            if nums[b]!=val:
                nums[a]=nums[b]
                a+=1

        return a      
