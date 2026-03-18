class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Khởi tạo kho chứa để đếm số lượng
        # defaultdict(int) tự động gán số lượng = 0 cho các chữ cái mới.
        char_count = collections.defaultdict(int)

        # Nhập kho:
        # Quét qua cuốn tạp chí, gặp chữ nào thì cộng số lượng chữ đó lên 1.
        for char in magazine:
            # ví dụ magazine = "aab" -> kho sẽ có {'a': 2, 'b': 1}
            char_count[char] += 1
        
        # Xuất kho:
        # Quét qua từng chữ cái cần có trong bức thư    
        for char in ransomNote:
            # Nếu chữ này chưa từng có mặt trong kho hoặc đã bị xài hết (số lượng = 0)
            if char not in char_count or char_count[char] == 0:
                # Trả về False ( Báo lỗi vì không từ )
                return False
            # Lấy 1 chữ ra xài thì phải trừ số lượng trong kho đi 1
            char_count[char] -= 1
            
        # Trả về nếu không bị False    
        return True