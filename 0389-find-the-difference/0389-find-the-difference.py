class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # Khởi tạo 2 biến để tính tổng điểm
        sum_s = 0
        sum_t = 0

        # Vòng lặp for duyệt qua chuỗi s để cộng dồn điểm
        for char in s:
            # Dùng hàm ord() để chuyển char thành số và cộng vào sum_s
            sum_s += ord(char)

        # Vòng lặp for duyệt qua chuỗi t để cộng dồn điểm
        for char in t:
            # Dùng hàm ord() để cộng vào sum_t
            sum_t += ord(char)

        # Tính kqa mã số của chữ cái dư ra
        diff = sum_t - sum_s

        # Chuyển con số diff ngược lại thành chữ cái
        return chr(diff)

        