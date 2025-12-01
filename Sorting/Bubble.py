class Solution:
    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n):
            swapped = False

            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            if not swapped:
                break
        
        return arr

obj = Solution()
print(obj.bubbleSort([5, 2, 8, 1, 3]))
