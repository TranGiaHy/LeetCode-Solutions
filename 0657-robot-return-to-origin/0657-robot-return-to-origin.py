class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        # Khởi tạo 2 biến x và y là tọa độ gốc 
        x = 0 # Trục ngang
        y = 0 # Trục dọc

        # Vòng lập duyệt qua từng lệnh di chuyển (move)
        for move in moves:
            # nếu move = U 
            if move == "U":
                y += 1 # Tăng tọa độ y lên 1
            # nếu move = D
            elif move == "D":
                y -= 1 # Giảm tọa độ y xuống 1
            # nếu move = D
            elif move == "R":
                x += 1 # Tăng tọa độ x lên 1
            elif move == "L":
                x -= 1 # Giảm tọa độ x xuống 1
        
        # Robot về lại gốc tọa độ (x = 0) và (y = 0)
        return x == 0 and y == 0