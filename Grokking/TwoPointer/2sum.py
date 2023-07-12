def find_sum_of_2(nums, target):
    nums.sort()
    low = 0
    high = len(nums) - 1

    while low < high:
        current_sum = nums[low] + nums[high]
        if current_sum == target:
            return True
        elif current_sum < target:
            low += 1
        else:
            high -= 1

    return False

print(find_sum_of_2([1, 3, 5, 7, 9], 14))

"""The time complexity of the refactored find_sum_of_2 function is O(n),
where n is the length of the nums list. This is because the function performs
a single pass through the sorted list using two pointers, low and high, and
adjusts their positions based on the sum of the numbers at those indices.
The function terminates when low is equal to or greater than high or when it
finds a pair with the target sum.

The space complexity of the function is O(1) because it uses a constant
amount of additional space regardless of the input size. The function only
utilizes a few variables (low, high, and current_sum) to keep track of indices
and the current sum. The space consumption does not depend on the size of the input list."""
