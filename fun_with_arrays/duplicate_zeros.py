from typing import List


# Given a fixed length array arr of integers, duplicate each occurrence of zero,
# shifting the remaining elements to the right.
#
# Note that elements beyond the length of the original array are not written.
#
# Do the above modifications to the input array in place, do not return anything from your function.
#
# Note:
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        inserted_zero_index = None
        for i in range(len(arr)):
            if arr[i] == 0 and (inserted_zero_index is None or inserted_zero_index != i):
                arr.insert(i + 1, 0)
                arr.pop()
                inserted_zero_index = i + 1


class TestCases:
    def get(self):
        return [
            (
                [1, 0, 2, 3, 0, 4, 5, 0],
                [1, 0, 0, 2, 3, 0, 0, 4]
            ),
            (
                [0, 1, 0, 2, 0],
                [0, 0, 1, 0, 0]
            ),
            (
                [0, 0],
                [0, 0]
            ),
            (
                [1, 0],
                [1, 0]
            ),
            (
                [1, 2, 3],
                [1, 2, 3]
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_result in TestCases().get():
        solution.duplicateZeros(arr=test_case)
        assert all(i == j for i, j in zip(test_case, expected_result)) is True
