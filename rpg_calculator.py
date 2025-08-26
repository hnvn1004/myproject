import random

def calculate_attack():
    print("=== Mini Calculator RPG ===")
    player_hp = 50
    monster_hp = 50
    turn = 1

    while player_hp > 0 and monster_hp > 0:
        print(f"\n--- Turn {turn} ---")
        print(f"HP bạn: {player_hp} | HP quái vật: {monster_hp}")
        
        # Nhập phép tính
        try:
            expr = input("Nhập phép tính (ví dụ: 2 + 3 * 4): ")
            damage = eval(expr)  # tính toán phép tính
        except:
            print("Phép tính không hợp lệ, mất lượt!")
            damage = 0

        # Player tấn công
        monster_hp -= damage
        print(f"Bạn tấn công gây {damage} sát thương!")

        # Monster phản đòn nếu còn HP
        if monster_hp > 0:
            monster_attack = random.randint(5, 15)
            player_hp -= monster_attack
            print(f"Quái vật phản đòn gây {monster_attack} sát thương!")

        turn += 1

    if player_hp <= 0 and monster_hp <= 0:
        print("\nHòa! Cả 2 cùng gục.")
    elif player_hp <= 0:
        print("\nBạn thua! Quái vật chiến thắng.")
    else:
        print("\nChúc mừng! Bạn đánh bại quái vật.")

if __name__ == "__main__":
    play_again = "y"
    while play_again.lower() == "y":
        calculate_attack()
        play_again = input("Bạn có muốn chơi lại không? (y/n): ")
    print("Cảm ơn đã chơi Mini Calculator RPG!")
