def if_statement():
    """
    if문
    :return:
    """

    """
    키보드로부터 money 입력
    10000원 이상 -> by Taxi
    2000원 이상 -> by bus
    아니면 -> on foot
    """
    money=int(input("Money input:"))
    print(money,type(money))

    message=""
    if money>10000:
        message="By Taxi"
    elif money>2000:
        message="By bus"
    else:
        message="On foot"

    print("가지고 있는 돈 {}, {}".format(money,message))


def if_expr():
    """
    조건 판별 식(Expression)
    :return:
    """

    money = int(input("얼마 가지고 있어?"))
    message="by Taxi" if money >= 10000 \
        else "by Bus" if money >= 2000 else "on foot"

    print("가지고 있는 돈 {money}, {message}".format(money=money,message=message))


def for_ex():
    """
    for문
    :return:
    """
    # 구구단
    # 삼각형 그리기

    # for i in range(2,10):
    #     for j in range(1,10):
    #         print(i, "*", j, "=", i*j)


    for i in range(0,100,2):
        print(i,end=" ")
    else:
        print("루프 정상 종료")


    for i in range(0,100,2):
        if i>50:
            break
        print(i, end=" ")
    else :
        print("루프 정상 종료")



    str="*"
    for i in range(1,5):
             print(str*i)


def while_ex():
    """
    while문으로 구구단, 삼각형, 역삼각형
    :return:
    """

    i=2
    j=1
    while(i<10):
        while(j<10):
            print(i, "*", j, "=", i*j,end="\t")
            j=j+1
        j=1
        i=i+1
        print()


    i=0
    while i < 100:
        print(i, end=" ")
        i+=2
    else:
        print("루프 정상 종료")

    # 의도적 무한 루프
    i=0
    while True:
        if i % 2 != 0:
            i += 1
            continue

        print(i,end=" ")
        i += 1
        if i > 1000:
            break


def list_comp():
    """
    리스트 컴프리헨션
    :return:
    """

    x = range(1,100)
    # 2*x+1 한 리스트로 생성
    result=[]
    for num in x:
        result.append(2*num+1)


    print("RESULT:",result)


    # List Comprehension Syntax
    # [ 표현식 for 항목 in 순차형 객체 ]

    result = [2*num+1 for num in x]
    print("COMP RESULT:",result)


    # 1~99까지의 수 중에서 짝수만
    result = [num for num in range(1,100) if num%2==0]
    print("짝수:", result)

strings = ["a","as","bat","cat","dove","python"]

def set_comp():
    """
    셋 컴프리헨션
    :return:
    """

    # Syntax : { 표현식 for in 순차객체 }
    # 중복 없고, 순서 없음
    # strings 안에서 문자열의 길이가 3글자 이하인 셋을 생성

    filtered_set = { s for s in strings if len(s) <= 3}
    print(filtered_set, type(filtered_set))

def dict_comp():
    """
    딕셔너리 컴프리헨션
    :return:
    """
    # Syntax : { 키표현식:값표현식 for 객체 in 순회가능 객체 }
    lens = {s:len(s) for s in strings}
    print(lens)


if __name__ == "__main__":
    #if_statement()
    #if_expr()
    #for_ex()
    #while_ex()
    #list_comp()
    #set_comp()
    dict_comp()
