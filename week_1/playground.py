l_len = int(input())
l = list(map(int, input().split(' ')))
l.sort()
                                            # 이분 탐색
def search(h):      
    left = 0                                # 맨 왼쪽은 0
    right = l_len - 1                       # 맨 오른쪽은 끝값
    mid = (left + right) // 2               # 중간
    result = 0
    while True:
        if l[mid] == h:                     # 만약 중간값이 구할 값이면
            result = 1                      # 1 리턴
            break
        elif l[mid] < h:                    # 만약 중간값이 구해야하는 값보다 작으면
            left = mid + 1                  # 중간 + 1을 왼쪽으로
        elif l[mid] > h:                    # 만약 중간값이 구해야하는 값보다 크면
            right = mid - 1                 # 중간 - 1을 오른쪽으로
        mid = (left + right) // 2           # 중간값 갱신
        if left > right:                    # 반목문 탈출
            break
    return result

input()
for i in map(int, input().split(' ')):
    print(search(i), end=' ')