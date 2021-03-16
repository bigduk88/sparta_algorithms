## 4344번

c = int(input()) # 반 개수
sp_list = list() # 학생수n 점수
i = 0

while True:
        sp_list = map(int, input().split()) #map 함수 활용하여 int 값으로 입력 받기
        sp_list = list(sp_list)
        avr = sum(sp_list[1:])/sp_list[0] # 점수 총 합[1:] / 학생수([0]) 평균 구하기
        count = 0
        for p in sp_list[1:]:
                if p > avr: # 점수(p)가 평균보다 높다면
                        count += 1 # count += 1
        print('%.3f'%(count/sp_list[0]*100) + '%') # 소수점 3째 자리 까지 출력. 평균 이상인 학생 수(count) / 전체 학생수([0])
        i = i +1
        if i == c: # 반 개수와 반복문 횟수가 같아 질 때 까지 반복.
                break


