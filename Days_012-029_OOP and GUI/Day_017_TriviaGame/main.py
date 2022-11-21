from data import question_data
from question_model import Question
import quiz_brain

# Creating question objects
question_bank = [Question(entry['question'], entry['correct_answer']) for entry in question_data]

# Creating quiz brain
quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions:
    quiz.next_question()
    
print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{len(question_bank)}")