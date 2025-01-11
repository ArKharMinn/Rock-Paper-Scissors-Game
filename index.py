import turtle as t
import random as r

screen=t.Screen()
screen.bgcolor("lightblue")

message="Press s to start a game Press q to exit"

text=t.Turtle()
text.hideturtle()
text.write(message,align="center", font=("Arial", 16, "normal"))
text.goto(0,290)

player_choose=""

chooseText=t.Turtle()
chooseText.hideturtle()

chooseText.write(player_choose,align="center", font=("Arial", 16, "normal"))

choices = ['🪨', '📄', '✂️']


def exit():
    screen.bye()

def start():
    global message
    message=f"Press 1 for rock 🪨, Press 2 for paper 📄, or Press 3 for scissors ✂️ Press q to exit"
    text.clear()
    text.write(message,align="center", font=("Arial", 13, "normal"))
    text.penup()
    update_choice()
    result()
    check()

def update_choice():
    global player_choose
    chooseText.clear() 
    chooseText.write(player_choose, align="center", font=("Arial", 16, "normal"))

def result():
    if player_choose == computer:
        message=f"It's a tie! You choose {player_choose} computer choose {computer}"
        chooseText.clear()
        chooseText.write(message,align="center", font=("Arial", 16, "normal"))
        chooseText.penup()
    elif (player_choose == '🪨' and computer == '✂️') or \
         (player_choose == '✂️' and computer == '📄') or \
         (player_choose == '📄' and computer == '🪨'):
        message=f"You win! You choose {player_choose} computer choose {computer}"
        chooseText.clear()
        chooseText.write(message,align="center", font=("Arial", 16, "normal"))
        chooseText.penup()
    else:
        message=f"You lose! Try again. You choose {player_choose} computer choose {computer}"
        chooseText.clear()
        chooseText.write(message,align="center", font=("Arial", 16, "normal"))
        chooseText.penup()

def check():
    global player_choose
    if player_choose not in ["1","2","2"]:
       player_choose=""
       update_choice()
    
def one():
    global player_choose
    global computer
    player_choose="🪨"
    update_choice()
    computer=r.choice(choices)
    result()

def two():
    global player_choose
    global computer
    player_choose="📄"
    update_choice()
    computer=r.choice(choices)
    result()

def three():
    global player_choose
    global computer
    player_choose="✂️"
    update_choice()
    computer=r.choice(choices)
    result()

screen.listen()
screen.onkey(start,"s")
screen.onkey(exit,'q')
screen.onkey(one,"1")
screen.onkey(two,'2')
screen.onkey(three,"3")
    
screen.mainloop()