'''
    In this problem we have to merge two sorted array. For example, given nums1 = [1,2,3,0,0,0] and nums2 = [2,5,6], you should return nums1 = [1,2,2,3,5,6].
    Time complexity: O(m+n)
    Space complexity: O(1)

    For solving this question we follow the following steps:
    1) First we have to initialize i = m - 1 and j = n - 1 and k = m + n - 1
    2) If nums1 is empty, copy elements from nums2 to nums1 starting at index 0.
    3) While i >= 0 and j >= 0, if nums1[i] > nums2[j], then we copy nums1[i] to nums1[k] and decrement i. Otherwise, we copy nums2[j] to nums1[k] and decrement j.
    4) Finally, we copy the remaining elements of nums2 to nums1 if there are any.

'''

def mergeSortedArray(nums1, nums2, m, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    if m == 0:
        # If nums1 is empty, copy elements from nums2 to nums1
        for idx in range(n):
            nums1[idx] = nums2[idx]
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are remaining elements in nums2, copy them to nums1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1



if __name__ == "__main__":
    nums1 = []
    m = 0
    nums2 = [1,2,3]
    n = 3
    mergeSortedArray(nums1, nums2, m, n)
    print(nums1)