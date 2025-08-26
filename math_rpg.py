import random

def generate_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(["+", "-", "*"])
    question = f"{a} {op} {b}"
    answer = eval(question)
    return question, answer

def math_rpg():
    print("=== Chào mừng đến với Mini Game Toán RPG ===")
    player_hp = 50
    monster_hp = 50
    turn = 1
    score = 0

    while player_hp > 0 and monster_hp > 0:
        print(f"\n--- Turn {turn} ---")
        print(f"HP bạn: {player_hp} | HP quái vật: {monster_hp}")
        
        q, ans = generate_question()
        try:
            user_input = int(input(f"Giải phép tính để tấn công quái vật: {q} = "))
        except ValueError:
            print("Bạn phải nhập số nguyên!")
            user_input = None

        if user_input == ans:
            dmg = random.randint(5, 15)
            monster_hp -= dmg
            print(f"Chính xác! Bạn gây {dmg} sát thương cho quái vật.")
            score += 1
        else:
            monster_attack = random.randint(5, 15)
            player_hp -= monster_attack
            print(f"Sai! Quái vật phản đòn gây {monster_attack} sát thương.")

        turn += 1

    print("\n=== Kết thúc trận chiến ===")
    if player_hp <= 0 and monster_hp <= 0:
        print("Hòa! Cả hai cùng gục.")
    elif player_hp <= 0:
        print("Bạn thua! Quái vật chiến thắng.")
    else:
        print("Chúc mừng! Bạn chiến thắng quái vật!")
    
    print(f"Điểm kinh nghiệm: {score}")

if __name__ == "__main__":
    play_again = "y"
    while play_again.lower() == "y":
        math_rpg()
        play_again = input("Bạn có muốn chơi lại không? (y/n): ")
    print("Cảm ơn đã chơi Mini Game Toán RPG!")
