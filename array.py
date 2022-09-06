def ArrayAddtion(nums):
    n = len(nums)
    result = [nums[0]]

    for i in range(1, n):
        nums[i] += nums[i - 1]
        result.append(nums[i])

    return result


ot = [45, 34, 32, 12, 34]
print(ArrayAddtion(ot))
