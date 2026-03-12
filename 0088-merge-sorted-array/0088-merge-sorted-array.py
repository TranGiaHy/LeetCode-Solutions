class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            # Nếu giá trị tại i > giá trị tại j
            if nums1[i] > nums2[j]:
                # Đưa giá trị của mảng 1 vào vị trí thứ k
                nums1[k] = nums1[i]
                # i lùi về để xét giá trị tiếp theo của mảng 1
                i -= 1
            else:
                # Đưa giá trị của mảng 2 vào vị trí thứ k
                nums1[k] = nums2[j] 
                # j lùi về để xét giá trị tiếp theo của mảng 2
                j -= 1
            
            # Lấp xong 1 ô trống thì lùi k về để lấp ô tiếp theo
            k -= 1
        
        # Trường hợp nếu mảng 1 đã được xét hết phần tử trước
        while j >= 0:
            # Đưa nốt các phần tử còn thừa từ mảng 2 vào mảng 1
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        