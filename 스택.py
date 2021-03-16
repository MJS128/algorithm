# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 명령의 수 N (1 ≤ N ≤ 10,000)
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
# 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.

import sys 
n =  int(sys.stdin.readline().rstrip())
stack= []

for i in range(n):
    if input=="push(x)":
        stack.append(i) 

    elif input=="top" :
        if stack > 0 :
            print (stack[-1])
        else: 
            print(-1)     
    elif input=="size":
        print(stack.pop())

    elif input == "empty":
        if stack > 0 :
            print (1)
        else:
            print (0)
    else: 
        if not stack:
            print (-1)
        else:
            stack.pop()
            print(stack.pop())    
      
print(stack)                                    

