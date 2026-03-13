class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # Số kẹo lớn nhất hiện có trong danh sách ( Kẹo của trẻ có nhiều nhất )
        max_candy = max(candies)

        # Tạo danh sách rỗng
        result = []
        
        # Duyệt qua từng đứa trẻ (candy đại diện cho số kẹo của 1 đứa)
        for candy in candies:
            # ktra Nếu số kẹo hiện tại + số kẹo thêm >= Kẹo của trẻ có nhiều nhất
            # Thêm True vào ds nếu >= Kẹo của trẻ có nhiều nhất
            # Thêm False vào ds nếu <= Kẹo của trẻ có nhiều nhất
            result.append(candy + extraCandies >= max_candy)

        # trả về kqua
        return result