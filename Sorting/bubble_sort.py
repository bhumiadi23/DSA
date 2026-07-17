class Solution:
    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n - 1, -1, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp


# Driver Code
nums = list(map(int, input().split()))

obj = Solution()
obj.bubbleSort(nums)

print(*nums)
