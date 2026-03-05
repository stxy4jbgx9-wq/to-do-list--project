ˆimport random

player_score = 0
cpu_score = 0

print("🎮 Best of 5 Mode — First to 3 Wins!")

while player_score < 3 and cpu_score < 3:

    print("\n1 is for '✊' (Rock).")
    print("2 is for '✋' (Paper).")
    print("3 is for '✌️' (Scissors).")

    try:
        player = int(input("Select a number between 1 and 3: "))

        if player < 1 or player > 3:
            print("❌ Invalid input! Choose 1, 2 or 3.")
            continue

        print(f"\nPlayer chose = {player}")

        if player == 1:
            print("✊ Rock")
        elif player == 2:
            print("✋ Paper")
        else:
            print("✌️ Scissors")

        cpu = random.randint(1, 3)

        print(f"\nCPU chose = {cpu}")

        if cpu == 1:
            print("✊ Rock")
        elif cpu == 2:
            print("✋ Paper")
        else:
            print("✌️ Scissors")

        if player == cpu:
            print("\n🤝 It is a tie!")

        elif (player == 1 and cpu == 3) or \
             (player == 2 and cpu == 1) or \
             (player == 3 and cpu == 2):
            print("\n🎉 Player won!")
            player_score += 1

        else:
            print("\n💻 CPU won!")
            cpu_score += 1   # ✅ fixed this

        print("\nScore:")
        print("Player:", player_score)
        print("CPU:", cpu_score)

    except ValueError:
        print("❌ Invalid input! Please enter a number only.")

print("\n🏁 Match Over!")

if player_score > cpu_score:
    print("🏆 Player wins the match!")
else:
    print("🏆 CPU wins the match!")

