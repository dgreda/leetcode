from typing import List


# Students are asked to stand in non-decreasing order of heights for an annual photo.
# Return the minimum number of students that must move in order for all students to be standing
# in non-decreasing order of height.
#
# Notice that when a group of students is selected they can reorder in any possible way
# between themselves and the non selected students remain on their seats.
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(a != b for a, b in zip(heights, sorted(heights)))


class TestCases:
    def get(self):
        return [
            (
                {
                    'heights': [1]
                },
                0
            ),
            (
                {
                    'heights': [0]
                },
                0
            ),
            (
                {
                    'heights': [3, 2, 1]
                },
                2
            ),
            (
                {
                    'heights': [1, 1, 4, 2, 1, 3]
                },
                3
            ),
            (
                {
                    'heights': [5, 1, 2, 3, 4]
                },
                5
            ),
            (
                {
                    'heights': [1, 2, 3, 4, 5]
                },
                0
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_result in TestCases().get():
        ret = solution.heightChecker(**test_case)
        assert ret == expected_result
