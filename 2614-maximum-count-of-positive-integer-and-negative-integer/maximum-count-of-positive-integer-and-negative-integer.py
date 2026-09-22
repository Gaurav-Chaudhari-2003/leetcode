class Solution:
    def maximumCount(self, nums: list[int]) -> int:

        left = 0
        right = len(nums)-1

        
        # find largest negative
        while left <= right:
            mid = (right + left) // 2

            if nums[mid] < 0:
                left = mid + 1
            elif nums[mid] >= 0:
                right = mid - 1
        
        negative_count = left


        # find smallest positive
        positive_count = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            
            if nums[mid] > 0:
                positive_count = len(nums) -  mid
                right = mid - 1
            elif nums[mid] <= 0:
                left = mid + 1
        
        return max(negative_count, positive_count)