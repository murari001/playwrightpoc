def selection_sort(nums, k):
  for i in range(k):
    min_indx = i
    for j in range(i+1,len(nums)):
      if nums[j] < nums[min_indx]:
        min_indx = j
    nums[i], nums[min_indx] = nums[min_indx], nums[i]

def insertion_sort(nums, start):
  for i in range(start, len(nums)):
    key = nums[i]
    j = i-1

    while j>=start and key < nums[j]:
      nums[j+1] = nums[j]
      j -= 1

    nums[j+1] = key

def solve(nums):
  n = len(nums)
  min_comparisons = float('inf')
  best_k = 0
  for k in range(1,n):
    comparisons = k * (n-k) + n * (n-1) //2 
    if comparisons < min_comparisons:
      best_k = k

  selection_sort(nums,best_k)
  insertion_sort(nums,best_k)
  
  print(*nums)
  
  
