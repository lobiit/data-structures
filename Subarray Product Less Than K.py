from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1

        return ans


# fixed window size
def find_best_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)

    return ans

