# 11728문제 하노이 탑 이동 순서 
# 스파르타 알고리즘 2-8,9 재귀 - 재귀함수란 자기 자신을 호출하는 함수 ex. 카운트 다운, 팩토리얼. *무한정 반복되게하면 무한루프에 빠지므로 탈출조건을 넣어야 한다.
# 세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.
# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# 이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.
# 아래 그림은 원판이 5개인 경우의 예시이다.
# 입력
# 첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.
# 출력
# 첫째 줄에 옮긴 횟수 K를 출력한다.
# 두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.

# def hanoi(t, start, dest, remain): 
#     if t == 0: 
#         return 
#     hanoi(t-1, start, remain, dest) #전체 원반 중 가장 큰 원반을 제외하고 중간기둥으로 옮김.
#     print(start, dest)              #시작 기둥에 있는 가장 큰 원반을 목표 기둥으로 옮김.
#     hanoi(t-1, remain, dest, start) #보조 기둥에 원반이 있으므로 기존 보조기둥을 시작기둥으로, 기존 시작기둥을 보조기둥으로 진행.

# n = int(input()) 
# print(2**n-1) 
# hanoi(n, 1, 3, 2),

# def hanoi_tower(n, start, end) :
#     if n == 1 :
#         print(start, end)
#         return

#     hanoi_tower(n-1, start, 6-start-end) # 1단계
#     print(start, end)                    # 2단계
#     hanoi_tower(n-1, 6-start-end, end)   # 3단계

# n = int(input())
# print(2**n-1)
# hanoi_tower(n, 1, 3)


n = int(input())
def hanoi(n, frm, via, to):
    if n == 1:   # 가장 큰 원반이 to로 옮겨지고, 동시에 나머지 원반들이 via로 옮겨감
        print(frm, to)
        return
    else:
        hanoi(n-1, frm, to, via)
        print(frm, to)   #가장 작은 원반이 다른곳으로 옮겨짐 , 나머지원반이 frm에 남음
        # frm에 있는 원반이 또 다른곳으로 옮겨짐, 가장 큰 원반 빼고
        hanoi(n-1, via, to, frm) #via 는 2개의 원반이 있는 상태
hanoi(n, 1, 2, 3)