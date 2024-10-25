def solve(n, nums):
  
  freq = {}
  for num in nums:
    if num in freq:
      freq[num] += 1
    else:
      freq[num] = 1
      
  nums = sorted(nums, key=lambda x: (freq[x], nums.index(x)))
      
  print(*nums)
      
    
