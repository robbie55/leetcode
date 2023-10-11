def twoSum(nums, target):
  hashmap = {}

  for i in range(len(nums)):
    complement = target - nums[i] 

    if complement in hashmap.keys():
      if i > hashmap[complement]:
        return [hashmap[complement], i]
      return [i, hashmap[complement]]
    hashmap[nums[i]] = i


print(twoSum([3,2,4], 6))