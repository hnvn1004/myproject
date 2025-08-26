import random
import time

commands = [
    "print('Hello World')",
    "list = []",
    "for i in range(1,6):",
    "if n % 2 == 0:",
    "python hello.py",
    "git add .",
    "git commit -m 'message'",
    "git push",
    "nano file.py"
]

def typing_game():
    print("=== Mini Game Luyện gõ lệnh Python & Termux ===")
    score = 0
    random.shuffle(commands)
    
    for cmd in commands:
        print(f"\nGõ chính xác lệnh sau trong 15 giây:\n{cmd}")
        start_time = time.time()
        user_input = input(">>> ")
        elapsed = time.time() - start_time
        
        if user_input == cmd and elapsed <= 15:
            print(f"Đúng! 👍 ({elapsed:.1f} giây)")
            score += 1
        else:
            print(f"Sai hoặc quá thời gian! Đúng là: {cmd} ({elapsed:.1f} giây)")

    print(f"\n=== Kết thúc! Điểm của bạn: {score}/{len(commands)} ===")

if __name__ == "__main__":
    play_again = "y"
    while play_again.lower() == "y":
        typing_game()
        play_again = input("Bạn có muốn chơi lại không? (y/n): ")
    print("Cảm ơn đã chơi Mini Game Luyện gõ lệnh!")
