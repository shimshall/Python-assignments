import random

def high_low_game(rounds):
    score = 0
    print("--------------------------------")
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}")
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        guess = input("Do you think your number is higher or lower than the computer's? (h/l): ").strip().lower()
        
        if (guess == "h" and player_number > computer_number) or (guess == "l" and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}\n")
    
    print("Thanks for playing!")
    print(f"Your final score is {score}")
    
    # Conditional ending messages
    if score == rounds:
        print("Wow! You played perfectly!")
    elif score >= rounds // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Start the game with a defined number of rounds
rounds = 5
high_low_game(rounds)
