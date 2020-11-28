from typing import List


# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
#
# Constraints:
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1.length == m + n
# nums2.length == n
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        extra_elements = len(nums1) - m
        if extra_elements > 0:
            for k in range(extra_elements):
                nums1.pop()

        i = j = 0
        while j < n:
            try:
                element = nums1[i]
            except IndexError:
                element = None

            if element is not None and element < nums2[j]:
                i = i + 1
                continue
            elif element is not None and element > nums2[j]:
                nums1.insert(i, nums2[j])
            else:
                nums1.insert(i, nums2[j])

            j = j + 1
            i = i + 1


class TestCases:
    def get(self):
        return [
            (
                {
                    'nums1': [4, 0, 0, 0, 0, 0],
                    'm': 1,
                    'nums2': [1, 2, 3, 5, 6],
                    'n': 5
                },
                [1, 2, 3, 4, 5, 6]
            ),
            (
                {
                    'nums1': [1, 2, 3, 0, 0, 0],
                    'm': 3,
                    'nums2': [2, 5, 6],
                    'n': 3
                },
                [1, 2, 2, 3, 5, 6]
            ),
        ]


if __name__ == "__main__":
    solution = Solution()

    for test_case, expected_result in TestCases().get():
        solution.merge(**test_case)
        assert all(i == j for i, j in zip(test_case['nums1'], expected_result)) is True
