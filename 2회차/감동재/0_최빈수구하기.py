import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
 
for test_case in range(0,T):
    x = input()
    I =input().split()
    dic ={}
 
    for i in I:
        if i in dic:
            dic[i]+=1
        else :
            dic[i] = 1
 
    max_cnt = 0
    current_max =0
 
    for d in dic:
        if dic[d] >= max_cnt:
            max_cnt = dic[d]
            if int(d) >= current_max:
                current_max = int(d)
 
    print(f"#{test_case+1} {current_max}")
