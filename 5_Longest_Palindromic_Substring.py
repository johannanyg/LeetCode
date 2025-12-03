class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        longest = ""

        for start in range(length):
            # Only check substrings that could be longer than currently longest
            for end in range(length - 1, start + len(longest) - 1, -1):

                if self.palindrome(s, start, end):
                    substring = s[start:end + 1]

                    if len(substring) > len(longest):
                        longest = substring

        return longest

    def palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


########### Local Testing #########################
'''
def main():
    solution = Solution()

    test_strings = [
        "babad",
        "cbbd",
        "pwwkw",
        "",
        "a"
    ]

    for s in test_strings:
        result = solution.longestPalindrome(s)
        print(f"Input: '{s}'\nOutput: {result}\n")
   


if __name__ == "__main__":
    main() 

'''