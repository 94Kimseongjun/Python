i = 0
for value in ['red', 'yellow', 'blue', 'white', 'grey']:
    print('{0}: {1}'.format(i,value))
    i += 1

    # 비교 : enumerate 함수를 사용했을 때
print("=======================")
for i, value in enumerate(['red', 'yellow', 'blue', 'white', 'grey']):
    print('{0}: {1}'.format(i,value))



seq = range(10) # 0이상 10 미만의 순차적 정수 목록
print(seq, type(seq))