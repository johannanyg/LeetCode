class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_list = []
        new_word= ""
        for x in s:
            if x in new_word:

                new_list.append(new_word)
                new_word = new_word[new_word.index(x)+1:] + x
            else:
                new_word += x
        
        if new_word:
            new_list.append(new_word)

        return len(max(new_list, key=len)) if new_list else 0



########### local run ########################'
'''
def main():
    solution = Solution()  # create an instance

    # Test cases
    test_strings = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
        "a"
    ]

    for s in test_strings:
        result = solution.lengthOfLongestSubstring(s)
        print(f"Input:'{s}' \nOutput: {result}")


if __name__ == "__main__":
    main()
'''