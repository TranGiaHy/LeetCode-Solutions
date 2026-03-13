class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        # mapping = {"key":"value"}
        mapping = {")":"(", "]":"[", "}":"{"}

        # Vòng lặp lấy từng ký tự char trong chuỗi s
        for char in s:
            # Trường hợp : nếu là ngoặc đóng
            # ktra nếu ký tự char của chuỗi s có trong mapping có phải là key hay ko
            if char in mapping:
            
                # Lấy ngoặc mở trên đỉnh stack ra để kiểm tra (gán vào top_element)
                # Nếu trong stack rỗng thì trả về kí tự "#"
                top_element = stack.pop() if stack else "#"

                # ktra (top_element) khác ký tự char trong mapping trả về false
                if mapping[char] != top_element:
                    return False

            # Trường hợp : nếu là ngoặc mở thì nhét ký tự vào stack
            else:
                stack.append(char)

        return len(stack) == 0
