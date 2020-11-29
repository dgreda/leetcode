import collections
from typing import List


# Given an array of integers A sorted in non-decreasing order,
# return an array of the squares of each number, also in sorted non-decreasing order.
#
# Note:
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        answer = collections.deque()
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1

        return list(answer)


class TestCases:
    def get(self):
        return [
            (
                {
                    'A': []
                },
                []
            ),
            (
                {
                    'A': [1]
                },
                [1]
            ),
            (
                {
                    'A': [0]
                },
                [0]
            ),
            (
                {
                    'A': [-4, -1, 0, 3, 10]
                },
                [0, 1, 9, 16, 100]
            ),
            (
                {
                    'A': [-7, -3, 2, 3, 11]
                },
                [4, 9, 9, 49, 121]
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_result in TestCases().get():
        ret = solution.sortedSquares(**test_case)
        assert all(i == j for i, j in zip(ret, expected_result)) is True
