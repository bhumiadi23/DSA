class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums)-1):
            mini=i

            for j in range(i,len(nums)):
                if nums[j]<nums[mini]:
                    mini=j
                
            nums[i],nums[mini]=nums[mini],nums[i]

        return nums
