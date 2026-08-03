# ---- test harness (just to run this locally) ----
# not part of the solution — LeetCode provides its own. this just lets me
# run my function and check the result on my own machine.

# ---- #26 Remove Duplicates from Sorted Array ----
# the array is SORTED, so any duplicates sit right next to each other. I use
# the write-pointer trick: one index (i) reads through everything, another
# (write) marks where the next unique element goes.
# the first element is always a keeper (nothing before it to be a dupe of), so
# write starts at 1 and i starts reading from 1.
# for each element I compare it to the LAST one I kept (nums[write-1]). if it's
# different, it's a new value -> write it and bump write. if it's the same, it's
# a duplicate -> skip. return write at the end = the count of unique elements.
# (the leftover junk past write doesn't matter — the judge only checks the first
# write elements.)
# note to self: it's write += 1, NOT write =+ 1 — that typo cost me a submission.

class Solution(object):
    def removeDuplicates(self, nums):
        write = 1                          # first element always kept
        for i in range(1, len(nums)):
            if nums[i] != nums[write-1]:   # different from last kept?
                nums[write] = nums[i]      # keep it
                write += 1
        return write                       # count of unique elements

# ---- run LeetCode's test cases ----
sol = Solution()
nums = [1,1,2]
print(sol.removeDuplicates(nums), nums[:2])              # 2 [1, 2]
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums), nums[:5])              # 5 [0, 1, 2, 3, 4]