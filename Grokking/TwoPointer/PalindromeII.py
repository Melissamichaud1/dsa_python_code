"""Write a function that takes a string as input and checks whether it can be a valid palindrome by removing at most one character from it.
"""
# TC = O(n)
# SC = O(1)
def is_palindrome(s):
  left = 0
  right = len(s) - 1
  while left <= right:
    if s[left] != s[right]:
      # Check the two possibilities when a mismatch is found
      substring1 = s[left+1:right+1]
      substring2 = s[left:right]

      if substring1 == substring1[::-1] or substring2 == substring2[::-1]:
        return True
      else:
        return False
    left += 1
    right -= 1
  return True

  """
The given code defines a function is_palindrome that checks whether a given string s can be a valid palindrome by removing at most one character. Let's break down the code and analyze its time and space complexity.

The code initializes two pointers, left and right, which represent the indices of the leftmost and rightmost characters of the string s respectively.

The code enters a while loop that continues until the left pointer is less than or equal to the right pointer.

Within the loop, the code checks if the characters at the left and right indices are different. If a mismatch is found, it proceeds to check the two possibilities when a character needs to be removed.

The code creates two substrings, substring1 and substring2, which are extracted from the input string s based on the left and right indices. substring1 excludes the character at the left index, while substring2 includes the character at the left index but excludes the character at the right index.

The code compares substring1 with its reversed version (substring1[::-1]) and substring2 with its reversed version (substring2[::-1]) using the == operator. If either of these comparisons is true, it means that removing one character can make the string a valid palindrome. In that case, the function returns True.

If none of the above conditions are met, the left and right pointers are updated to move towards the center of the string by incrementing left and decrementing right.

If the while loop completes without finding any mismatches, it means that the string is already a palindrome. In this case, the function returns True."""
