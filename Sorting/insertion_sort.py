class Solution:
    def insertionSort(self, arr):
        n = len(arr)

        for i in range(1, n):
            j = i

            while j > 0 and arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1

        return arr


# Driver Code
nums = list(map(int, input().split()))

obj = Solution()
print(*obj.insertionSort(nums))
