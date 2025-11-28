def func(num, left, right):
    if left >= right:
        return
    num[left], num[right] = num[right], num[left]
    func(num, left + 1, right - 1)

def reverse(num):
    func(num, 0, len(num) - 1)
    return num

arr = [1, 2, 3, 4, 5]
print("Original:", arr)
print("Reversed:", reverse(arr))

