# ---- #11 Container With Most Water ----
# each number is a wall height; the water between two walls = width * height of
# the SHORTER wall (water spills over the short side). width = distance between
# their indices (right - left). I want the max over all pairs.
# brute force checks every pair = O(n^2). two pointers does it in O(n):
# start at the widest span (left=0, right=end), track a running max, then move
# the pointer at the SHORTER wall inward. why the shorter one? because the short
# wall caps the water, and moving inward only shrinks the width — so keeping the
# short wall can never do better. the only move with any upside is discarding the
# shorter wall and hoping for a taller one. so every pair I skip is provably worse.
# note: can't sort here — width depends on the ORIGINAL positions.

class Solution(object):
    def maxArea(self, height):
        water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > water:
                water = area
            if height[left] < height[right]:   # move the SHORTER wall inward
                left += 1
            else:
                right -= 1
        return water

# ---- run LeetCode's test cases ----
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))   # 49
print(sol.maxArea([1,1]))                  # 1
print(sol.maxArea([4,3,2,1,4]))            # 16