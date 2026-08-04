# ---- #125 Valid Palindrome ----
# same two-pointer palindrome idea as a plain array (compare ends, move inward,
# bail if they ever differ) BUT with two twists this problem adds:
#   1. ignore anything that isn't a letter/number (spaces, punctuation)
#   2. ignore case ('A' == 'a')
# so before comparing, I skip non-alphanumeric chars on each side with inner
# while loops (using .isalnum()), then compare lowercased (.lower()).
# if left and right ever mismatch -> not a palindrome. if I get through the whole
# thing -> it is one. (early return False on failure, return True at the end.)

class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():    # skip junk on left
                left += 1
            while left < right and not s[right].isalnum():   # skip junk on right
                right -= 1
            if s[left].lower() != s[right].lower():          # compare, ignore case
                return False
            left += 1
            right -= 1
        return True

# ---- run LeetCode's test cases ----
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))   # True
print(sol.isPalindrome("race a car"))                        # False
print(sol.isPalindrome(" "))                                 # True