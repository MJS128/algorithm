#  “(())()”와 “((()))” 는 VPS
#  “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열
#  입력은 T개의 테스트 데이터
#  하나의 괄호 문자열의 길이는 2 이상 50 이하
#  입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력


# sum>0 sum<0, break 빠짐

n = int(input())

for i in range(n):
    x = input()
    y = list(x)
    sum = 0
    for i in y:
        if i == '(' :
            sum += 1            
        elif i == ')':
            sum -= 1
        if sum < 0 :
            print('no')
            break    
    if sum == 0 :
        print('yes')
    elif sum > 0 :
        print('no')    

           
