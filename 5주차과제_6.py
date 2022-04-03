##2021041021 곽민정
##재귀 호출로 진수변환하기

def conv(number, base):
	
    strings = "0123456789ABCDEF"
    
    if number < base:
    	return strings[number] ##변환다했을때
	
    else:
    	return conv(number // base, base) + strings[number % base] ##아직더 바꿔야되면 number에 나눈몫, base에 나머지보내기


n2, n8, n16 = '', '', '' ##진수마다 저장할변수선언해놓기

n = int(input('10진수 입력 -->'))

n2 = conv(n, 2)
n8 = conv(n, 8)
n16 = conv(n, 16)

print('2진수 : ', n2)
print('8진수 : ', n8)
print('16진수 : ', n16)
