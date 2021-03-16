'''
11050문제 - 이항계수 1
자연수 과 정수 가 주어졌을 때 이항 계수 
를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 10, 0 ≤  ≤ )

출력
(N) 
(K)
를 출력한다. = n!/r!(n-r)! = nCr
'''

N, K = list(map(int, input().split()))

up = 1
for i in range(N, N-K, -1):                 # N에서 N-K 까지 -1씩 감소한다
    up *= i                                 # up에 i곱한다. n!/r!(n-r)! 중 n! 부분

down = 1                                    #
for i in range(1, K+1):                     # 1부터 k+1까지 
    down *= i                               # down에 i를 곱한다. n!/r!(n-r)! 중 r!(n-r)! 부분

print(up // down)                           # n!/r!(n-r)!