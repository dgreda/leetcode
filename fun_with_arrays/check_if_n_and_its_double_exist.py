from typing import List


# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M
# (i.e. N = 2 * M).
#
# More formally check if there exists two indices i and j such that:
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
#
# Constraints:
# 2 <= arr.length <= 500
# -10^3 <= arr[i] <= 10^3
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                    return True

        return False


class TestCases:
    def get(self):
        return [
            (
                {
                    'arr': [10, 2, 5, 3]
                },
                True
            ),
            (
                {
                    'arr': [7, 1, 14, 11]
                },
                True
            ),
            (
                {
                    'arr': [14, 1, 7, 11]
                },
                True
            ),
            (
                {
                    'arr': [3, 1, 7, 11]
                },
                False
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_return in TestCases().get():
        ret = solution.checkIfExist(**test_case)
        assert ret == expected_return
