n = input(int())

m = input(int())

count=[]  #횟수
result=[]  #저장값
stack=[]  #임시저장소



for i in range(int(n)):    # 상근이가 들고있는 카드가 맞다면
   
    while i == n:
        stack.append(count)
        count = count + 1
        result.append("1")
    if i != n:               # 상근이가 들고있는 카드가 아니라면 dadfaf
        stack.pop()
        result.append("0")


    print (result)        

