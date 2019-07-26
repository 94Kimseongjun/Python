# 파일 모드 정리
# 파일 종류 : t(text, default(t), b(binary)
# 작업 종류 r(read, default(t), w(write), a(append)

def write_text_ex():
    """
    텍스트 파일 저장 예제
    :return:
    """
    f=open("./sample/test.txt","w",encoding="utf-8")
    write_size=f.write("Life is too short, you need Python\n")
    print("write_size",write_size)
    f.close()

def write_text_ex2():
    """with ~ as 를 이용한 자동 리소스 닫기"""
    with open("./sample/test2.txt","w",encoding="utf-8") as f:
        write_size=f.write("Life is too short, you need Python\n")

    # with 블록 종료 이후 자동으로 리소스 해제
    print("f는 열려있나?,",f.close()) # 안전성 확보


def read_text_ex():
    """
    sangbuk.scv를 불러와 출력해보자
    :return:
    """
    f=open("./sample/sangbuk.csv",encoding="utf-8") # read 모드 text 파일 -? 생략가능
    text = f.read()
    print("scv:",text)
    f.close() # 반드시 닫아줍니다

def read_text_ex2():
    """
    한 라인씩 읽어와서 가공
    :return:
    """
    with open("./sample/sangbuk.csv",encoding="utf-8") as f:
        while True: # 몇 라인인지 알 수 없으니 무한 루프
            line=f.readline()
            if not line:
                break
            #print(line)
            info = line.replace("\n","").split(",")
            member={
                "name":info[0],
                "number":info[1],
                "position":info[3]
            }
            members.append(member)


    print("MEMBERS",members)


# 연습문제
# sample 디렉터리 안쪽에 rose-flower.jpeg가 있음
# binary 모드로 열어서
# rose-flower-copy.jpeg로 write 로 해 보기
import pickle

def pickle_dump():
    with open("./sample/players.bin","wb") as f:
        pickle.dump({"baseball":9},f)
        pickle.dump({"soccer": 11}, f)
        pickle.dump({"volleyball": 6}, f)

def pickle_load():
    """
    피클 불러오기
    :return:
    """

    with open("./sample/players.bin","rb") as f: # 반드시 b 모드
       # 파일 내부에 피클이 몇 개 있는지 알 수 없으므로

        while True:
            try:
                print(pickle.load(f))
            except EOFError:
                print("피클은 더이상 없음")
                break




if __name__ == "__main__":
    #write_text_ex() # 텍스트 파일 저장 예제
    #write_text_ex2() # with ~ as 를 이용한 리소스 해제
    #read_text_ex() # 텍스트 파일 read 예제
    #read_text_ex2()
    pickle_dump()
    pickle_load()