#question

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer.upper()


#Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'\nSoru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print(''+ q)

        answer = input('\nCevap:')
        self.guess(answer)
        self.loadQuestion()


    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score +=1
        self.questionIndex += 1

    def loadQuestion(self):
         if len(self.questions) == self.questionIndex:
             self.showScore()
         else:
             self.displayProgress()
             self.displayQuestion()

    def showScore(self):
        self.displayProgress()
        print('Your Score: ',self.score)


    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('\nQuiz Bitti')
        else:
            print(f' Question {questionNumber} of {totalQuestion} '.center(100,'*'))


q1 = Question("How many different colors has M&M's ?", ['A-3','B-4','C-5','D-6'],'D')
q2 = Question('Which planet is the hottest?', ['A-Venus','B-Mars','C-Saturn','D-Mercury'],'A')
q3 = Question('According to Forrest Gump, "life was like...', ['A- a bag of lemons','B- a handful of roses','C- a lollipop','D- a box of chocolates'],'D')
q4 = Question('What is the rarest blood type?', ['A-0','B-A','C-B','D-AB-Negative'],'D')
q5 = Question('How many bones are there in the human body?', ['A-206','B-205','C-201','D-209'],'A')


questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)
quiz.loadQuestion()

