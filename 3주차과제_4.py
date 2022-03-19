#2021041021 곽민정
#거북이로 구구단 출력하기

import turtle

i, k, tX, tY = [0] * 4
swidth, sheight = 800, 450

if __name__ == "__main__" :
    turtle.title('거북 구구단')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle. penup()
    tX, tY = -500, 250
    turtle.goto(tX,tY)

    for i in range(1, 10) :     ##1~9까지
        for k in range(2, 10) :     ##2~9까
            turtle.goto(tX + 80 * k, tY - 40 * i)   ##거북이이동
            gugu = str(k) + ' x ' + str(i) + ' = ' + str(k * i)
            turtle.write(gugu, font = ('arial', 12, 'bold'))    ##구구단출력

    
    turtle.done()
