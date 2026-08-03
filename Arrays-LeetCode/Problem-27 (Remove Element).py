# ---- test harness (just to run this locally) ----
# not part of the solution — LeetCode provides its own.

# ---- #27 Remove Element ----
# remove every copy of val from the array, in place, and return the new length.
# same write-pointer idea: i reads everything, write marks where the next keeper
# goes. the "keep?" rule here is simple — keep anything that ISN'T val.
# every time nums[i] != val, I write it at write and bump write. vals just get
# skipped (never written), so they get overwritten. at the end write = how many
# I kept = the new length.
# no second loop and no cleanup needed — the judge only looks at the first write
# elements, so leftover junk in the back is ignored.

class Solution(object):
    def removeElement(self, nums, val):
        write = 0
        for i in range(len(nums)):
            if nums[i] != val:          # keep everything that isn't val
                nums[write] = nums[i]
                write += 1
        return write                    # new length

# ---- run LeetCode's test cases ----
sol = Solution()
nums = [3,2,2,3]
print(sol.removeElement(nums, 3), nums[:2])              # 2 [2, 2]
nums = [0,1,2,2,3,0,4,2]
print(sol.removeElement(nums, 2), nums[:5])              # 5 [0, 1, 3, 0, 4]