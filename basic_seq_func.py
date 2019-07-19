def using_range():
    """
    범위 객체
    :return:
    """

    # 순차형, 변경 불가
    # len, in, not in
    # 인덱스 접근, 슬라이싱
    r = range(10) # 인자값 1개 -> end, 10은 포함되지 않는다
    print(r,type(r))

    r = range(0, 100, 2)
    print(r, "LENGTH:", len(r))
    print(r[19])
    print("포함된 내용",list(r))

    # for loop 에서 사용

    for num in r:
        print(num, end=" ")


def using_zip():
    """
    zip 객체
    :return:
    """
    english= "SUN", "MON", "TUE", "WED" # 4개 짜리 튜플
    korean = "일", "월", "화", "수", "목", "금" # 6개 짜리 튜플

    engkor = zip(english, korean)
    print(engkor, type(engkor))


    # loop
    for item in engkor:
        print(item[0], item[1])

    print("=====================")

    for eng, kor in engkor:
        print("ENG:", eng, "KOR:", kor)




def using_enumerate():
    """
    enumerate 함수
    순차 자료형에서 자료 추출시 인덱스가 함께 필요할 때
    :return:
    """

    items = ["Python", "Java", "Linux", "C"]

    for item in items:
        print(item, end=" ")

    print()

    print(enumerate(items))



    # enumerate 를 이용한 loop
    for item in enumerate(items):
        print(item)

    for index, value in enumerate(items):
        print("{0}번째 항목={1}".format(index, value))


if __name__=="__main__":
    #using_range()
    using_zip()
    #using_enumerate()
