import turtle 
import random
t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
color = ["red","green","blue","pink","gray,"yellow","orange"]
t.pendown
t.color(random.choice(color))

t.lt(36)

for i in range(5):
  t.fd(200)
  t.lt(144)

t.rt(36)

for i in range(5):
  t.fd(123)
  t.lt(72)
