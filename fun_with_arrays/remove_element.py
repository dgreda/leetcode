from typing import List


# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place
# with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Constraints:
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val > 50:
            return len(nums)

        for v in reversed(nums):
            if v == val:
                nums.remove(v)

        return len(nums)


class TestCases:
    def get(self):
        return [
            (
                {
                    'nums': [0, 1, 2, 2, 3, 0, 4, 2],
                    'val': 2,
                },
                5,
                [0, 1, 3, 0, 4]
            ),
            (
                {
                    'nums': [3, 2, 2, 3],
                    'val': 3,
                },
                2,
                [2, 2]
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_return, expected_result in TestCases().get():
        ret = solution.removeElement(**test_case)
        assert ret == expected_return
        assert all(i == j for i, j in zip(test_case['nums'], expected_result)) is True
