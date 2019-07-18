def define_dict():
    """
    사전정의
    :return:
    """

    dct=dict()
    print(dct,type(dct))

    # Literal을 이용한 정의
    dct={"basketball":5,"baseball":9}

    # key 값을 이용한 접근
    # index, 슬라이싱, 연결, 반복 불가
    # len, in, not in (key) 가능

    dct['volleyball']=6
    print(dct)


    # 키워드 인자값을 이용한 생성
    d1 = dict(one=1,two=2)
    print("키워드 인자 생성:",d1)

    # 튜플의 리스트를 이용한 생성
    d2 = dict([('k1',1),("k2",2),("k3",3)])
    #print(d2,type(d2))

    print(dct.keys())
    print(dct.values())
    print(dct.items()) # key, value 쌍 튜플의 목록

    print("basketball" in dct)
    print(9 in dct)

    print(9 in dct.values())

    #zip 객체를 이용한 생성

    keys = ['one', 'two', 'three']
    values= [1, 2, 3]

    print("ZIP:",zip(keys,values))
    d2 = dict(zip(keys, values))
    print(d2)


def using_dict():
    """
    사전 사용법
    :return:
    """

    phones = {"홍길동":"010-1234-5678",
              "장길산":"010-1111-2222",
              "전우치":"010-7766-2211"}

    print("phones keys : ", phones.keys())
    print(phones, type(phones))

    phones['임꺽정']="010-9999-9999"
    print(phones)

    #print(phones['둘리']) #키가 없으면 오류
    print(phones.get("둘리")) #키가 없으면 None
    print(phones.get("둘리","누구?"))

    # 삭제 del
    del phones['장길산']
    print(phones)

    # 키 값이 없을 때의 삭제
    if '둘리' in phones:
        del phones['둘리']
    else:
        print("없습니다.")

    # pop, popitem
    data = phones.pop('홍길동')
    print(data)
    print(phones)


def loop():
    """
    사전의 loop
    :return:
    """
    phones = {"홍길동": "010-1234-5678",
              "장길산": "010-1111-2222",
              "전우치": "010-7766-2211"}


    # 기본 적인 루프
    for key in phones:
        print(key) # key 값 출력

    # 키, 값 쌍 튜플을 받아와서 사용

    for item in phones.items():
        print("KEY:",item[0], "Value:", item[1])


    # 언 패킹 이용
    for key, value in phones.items():
        print("KEY:",key, "Value:", value)




if __name__ == "__main__":
    #define_dict()
    #using_dict()
    loop()

