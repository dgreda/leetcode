from typing import List


# Given a sorted array nums, remove the duplicates in-place such that each element appears only once
# and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place
# with O(1) extra memory.
#
# Constraints:
# 0 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums is sorted in ascending order
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = len(nums) - 1
        while i > 0:
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            i = i - 1

        return len(nums)


class TestCases:
    def get(self):
        return [
            (
                {
                    'nums': [1, 1, 2],
                },
                2,
                [1, 2]
            ),
            (
                {
                    'nums': [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
                },
                5,
                [0, 1, 2, 3, 4]
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_return, expected_result in TestCases().get():
        ret = solution.removeDuplicates(**test_case)
        assert ret == expected_return
        assert all(i == j for i, j in zip(test_case['nums'], expected_result)) is True
