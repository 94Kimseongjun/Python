def define_list():
    """
    리스트 정의 예제
    리스트 : 순차형, Mutable, Container
    :return:
    """

    list1 = list()
    print(list1, type(list1))
    list2 = [1, "Python", True, [1, 2, 3]]
    print(list2, type(list2))



def list_oper():
    """
    리스트 연산
    :return:
    """

    lst = [1, "Python", True]
    print("Len:", len(lst))
    print(lst[0], lst[1], lst[2])
    print(lst[-1], lst[-2], lst[-3])

    print("list[1:3] : ", lst[1:3]) # 항상 끝 경계에 유의
    print("lst[1:] : ", lst[1:])
    print("lst[:3] : ", lst[:3])
    print("lst[:] : ", lst[:])


    # 단순 카피
    copy = lst[:]
    print("COPY:", copy)
    print("copy is lst?", copy is lst)

    # 연결
    print(lst+ ["Java", False, 3.141592])
    print("lst : ", lst)


    # oppend, extend
    copy.append(["Java", False, 3.141592])
    print("append : ", copy)
    copy = lst[:]
    copy.extend(["Java", False, 3.141592])
    print("Extend : ", copy)


    # insert : 삽입
    copy.insert(2,[1, 2, 3])
    print("insert : ", copy)

    # in, not in : 포함 여부
    print("IN:", "Python" in copy)

    # index : 특정 항목의 인덱스 반환
    print("INDEX:", copy.index("Python"))

    if "Linux" in copy:
        print(copy.index("Linux"))
        print(copy)
    else:
        print("Not Found")


    # 삭제
    print("copy:", copy)
    del copy[2]
    print("copy:", copy)

    # 변경 가능 시퀀스


    #슬라이싱
    lst = [1, 12, 123, 1234, 12345]
    print("lst:", lst, type(lst))


    copy = lst[:]
    # 슬라이싱을 이용한 삽입
    print("ORGINAL:", copy)
    copy[2:2] = [456, 4567]
    print("RESULT:", copy)


    #삭제
    # 아래 코드는 주의 : 뒤부터 지우세요
    #del copy[2]
    #del copy[3]

    copy[2:4] = [] # 슬라이싱을 이용한 삭제
    print("RESULT:", copy)

    # 슬라이싱을 이용한 치환

    copy[2:4] = ["Python", "Linux", "C"]
    print("RESULT : ", copy)



def sort_method():
    """
    sort ex
    :return:
    """

    lst = [10, 2, 22, 9, 8, 23, 4, 12]
    print("원본:", lst)
    lst.reverse() # 순서 뒤집기
    print("reverse():", lst)

    copy=lst.copy()
    print("copy:",copy)
    print("SORTED 함수:",sorted(copy)) #sorted함수는 원본 변경 x
    print("copy:",copy)
    print("SORTED DESC:", sorted(copy,reverse=True))
    print("SORTED key str:",sorted(copy,key=str))

    #key 함수의 정의

    def key_func(val):
        return val % 3


    print("SORTED custom key func:", sorted(copy,key=key_func))



def stack_ex():

    stack = []
    stack.append(40)
    stack.append(30)
    stack.append(20)
    stack.append(10)
    print("STACK:", stack)

    stack.pop()
    print("STACK:", stack)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    if len(stack)>0:
        print("STACK:", stack)
    else:
        print("Empty")


def queue_ex():
    """리스트를 활용한 Queue 구조
    """

    queue = [1, 2]
    queue.append(3)
    queue.append(4)
    queue.append(5)
    print("QUEUE:",queue)

    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))

    if len(queue):
        print(queue.pop(0))
    else:
        print("Empty")


def loop():
    """
    리스트 순회 예제
    :return:
    """

    # words 안의 단어를 모두 소문자로 바꿔 리스트로 변경
    words = "Life is too short, You need to Python".lower().split()
    print(words)





if __name__ == "__main__":
    #define_list()
    #list_oper()
    #sort_method()
    #stack_ex()
    #queue_ex()
    loop()
