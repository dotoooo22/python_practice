##16진수 정렬하기
##2021041021 곽민정

import random

data = []
i, k = 0, 0

if __name__ == "__main__" :
    for i in range(0, 10) :     ##10번반복
        tmp = hex(random.randrange(0, 100000))      ##16진수 랜덤 생성
        data.append(tmp)            ##리스트에 추가

    print('정렬 전 데이터 : ', end = '')      
    [print(num, end= ' ') for num in data]

    for i in range(0, len(data) -1) :       ##오름차순정렬하기
        for k in range(i +1, len(data)) :
            if int(data[i], 16) > int(data[k], 16) :
                tmp = data[i]
                data[i] = data[k]
                data[k] = tmp


    print('\n정렬 후 데이터 : ', end = '')
    [print(num, end = ' ') for num in data]
