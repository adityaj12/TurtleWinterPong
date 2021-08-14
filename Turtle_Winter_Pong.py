import turtle
import random
import time

#create one screen which changes colors
screen = turtle.Screen()
screen.colormode(255)

#turtle that writes the name of the game
title = turtle.Turtle()
title.ht()
title.color('purple')
title.penup()
title.goto(-12.5,205)
title.write("Winter Pong", align = "center", font = ("Times New Roman", 24, "normal"))

#initialize two paddles
paddle = turtle.Turtle()
paddle.ht()
paddle.shape("turtle")
paddle.color("blue")
paddle.setheading(90)

paddle2 = turtle.Turtle()
paddle2.ht()
paddle2.shape("turtle")
paddle2.color("purple")
paddle2.setheading(90)

#initialize the ball that is hit
ball = turtle.Turtle()
ball.ht()
ball.shape("circle")
ball.color("red")

#initialize the two turtles that actually draw
t = turtle.Turtle()
t.ht()
box = turtle.Turtle()
box.ht()

#background color changing function
def background(s):
  for i in range(0, 255):
    r = i
    g = 255 - i
    b = 254
    s.bgcolor(r,g,b)
    time.sleep(0.01)
   
  for i in range(0,255):
    r = 255 - i
    g = i
    b = 255
    s.bgcolor(r,g,b)
    time.sleep(0.01)

background(screen)

#function that draws snowflake after victory
def snowflake():
  t.ht()
  t.speed(0)
  t.penup()
  t.goto(0,0)
  t.pendown()
  
  for i in range(6):
      t.goto(0,0)
      t.right(60)
      if i % 3 == 0:
        t.pencolor("white")
      elif i % 3 == 1:
        t.pencolor("blue")
      else:
        t.pencolor("violet")
      
      for i in range(12):
          t.forward(5)
          t.left(45) 
          t.forward(20)
          t.backward(20)
          t.right(45)
          t.right(45)
          t.forward(20)
          t.backward(20)
          t.left(45)

#main function that starts game
def winter_pong():  
    
    ball.ht()
    paddle.ht()
    paddle2.ht()
    t.reset()
    box.reset()
    t.ht()
    box.ht()

    paddle.penup()
    paddle.setheading(90)
    paddle.goto(-200,0)
    paddle.st()
    
    paddle2.penup()
    paddle2.setheading(90)
    paddle2.goto(200,0)
    paddle2.st()
    
    ball.penup()
    ball.goto(0,0)
    ball.rt(random.randint(150,300))
    ball.st()
    
    #creates boundaries
    box.speed(5)
    box.color("purple")
    box.penup()
    box.st()
    box.goto(-200,200)
    box.pendown()
    
    for i in range(4):
      box.fd(400)
      box.rt(90)
    
    while True:
        
      ball.fd(3)
      
      #ball bouncing after hitting top/bottom boundary
      if abs(ball.xcor() - paddle.xcor()) < 10 and abs(ball.ycor() - paddle.ycor()) < 20:
          ball.speed(0)
          ball.setheading(0)
          ball.rt(random.randint(1,89))
          ball.fd(10)
          ball.speed(10)
      
      if abs(ball.xcor() - paddle2.xcor()) < 10 and abs(ball.ycor() - paddle2.ycor()) < 20:
          ball.speed(0)
          ball.setheading(180)
          ball.rt(random.randint(1,89))
          ball.fd(10)
          ball.speed(10)
      
      #game over when ball touches left or right boundary
      elif ball.xcor() >= 210:
        paddle.goto(0,0)
        snowflake()
        for i in range(8):
            paddle.rt(90)
        break
      
      elif ball.ycor() >= 197:
        ball.speed(0)
        ball.setheading(0)
        ball.rt(random.randint(91,179))
        ball.fd(10)
        ball.speed(10)
      
      elif ball.xcor() <= -210:
        paddle2.goto(0,0)
        snowflake()
        for i in range(8):
            paddle2.rt(90) 
        break
    
      elif ball.ycor() <= -197:
        ball.speed(0)
        ball.setheading(180)
        ball.rt(random.randint(91,179))    
        ball.fd(10) 
        ball.speed(10)

#movement of paddles
def up():
  paddle.fd(15)
    
def down():
  paddle.bk(15)
        
def up2():
  paddle2.fd(15)
    
def down2():
  paddle2.bk(15)
    
screen.onkey(winter_pong, "r")
screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(up2, "o")
screen.onkey(down2, "l")
    
screen.listen()

winter_pong()