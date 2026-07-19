class Solution:
    def secondLargestElement(self, nums):
        largest=nums[0]
        s_largest=-1
        for i in range(len(nums)):
            if nums[i]>largest:
                largest=nums[i]
        for i in range(len(nums)):
            if nums[i]>s_largest and nums[i]!=largest:
                s_largest=nums[i]

        return s_largest


# Driver Code
nums = list(map(int, input().split()))

obj = Solution()
print(obj.secondLargestElement(nums))
