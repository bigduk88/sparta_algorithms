# num1 = set(range(1, 10000))             #1~10000 까지 입력
# num2 = set()                            #집합자료형 set 선언

# for i in range(1, 10000):               # ex) i = 365
#     for j in str(i):                    # j = 3, 6, 5
#         i = i + int(j)                     # 365 + 3 + 6 + 5, i = 379
#     num2.add(i)                         # 생성자가 있는 숫자들을 num2에 담아준다.

# num3 = sorted(num1 - num2)              # 1~10000 자연수에서 생성자가 있는 수를 빼준다. sorted는 오름차순 정렬.
# for i in num3:                          
#     print(i)                            # for문이 돌면서 한줄씩 출력.


### 2번 째 풀이 함수형
# http://kmelon55.com/?p=172

# generate_num = []
# natural_num = list(range(1, 10001))
# def d(n):                 # n = 33 일 때
#     num = list(str(n))     # num = ['3', '3']
#     dnum = 0
#     # i = [0, 1] len(num)은 intiger라 for문에 쓸 수 없음, range 사용
#     for i in range(len(num)):
#         dnum += int(num[i])    # dnum = 0 + 3 + 3
#     return n + dnum         # d(n) = 33+ 3 + 3
# for i in natural_num:
#     generate_num.append(d(i))
# for j in natural_num:           # j = [1,2,3, ... , 10000]
#     if j in generate_num:
#         continue
#     else:
#         print(j)