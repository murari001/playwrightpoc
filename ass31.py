def solve(n, nums):
  
  for i in range(n-1):
    isSorted = True
    for j in range(n-1-i):
      
      if nums[j] > nums[j+1] and nums[j] > 0:
        nums[j], nums[j+1] = nums[j+1], nums[j]
        isSorted = False
        
    if isSorted:
      break
        
  count = 0
  for num in nums:
    if num < 1:
      count += 1
      
  nums = nums[count:] + nums[:count]
    
  print(*nums)

  
