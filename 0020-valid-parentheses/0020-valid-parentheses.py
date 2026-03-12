class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Khởi tạo một stack rỗng
        stack = []

        # { "key": "value" }. Hãy dùng ngoặc ĐÓNG làm key, ngoặc MỞ làm value.
        mapping = {")":"(", "]":"[", "}":"{"}

        # Duyệt qua từng ký tự 'char' trong chuỗi 's'
        for char in s:
            #TH1
            if char in mapping :

                top_element = stack.pop() if stack else "#"

                if mapping[char] != top_element:

                    return False # Game Over, trả về True hay False?
            #TH2
            else:
                # Nhét 'char' vào đỉnh stack
                stack.append(char)

        return len(stack) == 0
