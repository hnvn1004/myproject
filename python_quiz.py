import random

questions = [
    {
        "question": "Lệnh nào in ra màn hình 'Hello World'?",
        "options": ["print('Hello World')", "echo 'Hello World'", "printf('Hello World')", "write('Hello World')"],
        "answer": "print('Hello World')"
    },
    {
        "question": "Câu lệnh tạo danh sách trong Python?",
        "options": ["list = []", "list = {}", "list = ()", "list = <>"],
        "answer": "list = []"
    },
    {
        "question": "Câu lệnh kiểm tra số chẵn?",
        "options": ["if n % 2 == 0:", "if n / 2 == 0:", "if n // 2 == 0:", "if n * 2 == 0:"],
        "answer": "if n % 2 == 0:"
    },
    {
        "question": "Câu lệnh để tạo vòng lặp từ 1 đến 5?",
        "options": ["for i in range(1,6):", "for i in range(5):", "while i < 5:", "loop i from 1 to 5:"],
        "answer": "for i in range(1,6):"
    },
    {
        "question": "Câu lệnh để chạy file Python 'hello.py' trong Termux?",
        "options": ["python hello.py", "run hello.py", "execute hello.py", "./hello.py"],
        "answer": "python hello.py"
    }
]

def quiz_game():
    print("=== Mini Game Quiz Python - Ôn lại lệnh đã học ===")
    score = 0
    random.shuffle(questions)
    
    for q in questions:
        print("\n" + q["question"])
        for idx, opt in enumerate(q["options"], 1):
            print(f"{idx}. {opt}")
        
        try:
            choice = int(input("Chọn đáp án (1-4): "))
            if 1 <= choice <= 4:
                if q["options"][choice-1] == q["answer"]:
                    print("Đúng! 👍")
                    score += 1
                else:
                    print(f"Sai! Đáp án đúng là: {q['answer']}")
            else:
                print("Vui lòng chọn số từ 1 đến 4")
        except ValueError:
            print("Vui lòng nhập số nguyên từ 1 đến 4")

    print(f"\n=== Kết thúc Quiz! Điểm của bạn: {score}/{len(questions)} ===")

if __name__ == "__main__":
    play_again = "y"
    while play_again.lower() == "y":
        quiz_game()
        play_again = input("Bạn có muốn chơi lại không? (y/n): ")
    print("Cảm ơn đã chơi Mini Game Quiz Python!")
