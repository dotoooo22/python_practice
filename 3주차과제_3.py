##2021041021 곽민정
##하트 모양 출력하기

i, k, heartNum = 0, 0, 0
numStr, ch, heartStr = "", "", ""

if __name__ == "__main__" :
    numStr = input("숫자를 여러 개 입력하세요 : ")     ##숫자입력
    print("")
    i = 0
    ch = numStr[i]      ##i번째문자를넣음
    while True:
        heartNum = int(ch)      ##문자를 정수로변환

        heartStr = ""
        for k in range(0, heartNum) :   ##숫자만큼하트출력
            heartStr += "\u2665"
            k += 1

        print(heartStr)
        
        i += 1      ##다음글자로
        if(i > len(numStr) -1) :        ##문자길이만큼하면루프빠져나감
            break

        ch = numStr[i]      ##다음수
