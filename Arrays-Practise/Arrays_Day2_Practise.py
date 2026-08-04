def reverse_array(nums):
    left = 0
    right = len(nums) -1
    
    while left<right:
        nums[left], nums[right] = nums[right] , nums[left]
        left = left + 1
        right = right - 1
        
        
def is_palindrome(nums):
    left = 0
    right =len(nums) - 1
    while left<right:
        if nums[left]==nums[right]:
            pass
        else:
            return False
        
        left = left + 1
        right = right -1
    return True 

def pair_sum(nums, target):
    left = 0
    right = len(nums) - 1
    while left<right:
        s = nums[left] + nums[right]
        if s == target:
            return [left , right]
        elif s<target:
            left = left + 1
        else:
            right = right -1
    return [-1,-1]
            
            
        
            
def sorted_squares(nums):
    left = 0
    right = len(nums) -2
    last = (len(nums)-1) **2
    while left<right:
        nums[left]  , nums[right] = nums[right]**2, nums[left]**2
        left = left+1
        right = -1
    
     
        
def Solution(height): 
    water = 0
    left = 0
    right = len(height)-1
    while left<right:
        area = (right - left ) * min(height[left], height[right])
        if area >water:
            water= area
        if height[left]<height[right]:
            left +=1
        else:
            right -=1
    return water
        
    
    
    
         
        
        
print(sorted_squares([-4,-1,0,3,10]))    # [0, 1, 9, 16, 100]        
nums = [1,2,3,4]; reverse_array(nums); print(nums)   # [4,3,2,1]
print(is_palindrome([1,2,3,2,1]))                    # True
print(is_palindrome([1,2,3]))                        # False
print(pair_sum([1,3,5,8], 9))                        # [0, 3]
print(pair_sum([2,7,11,15], 9))                      # [0, 1]
print(Solution([1,8,6,2,5,4,8,3,7]))   # 49
print(Solution([1,1]))                  # 1
print(Solution([4,3,2,1,4]))            # 16
print(Solution([1,2,1]))                # 2
print(Solution([2,3,4,5,18,17,6]))      # 17