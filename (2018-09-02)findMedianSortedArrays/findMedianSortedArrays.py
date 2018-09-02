
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    # ふたつのリストを連結します。
    lis = nums1 + nums2

    # 小さい順番にソートし直します。
    lis.sort()

    # 偶数個->まんなかのふたつの平均値。奇数個->まんなか。
    mid = len(lis) // 2
    if len(lis) % 2 == 0:
        _ = (lis[mid-1] + lis[mid]) / 2
    else:
        _ = lis[mid]
    return _


test_cases = [
   [ [1,3], [2] ],  # 2.0
   [ [1,2], [3,4] ],  # 2.5
]
for case in test_cases:
    print(findMedianSortedArrays(case[0], case[1]))
