def twoSum(nums: list[int], target: int) -> list[int]:
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                pass
            else:
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result
    return 'No two sum solution found'


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 5], 7))
print(twoSum([3, 3], 6))
print(twoSum([3, 2, 7], 6))       

         
    