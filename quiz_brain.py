from typing import List
from question_model import Question


class QuizBrain:
    def __init__(self, question_bank: List[Question]):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_question(self) -> bool:
        # Return True if there are more questions to ask
        return self.question_number < len(self.question_list)

    def next_question(self):
        answer = input(f"Q.{self.question_number}: {self.question_list[self.question_number].text} (True/False): ")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.lower() == correct_answer.lower():
            print("Right")
            self.score += 1
        else:
            print("Wrong")
        print(f"Your current score is {self.score}/{len(self.question_list)}")
