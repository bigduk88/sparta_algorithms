'''
1149문제 RGB 거리 - 동적 계획법
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
'''

def min(a, b):
    return a if a <= b else b
#RGB를 빨,초,파
#이웃은 같은색이 안됨 i의 이웃은 i-1, i+1
#빨강 비용, 초록 비용, 파랑 비용이 주어질때 최소로 칠 할 수 있는 비용
 
#집의 수
n = int(input())
matrix = [[0]*3 for i in range(n)]
 
 
for i in range(n):
    #각 색별 페인트 비용
    matrix[i][0], matrix[i][1], matrix[i][2] = map(int, input().split())
 
matrix2 = [[0]*3 for i in range(n)]
 
for i in range(n):
    if i == 0:
        matrix2[i] = matrix[i]
    else:
        matrix2[i][0] = matrix[i][0] + min(matrix2[i-1][1], matrix2[i-1][2])
        matrix2[i][1] = matrix[i][1] + min(matrix2[i-1][0], matrix2[i-1][2])
        matrix2[i][2] = matrix[i][2] + min(matrix2[i-1][0], matrix2[i-1][1])
 
print(min(min(matrix2[n-1][0], matrix2[n-1][1]), matrix2[n-1][2]))
