from typing import List


# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.
# After doing so, return the array.
#
# Constraints:
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^5
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = None
        for i in range(len(arr) - 1, -1, -1):
            val = arr[i]

            if i == len(arr) - 1:
                arr[i] = -1
            else:
                arr[i] = max

            if max is None or max < val:
                max = val

        return arr


class TestCases:
    def get(self):
        return [
            (
                {
                    'arr': [17, 18, 5, 4, 6, 1]
                },
                [18, 6, 6, 6, 1, -1]
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_return in TestCases().get():
        ret = solution.replaceElements(**test_case)
        assert all(i == j for i, j in zip(ret, expected_return)) is True
