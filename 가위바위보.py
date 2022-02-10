import random
print('1. 가위\n2. 바위\n3. 보')
my = int(input('숫자입력 : '))
com = random.randint(1, 3)
print('나: ', my)
print("컴퓨터: ", com)
if (my == 1 and com == 3) or (my == 2 and com == 1) or (my == 3 and com == 2):
    print('승리')
elif (my == com):
    print('무승부')
else:
    print('패배')
