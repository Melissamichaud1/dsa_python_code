# Palindrome Number
"""
Given an integer x, return true if x is a
palindrome , and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

# Solution 1: Turn int to string, reverse it
# class Solution(object):
#     def isPalindrome(self, x):
#         x = str(x)
#         return x == x[::-1]

# Solution 2: Reverse half
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        half = 0
        while x > half:
            half = (half * 10) + (x % 10)
            x = x // 10
        return x == half or x == half // 10

solution = Solution()
print(solution.isPalindrome(123321))

"""
The function isPalindrome takes one parameter, x, which is the integer to check for palindrome.

It begins with an initial check. If x is negative or if it is a non-zero multiple of 10 (ends with 0), it cannot be a palindrome since leading zeros are not allowed in integers. In such cases, the code returns False.

Next, it initializes a variable half to 0. This variable will store the reversed half of the original number.

The code enters a while loop that continues until the remaining part of the number x becomes less than or equal to half.

Inside the loop, it updates half by multiplying it by 10 and adding the last digit of x (obtained using x % 10). This effectively reverses the digits of x and adds them to half.

After updating half, it reduces x by dividing it by 10 (x = x // 10). This removes the last digit of x, moving towards the middle of the number.

The loop continues until x becomes smaller than or equal to half.

Once the loop exits, it checks if the original number x is equal to half (for numbers with an odd number of digits) or if x is equal to half // 10 (for numbers with an even number of digits). This accounts for cases where the middle digit is not significant for palindrome checks.

If the condition in step 8 is true, it means the original number is a palindrome, and the code returns True. Otherwise, it returns False.

In summary, the code reverses the digits of the input number partially (up to the middle) using the half variable. Then, it compares the original number with the reversed half to determine if it is a palindrome. By only reversing half of the number, the code achieves an optimal solution with a time complexity of O(log10(n)), where n is the value of the input number.
"""

# Solution 3: Compare first and last digits and move inward
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = (reversed_half * 10) + (x % 10)
            x //= 10

        # If the number of digits is odd, we can ignore the middle digit
        return x == reversed_half or x == reversed_half // 10

"""
We rename the variable half to reversed_half for clarity.

Instead of checking for equality between x and reversed_half, we add an additional condition to check for equality between x and reversed_half // 10 when the number of digits is even. This accounts for cases where the middle digit can be ignored.

By implementing this optimization, the code avoids reversing the entire number and only checks half of it, resulting in a more efficient solution. The time complexity remains O(log10(n)), but the code requires fewer operations overall.

"""
