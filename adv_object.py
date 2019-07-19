# 글로벌 변수

g_a = 1
g_b = "Python"


# 사용자 정의 함수
def func():
    l_a=2
    l_b="Local"
    print("로컬 심볼 테이블 : ", locals())

    print("g_a" in locals())
    print(g_a)



def symbol_table():
    print("GLOBAL:", globals())
    print(type(globals()))

    print("g_a ?", "g_a" in globals())
    print(type(globals()))

    func()


def object_id():
    # Literal 의 id
    a=10
    b=10
    print("ID a:", id(a))
    print("ID b:", id(b))

    print("id a == id b ? ", id(a)==id(b))
    print("a is b ?", a is b) # is는 동일성의 비교

    #가변형
    lst1=[1,2,3]
    lst2=[1,2,3]
    lst3=lst1

    print("LST1:",lst1,type(lst1))
    print("LST2:", lst1, type(lst2))
    print("LST3:", lst1, type(lst3))

    print("lst1 == lst2:", lst1 == lst2)
    print("lst1 is lst2:", lst1 is lst2)
    print("lst1 == lst3:", lst1 == lst3)
    print("lst1 is lst3:", lst1 is lst3)


def object_copy():
    """
    객체의 복사
    :return:
    """
    a = [1, 2, 3]
    b = [4, 5, 6]
    x = [a, b, 100]

    print("X:", x)

    y = x # 참조 복사 : 심벌 테이블 내 주소값이 동일
    print("Y:",y)

    print("x is y ? ", x is y)
    x[2]=10
    print("y[2] ? :", y[2])

    # Shallow Copy
    # [:]
    import copy

    print("x:",x)

    y=copy.copy(x)

    print("Y:", y)
    print("x is y ? ", x is y) # 복제되었으므로 다른 객체

    x[2]=100
    print("Y:",y)

    print("x[0]:", hex(id(x[0])))
    print("y[0]:", hex(id(y[0])))

    x[0][0] = 2
    print("Y:", y)

    # deepcopy : 내부의 모든 객체를 새로 생성

    print("x:",x)
    y = copy.deepcopy(x) # 재귀적 카피

    print("x[0]:",hex(id(x[0])))
    print("y[0]:", hex(id(y[0])))

    x[0][0]=10
    print("Y:", y)
    print("x is y ? ", x is y)


if __name__=="__main__":
    #func()
    #symbol_table()
    #object_id()
    object_copy()
