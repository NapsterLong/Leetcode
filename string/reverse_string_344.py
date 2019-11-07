from typing import List

'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        index = 0
        while index < int(len(s) / 2):
            s[index], s[-1 - index] = s[-1 - index], s[index]
            index += 1

if __name__ == '__main__':
    s = Solution()
    chars = ["H", "a", "n", "n", "a", "h"]
    s.reverseString(chars)
    print(chars)