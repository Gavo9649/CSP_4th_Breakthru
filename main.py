import turtle as trtl
import random
import time

my_bricks_r1 = []
my_bricks_r2 = []
my_bricks_r3 = []
colors = ["red", "blue", "green", "orange", "purple", "gold"]
brick_colors = ['red', 'green', 'blue']

running = False

def move_platform_right():
  if platform_turtle.xcor() < 239:
    platform_turtle.forward(20)

def move_platform_left():
  if platform_turtle.xcor() > -239:
    platform_turtle.backward(20)

def platform_color():
  platform_turtle.color(colors[random.randint(0, 5)])

def ball_color():
  ball_turtle.color(colors[random.randint(0, 5)])

def start_game():
    global running
    running = True
    start_game_turtle.clear()
    start_game_turtle.hideturtle()
    text_turtle.hideturtle()
  
lives = 1
my_lives = []  
  
life_x = -210
life_y = 203
for life in range(lives):
  life = trtl.Turtle(shape='circle')
  life.speed(0), life.penup()
  my_lives.append(life)
  life.goto(life_x, life_y)
  life_x += 25

score = 0
platform_turtle = trtl.Turtle(shape='square')
platform_turtle.speed(0), platform_turtle.turtlesize(stretch_len=5), platform_turtle.penup(), platform_turtle.goto(0, -220), platform_turtle.speed(7), platform_turtle.setheading(0)

ball_velx = 0 #initial x velocity on game start
ball_vely = -10 #initial y velocity on game start
ball_turtle = trtl.Turtle(shape='circle')
ball_turtle.speed(0), ball_turtle.turtlesize(1), ball_turtle.penup(), ball_turtle.goto(0, -195), ball_turtle.speed(3)
 
text_turtle = trtl.Turtle()
text_turtle.speed(0), text_turtle.penup(), text_turtle.goto(-285, 190)
text_turtle.pendown(), text_turtle.write("Lives - ", font=("Arial", 20, "normal"))
text_turtle.penup()

start_game_turtle = trtl.Turtle()
start_game_turtle.goto(0, 0), start_game_turtle.write("Press Enter to Start", align='center', font=("Arial", 40, "normal"))

wn = trtl.Screen() #creates screen
wn.setup(600, 450) #sets screen size
wn.title("Atami Breakthru")
wn.listen() #listens for key presses on the window
wn.onkeypress(move_platform_right, "Right")
wn.onkeypress(move_platform_left, "Left")
wn.onkeypress(platform_color, "space")
wn.onkeypress(ball_color, "b")
wn.onkey(start_game, 'Return')

while True:
  wn.update()
  while running:
      wn.update()
      wn.title("Atami Breakthru - Score: " + str(score))
      ball_turtle.goto((ball_turtle.xcor()+ball_velx), (ball_turtle.ycor()+ball_vely))
      platform_turtle.setheading(0)

      if ball_turtle.xcor() > 280:
          ball_turtle.setx(280)
          ball_velx *= -1
    
      if ball_turtle.xcor() < -285:
          ball_turtle.setx(-285)
          ball_velx *= -1

      if ball_turtle.ycor() > 210:
          ball_turtle.sety(210)
          ball_vely *= -1

      if ball_turtle.ycor() < -200 and ball_turtle.ycor() > -215 and ball_turtle.xcor() < (platform_turtle.xcor() + 50) and ball_turtle.xcor() > (platform_turtle.xcor() - 50):
          score += 1 # breaking a tile will count as a score, not hitting the platform. This is just proof of concept
          ball_turtle.sety(-200)

          ball_vely *= -1
          ball_velx = ((ball_turtle.xcor() - platform_turtle.xcor()) * .3)

      elif ball_turtle.xcor() == platform_turtle.xcor() and ball_turtle.ycor() < -200 and ball_turtle.ycor() > -215:
          ball_velx = 0

    
      if ball_turtle.ycor() < -215 and lives >= 1: #ball is below the platform
          my_lives[lives-1].hideturtle()
          lives -= 1
          ball_velx = 0
          ball_turtle.goto(platform_turtle.xcor(), -195)

      elif ball_turtle.ycor() < -215 and lives == 0:
          text_turtle.clear()
          ball_turtle.hideturtle()
          platform_turtle.hideturtle()
          end_game_turtle = trtl.Turtle()
          end_game_turtle.speed(0), end_game_turtle.penup(), end_game_turtle.goto(0, 100)
          end_game_turtle.pendown(), end_game_turtle.write("Game Over", align='center', font=("Arial", 40, "normal"))
          end_game_turtle.penup(), end_game_turtle.goto(0, 0)
          end_game_turtle.pendown()
          for i in range(100000):
            end_game_turtle.speed(1)
            end_game_turtle.pensize(5)
            end_game_turtle.color(colors[random.randint(0, 5)])  
            end_game_turtle.setheading(random.randint(0, 360))
            end_game_turtle.forward(random.randint(0, 50))
            
            
   
wn.mainloop()
