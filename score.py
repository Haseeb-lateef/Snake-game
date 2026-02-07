SCORE_X = 0
SCORE_Y = 270
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0

        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(SCORE_X, SCORE_Y)
        self.update_scoreboard()


    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()




    # def end_game(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align= ALIGNMENT, font= FONT)


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.score+=1
        self.update_scoreboard()









