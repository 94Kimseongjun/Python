def handling_exception():
    """
    예외 ㅓ리 연습
    :return:
    """
    lst=[]
    try:
        # 오류 발생 가능 코드 블록을 try
        #lst[3]=1
        4/2
        int("1234")
    except IndexError as e:
        print("인덱스 범위 오류")
        print("Error:", e, type(e))
    except ZeroDivisionError as e:
        print("0으로는 나눌 수 없습니다.")
        print("Error:", e, type(e))
    except ValueError as e:
        print("정수 변환 실패")
        print("오류:",e,type(e))
    except  Exception as e:
        """ Exception은 모든 오류를 처리하기 때문에
         가장 마지막 except로 사용한다 ( 순서 유의 ) """
        print("Error")
        print("Error:",e,type(e))
    else: # 예외 없이 블록이 수행되었을 때
        print("정상 실행 완료")
    finally:
        print("예외 처리 완료")



def raise_exception():
    """
    강제 예외 발생 예제
    :return:
    """
    def beware_dog(animal):
        """
        만약 animol == "dog" 면 출입 제한
        아니면 "어서오세요"
        :param animal:
        :return:
        """
        if animal=="dog":
            # 예외 발생 : raise
            raise RuntimeError("강아지는 출입을 제한합니다.")
        else:
            print("어서 오세요:",animal)
    try:
        beware_dog("cat")
        beware_dog("cow")
        beware_dog("dog") # 내부에서 raise로 강제 예외 발생
    except RuntimeError as e:
        print(e,type(e))
    finally:
        print("예외 처리 완료")


if __name__ == "__main__":
    #handling_exception()
    raise_exception()