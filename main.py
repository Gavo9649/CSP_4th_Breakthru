import turtle as trtl
import random

# Sets colors for the game elements
colors = ["red", "blue", "green", "orange", "purple", "gold"]

# Initializes game running variable
running = False

# Function to move platform to the right
def move_platform_right():
  if platform_turtle.xcor() < 239: 
    platform_turtle.forward(20) # Amount platform moves
    if running == False: # If the game has not started, the ball will stay on top of the platform if moved
        ball_turtle.goto(platform_turtle.xcor(), -195)

# Function to move platform to the left
def move_platform_left():
  if platform_turtle.xcor() > -239:
    platform_turtle.backward(20) # Amount platform moves
    if running == False: # If the game has not started, the ball will stay on top of the platform if moved
        ball_turtle.goto(platform_turtle.xcor(), -195)

# Sets the platform to a random color from the 'colors' list
def platform_color():
  platform_turtle.color(colors[random.randint(0, 5)])

# Sets the ball to a random color from the 'colors' list
def ball_color():
  new_color = colors[random.randint(0, 5)]
  ball_turtle.color(new_color)
  for life in my_lives:
    life.color(new_color)

# Start game function; makes the running variable global and sets it to true
def start_game():
    global running
    running = True
    start_game_turtle.clear()
    start_game_turtle.hideturtle()
    text_turtle.hideturtle()


wn = trtl.Screen() # creates screen
wn.setup(600, 450) # screen size
wn.title("Atami Breakthru") # window title
wn.bgpic('1.1.9 Project thing lol/assets/starfield large.gif')
wn.listen() #listens for key presses on the window
wn.onkeypress(move_platform_right, "Right") # right arrow moves plat right
wn.onkeypress(move_platform_left, "Left") # left arrow moves plat left
wn.onkey(platform_color, "space") # 'space' randomizes platform color
wn.onkey(ball_color, "b") # 'b' randomizes ball color
wn.onkey(start_game, 'Return') # 'enter' starts game

# Background color
wn.bgcolor("black")

# Lives text (top left)
text_turtle = trtl.Turtle()
text_turtle.speed(0), text_turtle.penup(), text_turtle.goto(-285, 190)
text_turtle.pencolor("white")
text_turtle.pendown(), text_turtle.write("Lives - ", font=("Arial", 20, "normal"))
text_turtle.penup(), text_turtle.hideturtle()


lives = 3
my_lives = [] # List of circle turtles for lives
  
# Creates lives turtles to draw to the screen (top left)
life_x = -185
life_y = 205
for life in range(lives):
  life = trtl.Turtle(shape='circle')
  life.pencolor("white")
  life.speed(0), life.penup()
  my_lives.append(life)
  life.goto(life_x, life_y)
  life_x += 25

score = 0 # Reset score

# Platform init
platform_turtle = trtl.Turtle(shape='square')
platform_turtle.pencolor("white")
platform_turtle.speed(0)
platform_turtle.turtlesize(stretch_len=5)
platform_turtle.penup(),
platform_turtle.goto(0, -220)
platform_turtle.speed(7)
platform_turtle.setheading(0)

# Ball init
ball_velx = 0 #initial x velocity on game start
ball_vely = -7 #initial y velocity on game start
ball_turtle = trtl.Turtle(shape='circle') 
ball_turtle.pencolor("white")
ball_turtle.speed(0), ball_turtle.turtlesize(1), ball_turtle.penup(), ball_turtle.goto(0, -195), ball_turtle.speed(3) 

my_bricks_r1 = [] # /\
my_bricks_r2 = [] # || empty turtle lists for bricks
my_bricks_r3 = [] # \/

Bricks = 13 # Amount of bricks per row

# Create bricks row 1
Brick_x= -272
Brick_y = 105
for brick in range(Bricks):
  brick = trtl.Turtle(shape='square')
  brick.color("red")
  brick.turtlesize(stretch_len=2)
  brick.speed(0), brick.penup()
  my_bricks_r1.append(brick)
  brick.goto(Brick_x, Brick_y)
  Brick_x += 45

# Create bricks row 2
Brick_x2 = -272
Brick_y2 = 135
for brick in range(Bricks):
  brick = trtl.Turtle(shape='square')
  brick.color("green")
  brick.turtlesize(stretch_len=2)
  brick.speed(0), brick.penup()
  my_bricks_r2.append(brick)
  brick.goto(Brick_x2, Brick_y2)
  Brick_x2 += 45

# Create bricks row 3
Brick_x3 = -272
Brick_y3 = 165
for brick in range(Bricks):
  brick = trtl.Turtle(shape='square')
  brick.color("blue")
  brick.turtlesize(stretch_len=2)
  brick.speed(0), brick.penup()
  my_bricks_r3.append(brick)
  brick.goto(Brick_x3, Brick_y3)
  Brick_x3 += 45
# End brick creation

# Text for start of the game
start_game_turtle = trtl.Turtle()
start_game_turtle.pencolor("white")
start_game_turtle.goto(0, 0), start_game_turtle.write("Press Enter to Start", align='center', font=("Arial", 40, "normal"))
start_game_turtle.penup() 
start_game_turtle.goto(0, -35)
start_game_turtle.pencolor("white")
start_game_turtle.pendown(), start_game_turtle.write("Press 'b' to change ball color, and 'space' to change platform color", font=("Arial", 15, "normal"), align='center')
start_game_turtle.hideturtle()


while True:
  wn.update()
  while running: # Game is running
    wn.update()
    wn.title("Atami Breakthru - Score: " + str(score)) #update title to display score
    platform_turtle.setheading(0)

    # Ball physics
    ball_turtle.goto((ball_turtle.xcor()+ball_velx), (ball_turtle.ycor()+ball_vely)) 
    
    # Ball boundaries (right)
    if ball_turtle.xcor() > 280:
        ball_turtle.setx(280)
        ball_velx *= -1

    # (left)
    if ball_turtle.xcor() < -285:
        ball_turtle.setx(-285)
        ball_velx *= -1

    # (top)
    if ball_turtle.ycor() > 210:
        ball_turtle.sety(210)
        ball_vely *= -1

    # Check if ball is collided with platform
    if ball_turtle.ycor() < -200 and ball_turtle.ycor() > -215 and ball_turtle.xcor() < (platform_turtle.xcor() + 50) and ball_turtle.xcor() > (platform_turtle.xcor() - 50):
        ball_turtle.sety(-200)

        ball_vely *= -1
        ball_velx = ((ball_turtle.xcor() - platform_turtle.xcor()) * .3) #x velocity is based off where it hits the platform

    elif ball_turtle.xcor() == platform_turtle.xcor() and ball_turtle.ycor() < -200 and ball_turtle.ycor() > -215:
        ball_velx = 0

    # Ball is below the platform
    if ball_turtle.ycor() < -215 and lives >= 2: 
        # Remove a life
        my_lives[lives-1].hideturtle()
        lives -= 1
        
        # Reset ball
        ball_velx = 0
        ball_turtle.goto(platform_turtle.xcor(), -195)

    #Game over
    elif ball_turtle.ycor() < -215 and lives == 1:
        my_lives[lives-1].hideturtle()
        lives -= 1
        text_turtle.clear()
        ball_turtle.hideturtle()
        platform_turtle.hideturtle()
        end_game_turtle = trtl.Turtle()
        end_game_turtle.pencolor("white")
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
            
    #Check for brick collision row 1
    for brick in my_bricks_r1:
      if ball_turtle.xcor() < (brick.xcor() + 30) and ball_turtle.xcor() > (brick.xcor() -30) and ball_turtle.ycor() < (brick.ycor() +20) and ball_turtle.ycor() > (brick.ycor() -20):
        ball_vely *= -1.01
        my_bricks_r1.remove(brick)
        brick.hideturtle()
        score += 1

    #Check for brick collision row 2
    for brick in my_bricks_r2:
      if ball_turtle.xcor() < (brick.xcor() + 30) and ball_turtle.xcor() > (brick.xcor() -30) and ball_turtle.ycor() < (brick.ycor() +20) and ball_turtle.ycor() > (brick.ycor() -20):
        ball_vely *= -1.02
        my_bricks_r2.remove(brick)
        brick.hideturtle()
        score += 1

    #Check for brick collision row 3 
    for brick in my_bricks_r3:
      if ball_turtle.xcor() < (brick.xcor() + 30) and ball_turtle.xcor() > (brick.xcor() -30) and ball_turtle.ycor() < (brick.ycor() +20) and ball_turtle.ycor() > (brick.ycor() -20):
        ball_vely *= -1.03
        my_bricks_r3.remove(brick)
        brick.hideturtle()
        score += 1
    
    #Game over if level cleared
    if score == 39:
        text_turtle.clear()
        ball_turtle.hideturtle()
        platform_turtle.hideturtle()
        end_game_turtle = trtl.Turtle()
        end_game_turtle.speed(0), end_game_turtle.penup(), end_game_turtle.goto(0, 100)
        end_game_turtle.pencolor("white")
        end_game_turtle.pendown(), end_game_turtle.write("Level Cleared", align='center', font=("Arial", 40, "normal"))
        end_game_turtle.speed(0), end_game_turtle.penup(), end_game_turtle.goto(0, 50)
        end_game_turtle.pendown(), end_game_turtle.write("Good job", align='center', font=("Arial", 25, "normal"))
        end_game_turtle.speed(0), end_game_turtle.penup(), end_game_turtle.goto(0, -200)
        end_game_turtle.pendown(), end_game_turtle.write("The next level will start soon", align='center', font=("Arial", 15, "normal"))
        end_game_turtle.penup(), end_game_turtle.goto(0, 0)
        end_game_turtle.pendown()
        for i in range(15):
            end_game_turtle.speed(1)
            end_game_turtle.pensize(5)
            end_game_turtle.color(colors[random.randint(0, 5)])  
            end_game_turtle.setheading(random.randint(0, 360))
            end_game_turtle.forward(random.randint(0, 50))
        wn.bye()

wn.mainloop()
