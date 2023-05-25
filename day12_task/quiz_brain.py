# Blue print of the Game

class QuizzBrain:
    
    # constructor of the class
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
    
    # method to play the quiz game    
    def play(self):
        self.num = 1
        self.score = 0
        while self.question_number < len(self.question_list):
            self.ans = self.question_list[self.question_number].answer_q.lower()
            self.result = input(f"Q.{self.num}: {self.question_list[self.question_number].text_q}. (True/False)?:").lower()
            
            while self.result not in ["true","false"]:
                print("Wrong Input dear User try again")
                self.result = input(f"Q.{self.num}: {self.question_list[self.question_number].text_q}. (True/False)?:")
            
            if self.result == self.ans:
                self.score += 1
                print(f"You are right! Answer is {self.ans}")
                print(f"Your current score is {self.score}")
            else:
                print(f"You are Wrong! Answer is {self.ans}")
                print(f"Your current score is {self.score}")   
                
            self.question_number = self.question_number + 1
            self.num += 1
            
     