"""'A car has room for capacity passengers, and is given an array trips.
 Each trip is represented by [numPassengers, from, to], which indicates that at from, it picks up numPassengers,
  then drops them off at to. Can it complete all the trips without holding more passengers than capacity at any time?
"""


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * (max(trip[2] for trip in trips) + 1)
        for (value, left, right) in trips:
            arr[left] += value
            arr[right] -= value

        curr = 0
        for i in range(len(arr)):
            curr += arr[i]
            if curr > capacity:
                return False

        return True
