n = int(input())
group_word = 0
for _ in range(n):
    word = input()
    count = 0
    for i in range(len(word)-1):  # 헷갈렸던 부분, 글자의 다음을 탐색할 때 마지막 글자는 다음이 없으므로 len(word)-1을 해줘야한다
        if word[i] != word[i+1]:  # 글자와 그 글자의 다음이 다르다면
            new_word = word[i+1:]  # 글자 다음부터 new_word에 담음 ex) happy -> appy
            # print(new_word)
            if new_word.count(word[i]) > 0:  # appy 에서 h 개수 세기
                count += 1  # 있다면 1씩 증가(그룹단어가 아님)
    if count == 0:  # 그룹단어라면
        group_word += 1  # 카운트
print(group_word)






