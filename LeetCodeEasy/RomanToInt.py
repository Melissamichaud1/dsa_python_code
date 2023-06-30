# Roman to Integer
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""
# TC = O(1)
# SC = O(1)

values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in values:
               total += values[s[i:i+2]]
               i += 2
            else:
                total += values[s[i]]
                i += 1
        return total

solution = Solution()
print(solution.romanToInt("MMCMLXXXIX"))

"""
The code begins by creating a dictionary called values that maps Roman numerals to their corresponding integer values. For example, "I" maps to 1, "V" maps to 5, and so on. Additionally, it includes special cases where two-character Roman numerals represent values that are not simply additive combinations of their individual characters (e.g., "IV" represents 4).

The romanToInt method takes a string s as input, which is the Roman numeral to be converted. It initializes a variable total to 0, which will store the resulting integer value. It also initializes a variable i to 0, which represents the current index in the input string.

The code then enters a while loop that iterates as long as i is less than the length of the input string. This loop is used to process each character or pair of characters in the Roman numeral.

Inside the loop, the code checks if the current character and the next character (if it exists) form a valid two-character Roman numeral. This is done by checking if s[i:i+2] is present as a key in the values dictionary. If it is, it means that the two-character Roman numeral exists, and its corresponding value should be added to the total. The total is updated accordingly, and i is incremented by 2 to skip the processed characters.

If the current character and the next character do not form a valid two-character Roman numeral, the code adds the value of the current character alone to the total and increments i by 1 to move to the next character.

After processing all characters in the input string, the total represents the integer value of the Roman numeral, and it is returned as the result of the romanToInt method.

Finally, an instance of the Solution class is created, and the romanToInt method is called with the input string "MMCMLXXXIX". The resulting integer value is printed to the console.
"""
