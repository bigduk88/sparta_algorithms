'''
15650문제 N과 M(2) - 백트레킹
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''

N, M = map(int, input().split())

num_list = [i + 1 for i in range(N)]
check_list = [False] * N

arr = []

def dfs(cnt):
    if(cnt == M):
        print(*arr)
        return
    
    for i in range(0, N):
        if(check_list[i]):
            continue
        
        check_list[i] = True
        arr.append(num_list[i])
        dfs(cnt + 1)
        arr.pop()
        
        # 이 부분이 순열하고의 차이점이다.
        # 큰 나무에서 전에 봤던 것만
        # 닫아주면 된다.
        for j in range(i + 1, N):
            check_list[j] = False
        
dfs(0)



# import sys
# def permutation(target_depth, end):
#     for i in range(1, end + 1):
#         permutation_array = []
#         permutation_inner(target_depth, 1, i, end, permutation_array)
# def permutation_inner(target_depth, current_depth, start, end, array: list[int]):
#     if start > end:
#         return
#     if current_depth == target_depth:
#         print(*array, start)
#         return
#     for i in range(start, end + 1):
#         array.append(start)
#         permutation_inner(target_depth, current_depth + 1, i + 1, end, array)
#         array.pop()
# end, permutation_depth = sys.stdin.readline().rstrip().split()
# end = int(end)
# permutation_depth = int(permutation_depth)
# permutation(permutation_depth, end)