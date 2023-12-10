import random
import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def play_game():
    choice = [1, 2, 3, 4, 5, 6]
    player_total_score = 0
    computer_total_score = 0
    # player_wickets = 0
    innings = 2
    for inning in range(1, innings):
        print(f"Inning {inning} - It's your turn")
        speak(f"Inning {inning} - It's your turn")
        while True:
            player_choice = int(input(f"Enter your choice {choice}: "))
            if player_choice not in choice:
                print("Please choose appropriate options")
                speak("Please choose appropriate options")
                return

            computer_choice = random.choice(choice)
            print(f"The computer choice is {computer_choice}")
            speak(f"The computer choice is {computer_choice}")
            print(f"Your choice is {player_choice}")
            speak(f"Your choice is {player_choice}")

            if player_choice == computer_choice:
                print(f"Oops! You're out!")
                speak(f"Oops! You're out!")
                break
            else:
                player_total_score += player_choice
                print(f"Your total score is {player_total_score}")
                speak(f"Your total score is {player_total_score}")

        if inning == 1:
            print(f"Target for computer is {player_total_score + 1}")
            speak(f"Target for computer is {player_total_score + 1}")

       

    print("\nNow it's the computer's turn")
    for i in range(1, innings):
        while True:
            player_choice = int(input(f"Enter your choice from {choice}: "))
            computer_choice = random.choice(choice)
            print(f"The computer choice is {computer_choice}")
            speak(f"The computer choice is {computer_choice}")



            if player_choice == computer_choice:
                print("Great! You've taken the wicket of the computer.")
                speak("Great! You've taken the wicket of the computer.")
                break
            else:
                computer_total_score += computer_choice
                print(f"Computer's total score is {computer_total_score}")
                speak(f"Computer's total score is {computer_total_score}")

        if computer_total_score > player_total_score:
            print("Computer won the game!")
            speak("Computer won the game!")
        elif computer_total_score < player_total_score:
            print("You won the game!")
            speak("You won the game!")
        else:
            print("It's a tie!")
            speak("It's a tie!")

        print("Game over!")
        speak("Game over!")


if __name__ == "__main__":
    play_game()
    while True:
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break
