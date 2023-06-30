# Happy Number
"""
Write an algorithm to determine if a number n is a happy number.

We use the following process to check if a given number is a happy number:

Starting with the given number n, replace the number with the sum of the
squares of its digits.

Repeat the process until:
    - The number equals 1, which will depict that the given number n is a
    happy number.
    - It enters a cycle, which will depict that the given number n is not
    a happy number.

Return TRUE if n is a happy number, and FALSE if not.

"""

# TC = O(logn)
# SC = O(1)

def is_happy_number(n):
    # Helper function
    def sum_of_squared_digits(number):
        total_sum = 0
        while number > 0:
            digit = number % 10 # Right digit
            number = number // 10 # Remaining digit
            total_sum += digit ** 2 # Squares right digit, add to total sum
        return total_sum

    slow = n
    fast = sum_of_squared_digits(n)

    while fast != 1 and fast != slow:
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))

    return fast == 1


"""The sum_of_squared_digits function is a helper function that calculates the sum of the squares of the digits of a given number. It iterates over the digits of the number, squares each digit, and adds the squared value to the total_sum. It then removes the rightmost digit from the number by using the line number = number // 10.

The is_happy_number function takes a number n as input and follows a process to determine if it is a happy number. Here's a step-by-step explanation of how it works:

Initialize two variables, slow and fast, with the value of n. These variables will be used to track the progression of the process.

Enter a while loop that continues until either fast becomes 1 (indicating that n is a happy number) or fast becomes equal to slow (indicating the presence of a cycle).

Inside the while loop, update slow by calling sum_of_squared_digits(slow) to calculate the sum of squared digits of slow. This represents a single step in the process.

Update fast twice by calling sum_of_squared_digits(sum_of_squared_digits(fast)). This is done to simulate two steps in the process. By updating fast twice as fast as slow, it allows us to detect a cycle if one exists.

Check the conditions of the while loop again. If fast is equal to 1, it means n is a happy number, so we exit the loop. If fast is equal to slow, it means a cycle has been detected, and n is not a happy number.

Return the result by checking if fast is equal to 1. If it is, the function returns True, indicating that n is a happy number. Otherwise, it returns False.

"""
