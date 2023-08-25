'''
**Problem**: **Rotate Array**

Given an array, rotate the array to the right by `k` steps, where `k` is a non-negative integer.

**Input**:
- `nums`: A list of integers representing the array.
- `k`: An integer representing the number of steps to rotate.

**Output**:
- Modify the `nums` array in-place.

**Example**:

```
Input:
nums = [1,2,3,4,5,6,7], k = 3

Output:
[5,6,7,1,2,3,4]

Explanation:
Rotate the array by 1 step: [7,1,2,3,4,5,6]
Rotate the array by 2 steps: [6,7,1,2,3,4,5]
Rotate the array by 3 steps: [5,6,7,1,2,3,4]
```

**Constraints**:
1. Try to solve this problem using `O(1)` extra space (i.e., in-place without using any auxiliary arrays).
2. Avoid using built-in functions to solve the problem directly (e.g., don't just use Python's `list slicing` or `rotate` methods to get the answer).
3. How can you handle cases where `k` is larger than the array's length?
'''


# Array is given
# rotate the array to right by k steps
# [4,4,5,6,2,2]  k = 3 [6,2,2,4,4,5]



'''
Bruet Force Approach:

- Start loop from j = lengh - k, where i = 0
- at each iteration take that element and update with k-i and update k - 

       j
[4,4,5,6,2,2]

 i
[4,4,5,6,2,2]


         j    // j = lentgth - k + i   
[6,4,5,4,2,2]

    i         // i < k
[6,4,5,4,2,2]
'''


def reverse_array(arr, start, end):
    # [1,2,3,4,5,6,7]
    # []
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

        start += 1
        end -= 1



def rotate_array(arr, k):
    # if k > len(arr) then len(arr) % k = modulos
    # reverse array [7,6,5,4,3,2,1]
    # reverse first 3 [5,6,7,4,3,2,1]
    # [5,6,7,1,2,3,4]
    if k > len(arr):
        k = k % len(arr)

    reverse_array(arr, 0, len(arr) - 1)
    reverse_array(arr, 0, k - 1)
    reverse_array(arr, k, len(arr) - 1)
    return arr