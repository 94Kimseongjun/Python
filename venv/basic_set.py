evens = {2,4,6,8,10} # 짝수 집합
odds = {1,3,5,7,9}
numbers={1,2,3,4,5,6,7,8,9,10}
mthree={3,6,9}


def define_set():
    """
    세트의 정의 연습
    :return:
    """

    empty = set()
    empty = {}
    print(type(empty))


    # 세트는 길이 구할 수 있고, 포함여부(in, not in)
    # 순서 없음 인덱스, 슬라이싱은 불가

    print(numbers, "LENGTH:",len(numbers))
    print(2 in numbers, 3 in odds)

    # s="Python Programming Java"
    # words=set(s.upper().split)
    # print("WORDS:", words, "LENGTH:",len(words))

    lst=["Python","Java", "Python", "Linux", "Java"]
    filtered = set(lst)
    print(filtered)

def set_methods():
    """
    세트의 메서드들
    :return:
    """
    print("전체 집합:",numbers)

    numbers.add(12)
    print(numbers)

    #요소의 삭제
    evens.add(3)
    evens.remove(3)
    print("EVENS:",evens)

    #evens.remove  # keyerror -> remove는 없을 경우 error
    evens.discard(3) # 없어도 에러는 없음
    numbers.update({11,13})
    print(numbers, type(numbers))

def set_oper():
    """
    집합 연산
    :return:
    """
    print("전체 집합:", numbers)
    print("짝수 집합:",evens)
    print("홀수 집합:",odds)
    print("3의 배수 집합:",mthree)

    # 합 집합
    print("짝홀 합 집합:",evens|odds==numbers)
    print("짝홀 합 집합:", evens.union(odds) == numbers)

    # 차 집합
    print("전체 차집합 짝수",numbers-evens==odds)
    print("전체 차집합 짝수",numbers.difference(evens)==odds)


    # 교 집합
    print("홀수 교 3배수:",odds&mthree)
    print("홀수 교 3배수:",odds.intersection(mthree))


    # 모 집합
    print("evens은 numbers의 부분집합?:",evens.issubset(numbers))
    print("number는 odds의 모집합?:",numbers.issuperset(odds))


if __name__ == "__main__":
    #define_set()
    #set_methods()
    set_oper()