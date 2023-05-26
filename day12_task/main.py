from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = [] # list of Question objects

# i represents different dictionary of questons
for i in question_data: 
    new_ob = Question(i["text"],i["answer"])
    question_bank.append(new_ob)

# Instance of the game attempts    
quiz = QuizzBrain(question_bank)  
print(quiz.play()) 
    