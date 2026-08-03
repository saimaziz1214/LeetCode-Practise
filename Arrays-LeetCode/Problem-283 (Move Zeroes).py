# ---- test harness (just to run this locally) ----
# not part of the solution — LeetCode provides its own.

# ---- #283 Move Zeroes ----
# move all the 0s to the end but keep the order of the non-zeros, and do it IN
# PLACE (no new array). two phases with the write pointer:
# phase 1 — walk through, and every time I hit a non-zero, write it at the front
#   (at write) and bump write. this packs all the non-zeros to the front in order.
# phase 2 — after that, write is sitting right after the last non-zero, so
#   everything from write to the end is leftover junk. I just fill all of those
#   slots with 0.
# my first instinct was to build a new list and count zeros — that works but uses
# O(n) extra space. the write-pointer way does it in place with O(1) extra.

class Solution(object):
    def moveZeroes(self, nums):
        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:            # phase 1: pack non-zeros to the front
                nums[write] = nums[i]
                write += 1
        while write < len(nums):        # phase 2: fill the rest with zeros
            nums[write] = 0
            write += 1

# ---- run LeetCode's test cases ----
sol = Solution()
nums = [0,1,0,3,12]
sol.moveZeroes(nums); print(nums)                        # [1, 3, 12, 0, 0]
nums = [0]
sol.moveZeroes(nums); print(nums)                        # [0]