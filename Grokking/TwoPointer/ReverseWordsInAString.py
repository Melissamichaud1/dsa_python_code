"""
Given a sentence, reverse the order of its words without affecting the order of letters within a given word.

"""
# TC = O(n)
# SC = O(n)
import re
def reverse_words(sentence):
   # remove leading, trailing and multiple spaces
   sentence = re.sub(' +',' ',sentence.strip())
   # We need to convert the updated string
   # to lists of characters as strings are immutable in Python
   sentence = list(sentence)
   # Stores the length of the sentence string
   str_len = len(sentence)

   #  We will first reverse the entire string.
   str_rev(sentence, 0, str_len - 1)
   #  Now all the words are in the desired location, but
   #  in reverse order: "Hello World" -> "dlroW olleH".

   start = 0
   end = 0

   # Now, let's iterate the reversed string and reverse each word in place.
   # "dlroW olleH" -> "World Hello"

   while (start < str_len):
      # Find the end index of the word.
    while end < str_len and sentence[end] != ' ':
        end += 1
     # Let's call our helper function to reverse the word in-place.
    str_rev(sentence, start, end - 1)
    start = end + 1
    end += 1

   return ''.join(sentence)


# A function that reverses a whole sentence character by character
def str_rev(_str, start_rev, end_rev):
   # Starting from the two ends of the list, and moving
   # in towards the centre of the string, swap the characters
   while start_rev < end_rev:
       temp = _str[start_rev]          # temp store for swapping
       _str[start_rev] = _str[end_rev]  # swap step 1
       _str[end_rev] = temp            # swap step 2


       start_rev += 1                  # Move forwards towards the middle
       end_rev -= 1                    # Move backwards towards the middle

"""
The code starts by importing the re module, which is used for regular expression operations.

The reverse_words function is defined, which takes a sentence parameter.

The first step inside the reverse_words function is to remove leading, trailing, and multiple spaces from the sentence using the re.sub function. It replaces multiple spaces with a single space using the regular expression ' +'.

The sentence is then converted to a list of characters because strings in Python are immutable, meaning they cannot be modified in place.

The length of the sentence string is stored in the str_len variable.

The code calls the str_rev function to reverse the entire string sentence using the str_rev(sentence, 0, str_len - 1) line. This function reverses the characters of the string in-place.

After reversing the entire string, the code initializes start and end variables to keep track of the start and end indices of each word in the reversed string.

The code enters a while loop that iterates through the reversed string. It finds the end index of the current word by moving end until it encounters a space character.

Once the end index of the word is found, the code calls the str_rev function again to reverse the characters of the word in-place using the str_rev(sentence, start, end - 1) line.

The start and end variables are updated to point to the start and end indices of the next word in the reversed string.

The while loop continues until all words in the reversed string are reversed.

Finally, the function returns the reversed sentence by joining the characters in the sentence list using the ''.join(sentence) line.

The str_rev function is a helper function that takes a string _str, a start index start_rev, and an end index end_rev. It reverses the characters of the string in-place by swapping characters from the start and end indices and moving towards the center of the string."""
