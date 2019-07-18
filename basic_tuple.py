def define_tuple():
    """
    튜플 생성 예제
    :return:
    """

    t=tuple() #공튜플
    t=() # 공튜플

    #print(type(t))

    #타 순차 객체를 이용해서 생성
    t=tuple([1,2,3,4])

    # 순차 자료형, imutable
    # 인덱스 접근, 슬라이싱, in, not in
    print(t[-1], t[0],t[1]) # 인덱스 접근
    # t[0] = 10 #치환 불가

    #t=()
    t=(1,) # 요소가 하나인 튜플 작성시, 반드시 마지막에
    print(t)
    print(type((1)),type((1,)))


def tuple_methods():
    """튜플의 메서드"""

    t=[10,20,30,40,20]
    print(t.index(20))
    print(t.index(20,2))
    print(t.count(20))



def packing_unpacking():
    """
    튜플의 패킹과 언패킹
    :return:
    """

    t= 10,20,30,"Python" #packing
    print(t,type(t))

    a,b,c,d=t
    print("Unpacking", a,b,c,d)
    a, *b = t # 앞에서 한 개를 언패킹 ->a,
    print(a,b)

    a, *b, c = t
    print(a, b, c)





if __name__ == "__main__":
    #define_tuple()
    #tuple_methods()
    packing_unpacking()