import time
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Paragraphs
easy = [
    "Python is fun",
    "Coding improves logic",
    "Practice every day"
]

medium = [
    "Typing speed improves with consistent practice.",
    "Python is widely used in artificial intelligence.",
    "Building projects helps students learn faster."
]

hard = [
    "Artificial intelligence is transforming modern software development.",
    "Consistency and discipline are important for becoming a good programmer.",
    "Complex algorithms often require optimization for better performance."
]

# Accuracy function
def calculate_accuracy(original, typed):
    correct_chars = 0

    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(original)) * 100
    return round(accuracy, 2)

# Save scores
def save_score(username, wpm, accuracy):
    with open("scores.txt", "a") as file:
        file.write(f"{username},{round(wpm,2)},{accuracy}\n")

# Show leaderboard
def show_leaderboard():
    print(Fore.CYAN + "\n🏆 LEADERBOARD")
    print("-" * 40)

    try:
        with open("scores.txt", "r") as file:
            scores = []

            for line in file:
                data = line.strip().split(",")

                if len(data) == 3:
                    username = data[0]
                    wpm = float(data[1])
                    accuracy = data[2]

                    scores.append((username, wpm, accuracy))

            scores.sort(key=lambda x: x[1], reverse=True)

            for i, score in enumerate(scores[:5], start=1):
                print(f"{i}. {score[0]} - {score[1]} WPM - {score[2]}%")

    except FileNotFoundError:
        print("No scores yet.")

# Countdown
def countdown():
    print(Fore.YELLOW + "\nGet ready!")

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    print(Fore.GREEN + "GO!\n")

# Main typing test
def typing_test(paragraph, username):

    print(Fore.MAGENTA + "\nType the following sentence:\n")
    print(Style.BRIGHT + paragraph)

    input(Fore.YELLOW + "\nPress Enter when ready...")

    countdown()

    start_time = time.time()

    typed_text = input(Fore.WHITE + "Start typing:\n")

    end_time = time.time()

    time_taken = end_time - start_time

    word_count = len(typed_text.split())

    wpm = (word_count / time_taken) * 60

    accuracy = calculate_accuracy(paragraph, typed_text)

    print(Fore.CYAN + "\n📊 RESULTS")
    print("-" * 40)

    print(Fore.GREEN + f"Time Taken : {round(time_taken, 2)} sec")
    print(Fore.BLUE + f"WPM        : {round(wpm, 2)}")
    print(Fore.MAGENTA + f"Accuracy   : {accuracy}%")

    save_score(username, wpm, accuracy)

# MAIN PROGRAM

print(Fore.CYAN + "⌨️ WELCOME TO TYPING SPEED TEST")
print("-" * 40)

username = input("Enter your username: ")

while True:

    print(Fore.YELLOW + "\nChoose Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Leaderboard")
    print("5. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        paragraph = random.choice(easy)
        typing_test(paragraph, username)

    elif choice == "2":
        paragraph = random.choice(medium)
        typing_test(paragraph, username)

    elif choice == "3":
        paragraph = random.choice(hard)
        typing_test(paragraph, username)

    elif choice == "4":
        show_leaderboard()

    elif choice == "5":
        print(Fore.RED + "\nThanks for playing!")
        break

    else:
        print(Fore.RED + "\nInvalid choice.")