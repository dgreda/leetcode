from typing import List


# Given an array of integers arr, return true if and only if it is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
#   arr[0] < arr[1] < ... < arr[i - 1] < A[i]
#   arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        top_index = None
        i = 0
        while i <= len(arr) - 2:
            if arr[i] == arr[i + 1]:
                return False

            if top_index is None and arr[i] > arr[i + 1]:
                if i == 0:
                    return False

                top_index = i
                i = i + 1
                continue

            if top_index is None and arr[i] > arr[i + 1] or top_index is not None and arr[i] < arr[i + 1]:
                return False

            i = i + 1

        if top_index is not None:
            return True

        return False


class TestCases:
    def get(self):
        return [
            (
                {
                    'arr': [2, 1]
                },
                False
            ),
            (
                {
                    'arr': [3, 5, 5]
                },
                False
            ),
            (
                {
                    'arr': [3, 5, 4]
                },
                True
            ),
            (
                {
                    'arr': [0, 3, 2, 1]
                },
                True
            ),
            (
                {
                    'arr': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                },
                False
            ),
            (
                {
                    'arr': [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
                },
                False
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_return in TestCases().get():
        ret = solution.validMountainArray(**test_case)
        assert ret == expected_return
