class QuizBrain:

    def __init__(self, question_list: list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self) -> None:
        current_question = self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer
        current_question_number = self.question_number + 1
        user_input = input(
            f"Q.{current_question_number}: {current_question} (True/False) "
        )
        self.question_number += 1
        self.check_answer(user_answer=user_input, correct_answer=correct_answer)

    def still_has_question(self) -> bool:
        return self.question_number == len(self.question_list)

    def check_answer(self, user_answer: str, correct_answer: str) -> bool:
        result = user_answer.lower() == correct_answer.lower()
        console_text = (
            " You got it right!🥳"
            if result
            else f" That's wrong.🥶 \n Correct answer is: {correct_answer}"
        )
        if result:
            self.score += 1
        print(
            f"{console_text}\n Your current score is: {self.score}/{self.question_number}\n"
        )
