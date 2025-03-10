# repo1
Quiz Program

Description:
This is a basic Python quiz program that allows users to test their knowledge across different categories such as General Knowledge, Science, and History. The program displays questions from a selected category, allows the user to answer them, and provides feedback on whether the answers are correct. Additionally, there is a time limit of 10 seconds for each question.

Features:
- Categories: The quiz includes different categories (General Knowledge, Science, History).
- Time Limit: The user has 10 seconds to answer each question.
- Simple Interface: The program asks questions in sequence, checks answers, and provides feedback.
- Feedback: After the quiz, the user receives a score along with feedback based on their performance.

Requirements:
- Python 3.x installed on your system.

How to Run:
1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the quiz.py file is located.
4. Run the following command to execute the program:
   python quiz.py
5. The program will ask questions, and you will need to input your answers.

How it Works:
1. Questions & Categories: The quiz is structured in categories (General Knowledge, Science, History) with predefined questions and answers.
2. Time Limit: You will have 10 seconds to answer each question. If you take longer than 10 seconds, you will be informed that the time is up.
3. Answer Checking: After each question, your answer will be checked. If correct, you will get a "Correct!" message; otherwise, you’ll be shown the correct answer.
4. Final Score: At the end of the quiz, the program will display your score out of the total number of questions asked. Based on your score, you will receive feedback:
   - "Perfect! You're a quiz master!" (for perfect score)
   - "Good job! You're doing great." (for good performance)
   - "Better luck next time!" (for a lower score)

Example Output:
Welcome to the General Knowledge Quiz!

What is the capital of France? (You have 10 seconds to answer): Paris
Correct!
Who wrote 'Romeo and Juliet'? (You have 10 seconds to answer): Shakespeare
Correct!
What is 2 + 2? (You have 10 seconds to answer): 4
Correct!

Your final score is: 3/3
Perfect! You're a quiz master!

Customization:
You can modify the quiz by:
- Adding more categories and questions: Simply add more key-value pairs to the quiz dictionary.
- Changing the time limit: Modify the time limit in the ask_question() function if you'd like to give users more or less time to answer.
- Adding difficulty levels: You can categorize questions into different difficulty levels (easy, medium, hard) and allow the user to choose the difficulty before starting the quiz.

License:
This project is open-source. Feel free to modify, use, and distribute it as needed.
