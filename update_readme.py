import os

def get_difficulty(folder_name):
    """Mở file README.md bên trong từng thư mục bài tập để tìm độ khó"""
    readme_path = os.path.join(folder_name, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Quét 500 ký tự đầu tiên để tìm keyword độ khó
            if "Easy" in content[:500]: return "🟢 Easy"
            if "Medium" in content[:500]: return "🟡 Medium"
            if "Hard" in content[:500]: return "🔴 Hard"
    return "❓ Unknown"

def update_readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. TRÍCH XUẤT (EXTRACT): Lưu lại các Time/Space/Tags cũ đã nhập tay
    old_data = {}
    for line in content.split('\n'):
        if line.startswith('| ') and len(line.split('|')) >= 7:
            cols = [c.strip() for c in line.split('|')]
            if cols[1].isdigit(): # Nếu cột 1 là số ID
                old_data[cols[1]] = {'time': cols[5], 'space': cols[6], 'tags': cols[7]}

    # 2. BIẾN ĐỔI & PHÂN LOẠI (TRANSFORM)
    folders = [f for f in os.listdir('.') if os.path.isdir(f) and f[0].isdigit()]
    
    easy, medium, hard, unknown = [], [], [], []
    for folder in folders:
        diff = get_difficulty(folder)
        if "Easy" in diff: easy.append((folder, diff))
        elif "Medium" in diff: medium.append((folder, diff))
        elif "Hard" in diff: hard.append((folder, diff))
        else: unknown.append((folder, diff))

    # Sắp xếp từng nhóm theo ID từ nhỏ đến lớn
    easy.sort()
    medium.sort()
    hard.sort()
    unknown.sort()

    # 3. TẠO BẢNG MỚI
    table = "| # | Bài toán | Lời giải | Độ khó | Time | Space | Topic Tags |\n"
    table += "|---|---|---|---|---|---|---|\n"

    # Lắp ghép các nhóm lại theo thứ tự: Easy -> Medium -> Hard
    for group in [easy, medium, hard, unknown]:
        for folder, diff in group:
            parts = folder.split('-')
            num = parts[0]
            name = " ".join(parts[1:]).title()
            link_lc = f"https://leetcode.com/problems/{'-'.join(parts[1:])}/"
            link_git = f"[Python](./{folder})"
            
            # Khôi phục dữ liệu cũ, nếu là bài mới toanh thì để `O(?)`
            time_val = old_data.get(num, {}).get('time', '`O(?)`')
            space_val = old_data.get(num, {}).get('space', '`O(?)`')
            tag_val = old_data.get(num, {}).get('tags', '🏷️')

            table += f"| {num} | [{name}]({link_lc}) | {link_git} | {diff} | {time_val} | {space_val} | {tag_val} |\n"

    # 4. NẠP DỮ LIỆU (LOAD): Ghi đè vào file README
    start_marker = ""
    end_marker = ""
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx + len(start_marker)] + "\n" + table + content[end_idx:]
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Đã cập nhật README thông minh thành công!")

if __name__ == "__main__":
    update_readme()
