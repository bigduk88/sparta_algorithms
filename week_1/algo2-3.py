words = input().upper()                             #입력 받고 대소문자 관계없이 최빈 알파벳을 구하는 것이므로 전부 대문자로 바꿔준다.
word_list = list(set(words))                        #set을 이욯하여 입력받은 문자열에서 중복값을 제거. 알파벳이 몇 번 사용되는지 확인하는데에 사용됨.

count_list = []                                     #입력값에 같은 알파벳이 몇 개 있는지 숫자를 카운트해서 넣는다.
for counting in word_list :                         #
    count = words.count(counting)                   #
    count_list.append(count)                        #

if count_list.count(max(count_list)) > 1 :          #if문으로 알파벳이 사용된 개수 중 가장 큰 수를 찾고 해당 숫자가 1보다 크면 물음표 출력.
    print('?')                                      #최댓값이 하나일 경우 숫자 리스트에서 가장 큰 수의 위치를 index함수로 찾고 word_list
else :                                              # 리스트에서 같은 인덱스에 위치한 문자열을 출력.    
    max_index = count_list.index(max(count_list))   #
    print(word_list[max_index])                     #