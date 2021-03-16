# 1929문제 소수 구하기
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

def isPrime(num):                                   #소수인지 아닌지 판별해주는 함수 정의
    if num==1:                                      #1은 소수가 아니므로 False 리턴
        return False
    else:
        for i in range(2, int(num**0.5)+1):         #소수를 구하려면 2부터 해당숫자의 제곱근 사이의 숫자 중 num과 나누어 0이 되는 수가 있는지 검사.
            if num%i == 0:                          # 제곱근 범위 나누기 법
                return False
        return True                                 

M, N = map(int, input().split())                    

for i in range(M, N+1):                             
    if isPrime(i):                                  
        print(i)                                    