class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Khởi tạo Dictionary rỗng (sổ tay)
        char_map = {}
        # vị trí index Left của chuỗi s
        left = 0
        # độ dài kỷ lục của chuỗi
        max_length = 0

        # Vòng lặp duyệt qua từng ký tự trong chuỗi s, 
        # với i là tọa độ hiện tại
        for i in range(len(s)):
            # Nếu phát hiện trùng lặp
            # Nếu ký tự s[i] đã có trong char_map
            # Và ký tự đó vẫn nằm trong giới hạn cửa sổ (>=left)
            if s[i] in char_map and char_map[s[i]] >= left:
                # Di chuyển Left lên vị trí tiếp theo
                left = char_map[s[i]] + 1

            # ghi đè tọa độ mới nhất của s[i] vào sổ tay
            char_map[s[i]] = i

            # Đo độ dài hiện tại (Cạnh phải - Cạnh trái + 1)
            current_len = i - left + 1

            # Cập nhật kỷ lục 
            # nếu cửa sổ hiện tại dài hơn kỷ lục cũ
            max_length = max(max_length, current_len)
        
        # Trả về kết quả 
        return max_length