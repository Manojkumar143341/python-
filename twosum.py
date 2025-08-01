def twosum(nums,target):
    new_map ={}
    for i ,num in enumerate(nums):
        diff = target - num
        if diff in new_map:
            return [num_map[diff],i]
        num_map[num]=i
nums =[1,2,3,4,5]
target=3
print(twosum(nums,target))