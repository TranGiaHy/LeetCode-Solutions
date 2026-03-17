class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Lấy "cửa sổ" đầu tiên từ đầu mảng đến vị trí k-1
        # k = 4 -> lấy nums[0] đến nums[3] là [1, 12, -5, -6]
        # sau đó tính tổng khởi điểm: 1 + 12 - 5 - 6 = 2
        current_sum = sum(nums[:k])

        # Ghi nhận tổng lớn nhất tạm thời max_sum = 2
        max_sum = current_sum

        # Cho "cửa sổ" trượt từ vị trí số 4 đến hết mảng
        for i in range(k, len(nums)):
            # Cập nhật current_sum mới:
            # Current_sum = 2
            # nums[4] -> 50 (giá trị tại chỉ số i = 4)
            # nums[4-4]->nums[0] = 1 (giá trị tại chỉ số i = 0)
            # Tổng mới = 2 (tổng cũ) + 50 (mới) - 1 (cũ) = 51
            current_sum = current_sum + nums[i] - nums[i - k]
            # So sánh lấy tổng lớn nhất (2 < 51) chọn 51
            # Lúc này max_sum = 51
            max_sum = max(max_sum, current_sum)
        
        # Trượt hết mảng, max_sum / k để ra trung bình
        return float(max_sum) / k