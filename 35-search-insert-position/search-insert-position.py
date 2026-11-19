class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0,len(nums)   # right is EXCLUSIVE

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1       # target is to the right
            else:
                right = mid          # nums[mid] >= target → mid is a candidate

        return left                  # first index where nums[left] >= target