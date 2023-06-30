# Two Sum
"""
- Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
- You may assume that each input would have exactly one solution, and you may not use the same element twice.
- You can return the answer in any order.

One pass hash table
TC = O(n)
SC = O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hashmap:
                return [i, hashmap[x]]
            else:
                hashmap[nums[i]] = i

# Example usage
nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)

if result is not None:
    print("Indices of the pair:", result)
    print("Numbers in the list:", nums[result[0]], nums[result[1]])
else:
    print("No pair found that adds up to the target.")

'''
- The function twoSum takes three parameters: nums, which is the list of integers, target, which is the target value to find the pair for, and self, which indicates that it's a method of a class (but it's not utilized in this code).
- It initializes an empty dictionary called hashmap, which will be used to store the numbers encountered so far and their corresponding indices.
- The code then enters a loop that iterates through the nums list using the index i.
- Inside the loop, it calculates the difference x between the target and the current element nums[i]. This represents the other number needed to reach the target when added to the current number.
- It checks if x exists in the hashmap dictionary. If it does, it means that a previous number encountered in the list can be added to the current number to reach the target. In that case, it returns a list containing the current index i and the index stored in hashmap[x].
- If x is not found in the hashmap, it means the current number is not part of a pair that adds up to the target. Therefore, it adds the current number and its index i to the hashmap dictionary, so that it can be used for future comparisons.
- If no pair is found after iterating through the entire list, the function will implicitly return None, indicating that there is no valid pair that adds up to the target value.
'''
