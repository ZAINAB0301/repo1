import time

# Define a dictionary with categories
quiz = {
    "General Knowledge": {
        "What is the capital of France?": "Paris",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is 2 + 2?": "4",
    },
    "Science": {
        "What is the chemical symbol for water?": "H2O",
        "What is the largest planet in our solar system?": "Jupiter",
        "What is the boiling point of water in Celsius?": "100",
    },
    "History": {
        "Who was the first President of the United States?": "George Washington",
        "In what year did World War II end?": "1945",
        "Who was the last czar of Russia?": "Nicholas II",
    }
}

# Function to ask questions with a time limit
def ask_question(question, correct_answer):
    start_time = time.time()  # Track start time
    user_answer = input(question + " (You have 10 seconds to answer): ")
    
    # Check if time is up
    if time.time() - start_time > 10:
        print("Time's up! You took too long to answer.")
        return False
    
    # Check if the answer is correct
    if user_answer.strip().lower() == correct_answer.lower():
        return True
    else:
        print("Wrong! The correct answer is " + correct_answer + ".")
        return False

# Main function to start the quiz
def start_quiz():
    score = 0
    total_questions = 0

    # Randomly choose a category
    category = list(quiz.keys())[0]  # Choose the first category as default
    print("Welcome to the " + category + " Quiz!\n")
    
    # Ask questions from the selected category in the order they appear
    for question, correct_answer in quiz[category].items():
        total_questions += 1
        if ask_question(question, correct_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
        
        # Optional: Pause to let user breathe before next question
        time.sleep(1)

    # Show final score and feedback
    print("\nYour final score is: " + str(score) + "/" + str(total_questions))

    # Provide feedback based on score
    if score == total_questions:
        print("Perfect! You're a quiz master!")
    elif score >= total_questions // 2:
        print("Good job! You're doing great.")
    else:
        print("Better luck next time!")

# Start the quiz
start_quiz()
