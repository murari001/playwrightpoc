def solve(nums):

  n = len(nums)
    
  for i in range(n-1):
    
      isSorted = True
      
      for j in range(n-1-i):
          if nums[j] > nums[j+1]:
              nums[j], nums[j+1] = nums[j+1], nums[j]
              
              isSorted = False

      if isSorted:
          break
        
  print(*nums)

