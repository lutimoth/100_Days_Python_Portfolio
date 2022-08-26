from data import question_data
from question_model import Question
import quiz_brain

# Creating question objects
question_bank = [Question(question['text'], question['answer']) for question in question_data]

# Creating quiz brain
quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions:
    quiz.next_question()