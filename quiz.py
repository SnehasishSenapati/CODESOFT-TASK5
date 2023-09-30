import random

# Quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Mars",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "correct_answer": "Blue Whale",
    },
]

def run_quiz(questions):
    score = 0

    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions. Let's see how well you do.\n")

    for question in questions:
        print(question["question"])
        random.shuffle(question["options"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")

        user_answer = input("Enter the number of your answer: ")
        try:
            user_answer = int(user_answer)
            if 1 <= user_answer <= 4:
                user_answer = question["options"][user_answer - 1]
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if user_answer == question["correct_answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {question['correct_answer']}\n")

    print(f"Quiz completed! Your score is: {score}/{len(questions)}")
    if score == len(questions):
        print("Congratulations! You got all the answers correct.")
    elif score >= len(questions) / 2:
        print("Good job! You did well.")
    else:
        print("You can do better. Keep learning!")

if __name__ == "__main__":
    while True:
        run_quiz(quiz_data)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
