class Solution:
    def twoSum(self, nums, target: int):
        hashmap = {num:nums.index(num) for num in nums}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in hashmap and i != hashmap[complement]:
                return [i, hashmap[complement]]
