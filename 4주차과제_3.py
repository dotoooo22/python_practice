##2021041021 곽민정
##4주차과제_3

import turtle
import random

myTurtle, tX, tY, tColor, tSize, Tangle = [None] * 6
playerTurtles = []
swidth, sheight = 500, 500
pX, pY = 0, 0
if __name__ == "__main__" :
    turtle.title('거북 리스트 활용')
    turtle. setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)

    for i in range(0, 5) :
        myTurtle = turtle.Turtle('turtle')
        
        tX = random.randrange(-swidth / 2, swidth / 2)
        tY = random.randrange(-sheight / 2, sheight / 2)
        r =random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(1, 100)/10
        tAngle = random.randrange(0, 360)       ##랜덤각도추가
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b, tAngle])
        
    ##turtles[3](크기)로 정렬
    sortedTurtles = sorted(playerTurtles, key = lambda turtles : turtles[3], reverse = False)

    for index, tList in enumerate(sortedTurtles[0:]) :      ##enumerate는 index를 반환해주어서 인덱스값으로 이전위치를 가져올 수 있다
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        pX = tList[1]
        pY = tList[2]
        if index == 0 :         ##첫번째거북이는 이전위치가없으니까 그냥 이동만
            myTurtle.penup()
            myTurtle.goto(tList[1], tList[2])
            myTurtle.stamp()
            continue
        myTurtle.penup()
        myTurtle.goto(sortedTurtles[index-1][1], sortedTurtles[index-1][2])     ##이전위치로이동해서
        myTurtle.pendown()
        myTurtle.goto(tList[1], tList[2])           ##현재위치까지 선그리면서이동
        
        myTurtle.right(tList[7])
    turtle.done()
