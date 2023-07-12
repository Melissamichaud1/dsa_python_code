# TC = O(n^2)
# SC = O(n)

def find_sum_of_three(nums, target):
    # Sort the input list
    nums.sort()

    # Fix one integer at a time and find the other two
    for i in range(0, len(nums)-2):
        # Initialize the two pointers
        low = i + 1
        high = len(nums) - 1

        # Traverse the list to find the triplet whose sum equals the target
        while low < high:
            triplet = nums[i] + nums[low] + nums[high]

            # The sum of the triplet equals the target
            if triplet == target:
                return True

            # The sum of the triplet is less than target, so move the low pointer forward
            elif triplet < target:
                low += 1

            # The sum of the triplet is greater than target, so move the high pointer backward
            else:
                high -= 1

    # No such triplet found whose sum equals the given target
    return False

print(find_sum_of_three([3,5,2,6,7], 9))
"""
In the loop, we keep one value of the array with us and then look for the other two integers against this selected value that complete the triplet whose sum equals the target value.

First, we sort the input array, nums, in ascending order. This is because traversing an unsorted array would lead to a bad time complexity. If the input array is sorted, we can easily decide, depending on the sum of the current triplet, whether to move the low pointer toward the end, or, the high pointer toward the start. Next, we iterate over the elements in nums using the index i, where i
<
<
 length.nums - 2. Against each nums[i], we find the other two integers that complete the triplet whose sum equals the target value, that is, nums[i] + nums[low] + nums[high] == target. We do this by traversing nums with the low and high pointers. In each iteration, the traversal starts with the low pointer being at nums[i+1] and the high pointer at the last element of nums. Then, depending on the current sum value, we move these pointers as follows:

If the sum of the triplet is equal to the target, we return TRUE. Otherwise, we continue.

If the sum of the triplet is less than the target, we move the low pointer forward, that is, toward the end. The aim is to increase the value of the sum so that it gets closer or equal to the target value.

If the sum of the triplet is greater than the target, we move the high pointer toward the start. The aim is to reduce the value of the sum so that it gets closer or equal to the target value.

We repeat this for each iteration until we get the required triplet.
"""
