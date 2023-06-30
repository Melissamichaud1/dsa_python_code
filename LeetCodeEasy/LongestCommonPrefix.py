"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
# TC = O(n*m)
# SC = O(1)
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Horizontal scan
        if len(strs) == 0:
            return ""
        # First item = prefix
        prefix = strs[0]
        # Loop through all list items
        for i in range(len(strs)):
            # Remove the last prefix letter until both words have
            # the same beginning (prefix)
            while strs[i].find(prefix) != 0:
                # Remove the last letter
                prefix = prefix[:-1]
                # If we removed every letter = no common prefix
                if len(prefix) == 0:
                    return ""
        return prefix

solution = Solution()
print(solution.longestCommonPrefix(["hello", "help", "hellmans"]))

"""
The code first checks if the length of strs is 0. If it is, it means there are no strings in the array, and the function returns an empty string.

If strs is not empty, we initialize the prefix variable with the first string in the array (strs[0]).

Then, we iterate over the remaining strings in the array starting from the second string (index 1) using a for loop.

Inside the loop, we use a while loop to find the longest common prefix between the current string (strs[i]) and the prefix string. The while loop continues until the prefix is found at the beginning of the current string (strs[i].find(prefix) == 0).

If the prefix is not found at the beginning of the current string, we remove the last character from the prefix using slicing (prefix = prefix[:-1]). If the prefix becomes empty, it means there are no common prefixes among the strings, and the function returns an empty string.

After iterating through all the strings and finding the longest common prefix, the function returns the resulting prefix.
"""
