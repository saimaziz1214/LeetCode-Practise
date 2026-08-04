# ---- #977 Squares of a Sorted Array ----
# the array is sorted but has negatives, so squaring scrambles the order (a big
# negative like -4 squares to 16, which is bigger than nearby positives).
# my first thought was just square everything and sort -> works, but that's
# O(n log n). the two-pointer way is O(n):
# the biggest square is ALWAYS at one of the two ends (most-negative on the left
# or most-positive on the right). so I compare the ends, take the bigger square,
# and place it at the BACK of a new array — filling largest-to-smallest, back to
# front. that comes out sorted ascending automatically.
# note: while left <= right (not <) so I don't miss the final middle element.

class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        new = [0] * n
        left = 0
        right = n - 1
        write = n - 1                       # fill from the BACK (largest first)
        while left <= right:
            sq_left = nums[left] ** 2
            sq_right = nums[right] ** 2
            if sq_left > sq_right:
                new[write] = sq_left
                left += 1
            else:
                new[write] = sq_right
                right -= 1
            write -= 1
        return new

# ---- run LeetCode's test cases ----
sol = Solution()
print(sol.sortedSquares([-4,-1,0,3,10]))    # [0, 1, 9, 16, 100]
print(sol.sortedSquares([-7,-3,2,3,11]))    # [4, 9, 9, 49, 121]