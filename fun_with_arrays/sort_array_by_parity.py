from typing import List


# Given an array A of non-negative integers, return an array consisting of all the even elements of A,
# followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.
#
# Note:
# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) == 0:
            return

        write_pointer = 0
        try:
            while A[write_pointer] % 2 == 0:
                write_pointer = write_pointer + 1
        except IndexError:
            pass

        read_pointer = write_pointer + 1
        for read_pointer in range(read_pointer, len(A)):
            if A[read_pointer] % 2 != 0:
                continue

            val = A.pop(read_pointer)
            A.insert(write_pointer, val)
            write_pointer = write_pointer + 1

        return A


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
                    'A': [3, 1, 2, 4]
                },
                [2, 4, 3, 1]
            ),
            (
                {
                    'A': [2, 4, 3, 1]
                },
                [2, 4, 3, 1]
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_result in TestCases().get():
        solution.sortArrayByParity(**test_case)
        assert all(i == j for i, j in zip(test_case['A'], expected_result)) is True
