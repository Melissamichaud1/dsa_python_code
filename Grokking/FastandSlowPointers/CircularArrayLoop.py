"""
An input array, nums containing non-zero integers, is given, where the
value at each index represents the number of places to skip forward
(if the value is positive) or backward (if the value is negative).
When skipping forward or backward, wrap around if you reach either end
of the array. For this reason, we are calling it a circular array.
Determine if this circular array has a cycle. A cycle is a sequence of
indices in the circular array characterized by the following:

- The same set of indices is repeated when the sequence is traversed in
accordance with the aforementioned rules.
- The length of the sequence is at least two.
- The loop must be in a single direction, forward or backward.
- It should be noted that a cycle in the array does not have to originate
at the beginning. A cycle can begin from any point in the array.
"""

def circular_array_loop(nums):
    size = len(nums)
    # Iterate through each index of the array 'nums'.
    for i in range(size):
        # Set slow and fast pointer at current index value.
        slow = fast = i

        # Set true in 'forward' if element is positive, set false otherwise.
        forward = nums[i] > 0

        while True:
            # Move slow pointer to one step.
            slow = next_step(slow, nums[slow], size)
            # If cycle is not possible, break the loop and start from next element.
            if is_not_cycle(nums, forward, slow):
                break

            # First move of fast pointer.
            fast = next_step(fast, nums[fast], size)
            # If cycle is not possible, break the loop and start from next element.
            if is_not_cycle(nums, forward, fast):
                break

            # Second move of fast pointer.
            fast = next_step(fast, nums[fast], size)
            # If cycle is not possible, break the loop and start from next element.
            if is_not_cycle(nums, forward, fast):
                break

            # At any point, if fast and slow pointers meet each other,
            # it indicate that loop has been found, return True.
            if slow == fast:
                return True

    return False

# A function to calculate the next step
def next_step(pointer, value, size):
    result = (pointer + value) % size
    if result < 0:
        result += size
    return result

# A function to detect a cycle doesn't exist
def is_not_cycle(nums, prev_direction, pointer):

    # Set current direction to True if current element is positive, set False otherwise.
    curr_direction = nums[pointer] >= 0
    # If current direction and previous direction is different or moving a pointer takes back to the same value,
    # then the cycle is not possible, we return True, otherwise return False.
    if (prev_direction != curr_direction) or (abs(nums[pointer] % len(nums)) == 0):
        return True
    else:
        return False
