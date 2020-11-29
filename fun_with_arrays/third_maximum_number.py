from typing import List


# Given a non-empty array of integers, return the third maximum number in this array.
# If it does not exist, return the maximum number. The time complexity must be in O(n).
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            d[i] = True
        l = sorted(d.keys(), reverse=True)
        if len(l) >= 3:
            return l[2]
        else:
            return l[0]


class TestCases:
    def get(self):
        return [
            (
                {
                    'nums': [1]
                },
                1
            ),
            (
                {
                    'nums': [0]
                },
                0
            ),
            (
                {
                    'nums': [3, 2, 1]
                },
                1
            ),
            (
                {
                    'nums': [1, 2]
                },
                2
            ),
            (
                {
                    'nums': [2, 2, 3, 1]
                },
                1
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_result in TestCases().get():
        ret = solution.thirdMax(**test_case)
        assert ret == expected_result
