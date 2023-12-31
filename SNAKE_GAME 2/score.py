from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        try:
            with open("score_data.txt") as file_score:
                self.high_score = int(file_score.read())
        except FileNotFoundError:
            self.high_score = 0
        self.inrcrease_score()
        self.hideturtle()
        self.update_screen()
        self.game_over
        
    def update_screen(self):
        self.clear()
        self.goto(0,270)
        self.write(f"SCORE : {self.score} HIGH SCORE : {self.high_score}",align="center",font=("Arial", 24, "normal"))
        
    def inrcrease_score(self):
        self.score += 1
        self.update_screen()

    def game_over(self):
        if self.high_score < self.score:
            self.high_score = self.score
        self.score = 0
        self.update_screen()
        