# Valid Palindrome
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
# TC = O(n) -> n is len of input string
# SC = O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize 2 pointers: beginning and end indices of string
        left = 0
        right = len(s) - 1

        # Condition contiues until pointers meet or cross
        while left < right:

            # if character at left position is not alphanumeric,
            # continue statement to move to the next iteration of
            # the loop without executing the remaining code.
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            # After both checks, if the characters at s[left] and
            # s[right] (converted to lowercase) are not equal, it
            # means that the string is not a palindrome, and the
            # method returns False.
            if  s[left].lower() != s[right].lower():
                return False

            # If characters at right and left are equal, this
            # code moves the pointers closer toward the middle
            # for the next iteration
            left += 1
            right -= 1

        return True

"""

This code defines a class Solution with a method isPalindrome that checks whether a given string s is a palindrome.

The method starts by initializing two pointers, left and right, which are set to the beginning and end indices of the string s, respectively (left = 0 and right = len(s) - 1).

The code then enters a while loop with the condition left < right. This loop continues until the left and right pointers meet or cross each other.

Inside the loop, the code checks if the character at the left position in s is alphanumeric (a letter or a digit) using the isalnum() method. If it is not alphanumeric, the code increments the left pointer by 1 and uses the continue statement to move to the next iteration of the loop without executing the remaining code. This step ensures that only alphanumeric characters are considered for the palindrome check.

Similarly, the code checks if the character at the right position in s is alphanumeric. If it is not, the code decrements the right pointer by 1 and continues to the next iteration of the loop.

After both checks, if the characters at s[left] and s[right] (converted to lowercase) are not equal, it means that the string is not a palindrome, and the method returns False.

If the characters at s[left] and s[right] are equal, the code increments left by 1 and decrements right by 1 to move the pointers closer to each other for the next iteration.

Once the while loop finishes, it means that all the pairs of characters have been compared, and the string s is a palindrome. In this case, the method returns True
"""
