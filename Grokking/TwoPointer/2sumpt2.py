def two_sum(nums, target):
    # Create a dictionary to store the complement value and its corresponding index
    complement_dict = {}

    # Iterate through the list
    for i, num in enumerate(nums):
        complement = target - num
        # Check if the complement value exists in the dictionary
        if complement in complement_dict:
            # Return the indices of the two numbers that add up to the target
            return [complement_dict[complement], i]
        # Add the current number and its index to the dictionary
        complement_dict[num] = i

    # If no solution is found, return an empty list
    return []

print(two_sum([2, 7, 11, 15], 9))
