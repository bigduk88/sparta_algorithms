# 2869문제 달팽이는 올라가고 싶다
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)
# 출력
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

# def totalday(a, b, v):
#     dh = a-b
#     td = v-dh
#     td = v/dh
#     print(int(td))
# print(totalday(3, 2, 10))

# a,b,v = map(int,input().split())
# td = v/(a-b)
# print(td)

a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1) # if 문은 올림을 하기위해 사용함.

# a,b,v=map(int,input().split())
# print(1-(v-a)//(b-a))