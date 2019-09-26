# 1. Iterative binarySearch
def binarySearch1(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 2. Recursive binarySearch
def binarySearch2(nums, target, left, right):
    if left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binarySearch2(nums, target, mid+1, right)
        else:
            return binarySearch2(nums, target, left, mid-1)
    else:
        return -1

# 3. First occurrance in the list
def binarySearch3(nums, target):
    left = 0
    right = len(nums)-1
    first = -1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            first = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first

# 4. Last occurrance in the list
def binarySearch4(nums, target):
    left = 0
    right = len(nums)-1
    last = -1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            last = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last

# 5. Randomize binarySearch
from random import randint
def binarySearch5(nums, target):
    left = 0
    right = len(nums)-1
    while (left <= right):
        mid = randint(left, right)
        if (nums[mid] == target):
            return mid
        elif (nums[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 6. Rotated array binarySearch
def binarySearch6(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if target < nums[mid] and target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
