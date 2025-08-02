nums = [1,2,2,3,3,3,4,5]
def fing_max(nums):
     return max(nums)

longest = 0
current = 0

for num in nums:
   if num == max_values:
    current += 1
    longest = max(longest,current)
   else:
     current = 0
print(longest)
