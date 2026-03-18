import os

def generate_table():
    # 1. Tìm tất cả các thư mục có tên bắt đầu bằng số (ví dụ: 0383-ransom-note)
    folders = [f for f in os.listdir('.') if os.path.isdir(f) and f[0].isdigit()]
    folders.sort() # Sắp xếp theo thứ tự bài từ nhỏ đến lớn
    
    # 2. Tạo phần đầu của cái Bảng
    table = "| # | Bài toán | Lời giải | Độ khó | Time | Space | Topic Tags |\n"
    table += "|---|---|---|---|---|---|---|\n"
    
    # 3. Quét từng thư mục để tạo các hàng (rows)
    for folder in folders:
        parts = folder.split('-')
        num = parts[0] # Lấy số thứ tự (vd: 0383)
        
        # Biến "ransom-note" thành "Ransom Note"
        name_parts = parts[1:]
        name = " ".join(name_parts).title() 
        
        # Tạo link trỏ tới LeetCode
        leetcode_link = f"https://leetcode.com/problems/{'-'.join(name_parts)}/"
        
        # Tạo link trỏ tới thư mục code trên GitHub của bạn
        solution_link = f"[Python](./{folder})"
        
        # Lưu ý: Các cột Độ khó, Time, Space, Topic tạo sẵn placeholder để bạn tự điền tay sau, 
        # vì việc dùng bot đọc độ phức tạp từ code là cực kỳ phức tạp.
        table += f"| {num} | [{name}]({leetcode_link}) | {solution_link} | 🔄 | `O(?)` | `O(?)` | 🏷️ |\n"
    
    return table

def update_readme():
    # Đọc nội dung file README hiện tại
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_marker = ""
    end_marker = ""
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    # Nếu tìm thấy 2 cái cọc mốc, tiến hành cắt ghép và ghi đè nội dung mới vào giữa
    if start_idx != -1 and end_idx != -1:
        new_content = (
            content[:start_idx + len(start_marker)] 
            + "\n" 
            + generate_table() 
            + content[end_idx:]
        )
        
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Đã cập nhật README thành công!")

if __name__ == "__main__":
    update_readme()
