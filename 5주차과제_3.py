##2021041021 곽민정
##나선형으로 문자열 출력하기
import turtle
import random
import math
from tkinter.simpledialog import *

inStr = ''
swidth, sheight = 500, 500
tX, tY, txtSize = 0,0,20
radius, angle, radian = 200, 0, 0

turtle.title('거북이 나선형 모양의 글자쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)	 
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

angle = 360*2 / len(inStr)##두바퀴돌리기

for ch in inStr :

    radian = 3.14 * angle / 180 ##라디안으로 각도구하기

    tX = radius * math.cos(radian) ##x좌표 구하기
    tY = radius * math.sin(radian) ##y좌표 구하기
    r = random.random(); g = random.random(); b = random.random()

    turtle.goto(tX, tY)
	 
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))
    radius -= 5 ##거리5씩좁히기
    angle += (360*2) / len(inStr) ##두바퀴돌린 다음 각도 구하기

turtle.done()
