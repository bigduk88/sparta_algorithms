'''
9663문제 N-Queen - 백트레킹
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
'''

n = int(input())
s = [0 for i in range(16)]
result = 0
def isTrue(x):
    for i in range(1, x):
        if s[x] == s[i] or abs(s[x] - s[i]) == x - i:
            return False
    return True
def dfs(cnt):
    global result
    if cnt > n:
        result += 1
    else:
        for i in range(1, n + 1):
            s[cnt] = i
            if isTrue(cnt):
                dfs(cnt + 1)
dfs(1)
print(result)



# import sys
# class Position:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
# # 새로운 퀸이 배치될 수 있는 위치인지에 대한 판별값을 리턴합니다
# # 새로운 퀸이 배치될 수 있는 위치라면 True를 반환합니다
# def is_valid_place(candidates_list: list[Position], new_candidate: Position):
#     for already_exist_candidate in candidates_list:
#         # 이미 퀸들이 배치되어 있는 위치에서 직선상 또는 대각선상의 위치에는 배치될 수 없습니다
#         is_located_in_straight_line = already_exist_candidate.y == new_candidate.y or already_exist_candidate.x == new_candidate.x
#         is_located_diagonally = abs(already_exist_candidate.y - new_candidate.y) == abs(already_exist_candidate.x - new_candidate.x)
#         if is_located_in_straight_line == True or is_located_diagonally == True:
#             return False
#     # 이미 배치되어 있는 모든 퀸들로부터 간섭받지 않는 최적의 위치입니다
#     return True
# def n_queen(n):
#     candidates_list = []
#     result_list = []
#     n_queen_inner(n, candidates_list, result_list)
#     return len(result_list)
# def n_queen_inner(n, candidates_list: list[Position], result_list: list[list[Position]]):
#     row = len(candidates_list) + 1
#     for col in range(1, n + 1):
#         candidate = Position(col, row)
#         # 새로운 퀸은 기존의 퀸들과 간섭받지 않는 위치에만 배치할 수 있습니다
#         if is_valid_place(candidates_list, candidate) == True:
#             # 이번 for문에서 배치된 퀸이 배치됨으로써 체스판에 n개의 퀸이 전부 세워졌다면
#             # result_list에 “배치된 퀸들의 조합“을 추가합니다
#             if row == n:
#                 result_list.append(candidates_list + [candidate])
#                 return
#             # 아직 N개의 퀸이 배치되지 않았다면 이번 위치를 후보자 위치로 추가한 뒤
#             # 유효 퀸 조합을 다시 찾습니다
#             candidates_list.append(candidate)
#             n_queen_inner(n, candidates_list, result_list)
#             candidates_list.pop()
# # main
# n = int(sys.stdin.readline().rstrip())
# print(n_queen(n))