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
def fn(arr, k):
    curr = 0
    ans = curr
    for i in range(len(arr)):
        if i >= k:
            curr *= arr[i]
            arr[i - k] -= 1


#  Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        best = now = sum(nums[:k])
        for i in range(k, len(nums)):
            now += nums[i] - nums[i - k]
            if now > best:
                best = now
        return best / k


def build_string(s):
    arr = []
    for c in s:
        arr.append(c)

    return "".join(arr)


