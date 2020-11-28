from typing import List


# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return

        write_pointer = 0
        try:
            while nums[write_pointer] != 0:
                write_pointer = write_pointer + 1
        except IndexError:
            pass

        read_pointer = write_pointer + 1
        for read_pointer in range(read_pointer, len(nums)):
            if nums[read_pointer] == 0:
                continue

            val = nums.pop(read_pointer)
            nums.insert(write_pointer, val)
            write_pointer = write_pointer + 1


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
                    'nums': [0]
                },
                [0]
            ),
            (
                {
                    'nums': [0, 1, 0, 3, 12]
                },
                [1, 3, 12, 0, 0]
            ),
            (
                {
                    'nums': [1, 1, 0, 3, 0, 12, 0, 0, 15]
                },
                [1, 1, 3, 12, 15, 0, 0, 0, 0]
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_result in TestCases().get():
        solution.moveZeroes(**test_case)
        assert all(i == j for i, j in zip(test_case['nums'], expected_result)) is True
