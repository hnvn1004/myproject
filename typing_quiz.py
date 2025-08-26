# Mini Game Gõ lệnh + học chức năng
import random

commands = [
    {"cmd": "print('Hello World')", "desc": "In ra màn hình Hello World"},
    {"cmd": "list = []", "desc": "Tạo danh sách rỗng"},
    {"cmd": "for i in range(1,6):", "desc": "Vòng lặp từ 1 đến 5"},
    {"cmd": "if n % 2 == 0:", "desc": "Kiểm tra số chẵn"},
    {"cmd": "python hello.py", "desc": "Chạy file Python hello.py"},
    {"cmd": "git add .", "desc": "Thêm tất cả file vào Git staging"},
    {"cmd": "git commit -m 'message'", "desc": "Commit các file với message"},
    {"cmd": "git push", "desc": "Đẩy commit lên GitHub"},
    {"cmd": "nano file.py", "desc": "Mở file Python để chỉnh sửa"}
]

def typing_quiz():
    print("=== Mini Game Gõ lệnh + học chức năng ===")
    score = 0
    random.shuffle(commands)

    for item in commands:
        print("\nGõ chính xác lệnh sau:")
        print(f"Hướng dẫn: {item['desc']}")
        user_input = input(">>> ")

        if user_input.strip() == item['cmd']:
            print(f"Đúng! ✅ Lệnh này dùng để: {item['desc']}")
            score += 1
        else:
            print(f"Sai! ❌ Đúng là: {item['cmd']} → {item['desc']}")

    print(f"\n=== Kết thúc! Điểm của bạn: {score}/{len(commands)} ===")

if __name__ == "__main__":
    play_again = "y"
    while play_again.lower() == "y":
        typing_quiz()
        play_again = input("Bạn có muốn chơi lại không? (y/n): ")
    print("Cảm ơn đã chơi Mini Game Gõ lệnh + học chức năng!")
