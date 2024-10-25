def solve(n, nums, x):
  
  for i in range(n-1):
    isSorted = True
    for j in range(n-1-i):
      
      a = abs(nums[j]-x)
      b = abs(nums[j+1]-x)
      
      if a > b:
        nums[j], nums[j+1] = nums[j+1], nums[j]
        isSorted = False
    
    if isSorted:
      print(*nums)
      return
  
