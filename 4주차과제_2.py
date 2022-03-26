##2021041021 곽민정
##기차 수송량에 따라 순위 매기기
import operator

trainTupleList = [('토마스', 5), ('헨리', 8), ('에드워드', 9), ('에밀리', 5), \
                  ('토마스', 4), ('헨리', 7), ('토마스', 3), ('에밀리', 8), \
                  ('퍼시', 5), ('고든', 13)]
trainDic, trainList = {}, []
tmpTup = None
totalRank, currentRank = 1, 1

if __name__ == "__main__" :
    for tmpTup in trainTupleList :
        tName = tmpTup[0]
        tWeight = tmpTup[1]
        if tName in trainDic :          ##각자수송량합산해두기
            trainDic[tName] += tWeight
        else :
            trainDic[tName] = tWeight

    print('기차 수송량 목록 ==> ', trainTupleList)
    print('--------------------------------------')
    ##수송량순으로정렬
    trainList = sorted(trainDic.items(), key = operator.itemgetter(1), \
                       reverse = True)
        
    print("%20s" % '기차\t총 수송량\t순위')
    print('--------------------------------------')
    print("%10s" % trainList[0][0], '\t', trainList[0][1], '\t\t', currentRank)     ##제일많은사람출력
    for i in range(1, len(trainList)) :     ##정렬된 순서대로 출력하기
        totalRank += 1      
        if trainList[i][1] == trainList[i-1][1] :       ##수송량같으면순위안더해서같게하기
            pass
        else :
            currentRank = totalRank
        print("%10s" % trainList[i][0], '\t', trainList[i][1], '\t\t', currentRank)
