from typing import List


# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime?
# You may assume the returned list does not count as extra space.
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        set_num = set(nums)

        for i in range(1, len(nums) + 1, 1):
            if i not in set_num:
                result.append(i)

        return result


class TestCases:
    def get(self):
        return [
            (
                {
                    'nums': []
                },
                []
            ),
            (
                {
                    'nums': [1]
                },
                [1]
            ),
            (
                {
                    'nums': [4, 3, 2, 7, 8, 2, 3, 1]

                },
                [5, 6]
            ),
            (
                {
                    'nums': [2, 4, 3, 1, 5]
                },
                []
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_result in TestCases().get():
        ret = solution.findDisappearedNumbers(**test_case)
        assert all(i == j for i, j in zip(ret, expected_result)) is True
