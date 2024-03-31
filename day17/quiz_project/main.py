from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [
    Question(text=question_data[i]["question"], answer=question_data[i]["correct_answer"])
    for i in range(0, len(question_data))
]

quiz = QuizBrain(question_bank)
while not quiz.still_has_question():
    quiz.next_question()
print(
    f"You've completed the quiz\nYour final score was: {quiz.score}/{quiz.question_number}"
)
