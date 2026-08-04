def total(arrays):
    total = 0
    for n in arrays:
        total = total + n
    return total 

def biggest(arrays):
    big = 0
    for n in arrays:
        if n> big:
            big = n
    return big

def count_evens(arrays):
    even = 0
    for n in arrays:
        if n%2 == 0:
            even = even + 1
    return even 


def find(arrays, target):
    for i in range(len(arrays)):
        if arrays[i] == target:
            return i
        
    return -1

def reverse_in_place(nums):
    left = 0
    right = len(nums)-1
    while left< right:
        nums[left], nums[right] = nums[right], nums[left]
        left = left +1
        right = right -1
    
# def move_zeros(nums):
#     walk= []
#     zero = 0
#     for n in nums:
#         if n !=0:
#             walk.append(n)
#         else:
#             zero = zero + 1
    
#     for i in range(zero):
#         walk.append(0)
#     return walk 
            
def move_zeros(nums):
    write = 0
    for i in range(len(nums)):
        if nums[i] !=0:
            nums[write] = nums[i]
            write = write+1
    while write< len(nums):
        nums[write] = 0
        write +=1
        
def remove_value(nums, val):
    write = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[write] = nums[i]
            write +=1
    return write 

def remove_duplicates(nums):
    write = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[write - 1]:
            nums[write] = nums[i]
            write ==1
    return write 

            
        
          
            


# print(total([5,2,8]))              # 15
# print(biggest([5,2,8,1]))          # 8
# print(count_evens([5,2,8,1]))      # 2
# print(find([5,2,8], 8))            # 2
# nums = [1,2,3,4]; reverse_in_place(nums); print(nums)   # [4,3,2,1]
# print(move_zeros([0,1,0,3,2]))      # [1, 3, 2, 0, 0]
# nums = [3,2,3,4]; print(remove_value(nums, 3))
nums = [1,1,2,3,3]; print(remove_duplicates(nums)); print(nums[:3])   # 3 ; [1,2,3]