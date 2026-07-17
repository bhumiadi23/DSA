class Solution:

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high
        while i < j:
            while i <= high - 1 and arr[i] <= pivot:
                i += 1
            while j >= low + 1 and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quickSort(self, arr, low, high):
        if low < high:
            pIndex = self.partition(arr, low, high)
            self.quickSort(arr, low, pIndex - 1)
            self.quickSort(arr, pIndex + 1, high)

nums=list(map(int,input().split()))
obj=Solution()
obj.quickSort(nums,0,len(nums)-1)
print(*nums)