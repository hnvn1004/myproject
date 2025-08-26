import random

def guess_game():
    print("=== Chào mừng bạn đến với Mini Game: Đoán số ===")
    secret = random.randint(1, 50)
    attempts = 0
    max_attempts = 7
    guessed = False

    while attempts < max_attempts:
        try:
            guess = int(input(f"Lần {attempts+1}/{max_attempts}, đoán số (1-50): "))
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")
            continue

        attempts += 1

        if guess < secret:
            print("Số quá nhỏ!")
        elif guess > secret:
            print("Số quá lớn!")
        else:
            print(f"Chúc mừng! Bạn đoán đúng sau {attempts} lần.")
            guessed = True
            break

    if not guessed:
        print(f"Thật tiếc! Số bí mật là {secret}")

    print("=== Thống kê kết quả ===")
    if guessed:
        print(f"Bạn đoán đúng trong {attempts} lần")
    else:
        print(f"Bạn đã hết lượt, số bí mật là {secret}")

if __name__ == "__main__":
    play_again = "y"
    while play_again.lower() == "y":
        guess_game()
        play_again = input("Bạn có muốn chơi lại không? (y/n): ")
    print("Cảm ơn đã chơi Mini Game!")
