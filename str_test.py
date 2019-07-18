def test():
    a=23
    print(type(a))


    b = 0b1101
    c = 0o23
    d = 0x23
    print(a,b,c,d)


def int_ex():
    a=2019
    print(a, "is", type(a))
    print(a, "is int?", isinstance(a, int))


    b = 0b1101
    o = 0o23
    h = 0xAB

    print(b,o,h)

def float_ex():
    a=3.141592
    print(a,"is",type(a))
    print(a, "is float?", isinstance(a, float))

    b = 3.0
    print(b, "is", type(b))
    print(b, "is float?", isinstance(b, float))

    print(a.is_integer(), b.is_integer())

    # 지수 표현법
    c = 3e8
    d = -2E-5
    print(c, d)
    print(d == -0.00002) # -2E-5 == -0.00002

def bit_oper():
    # bit not
    print(bin(5), bin(~5))

    # bit and(&), bit or(|)
    a = 0b10101010
    print(bin(a & 0b10))

    # bit shift <<, >>
    bits = 1
    print("bits << 2 :", bin(bits << 2))

def str_ex():
    str3 = """ABCDEFG
        abcdef
        가나다라마바사아
        123456789"""

    print(str3)

    first_name = "Seong Jun"
    last_name = "Kim"
    full_name = first_name +" "+ last_name
    print(full_name)
    print(first_name, last_name)

    laugh = "Ha"
    print(laugh * 3)

    str = "Life is too short, You need Python!"
    print(len(str))
    print(str[2])
    print(str[8:11])
    print(str[-7:-1])
    print(str[5:])

def define_str():
    s1 = "Hello Python"
    s2 = str("Hello Python")
    s3 = str(3.141592)

    print(s1, s2, s3,"\n=========")
    print(s1,"is",isinstance(s1,str))
    print(s2, "is", isinstance(s2, str))
    print(s3, "is", isinstance(s3, str))

    s4 = "I like Python\nI like\tJava Also"
    print(s4)

    # 다중형 문자열
    s5 = """I like Python
I like Java Also
Hi
hahahaha
hello
        """
    print(s5)

    """
    다중행 문자열은 주석으로 활용 가능
    :return:
    """

def string_oper():
    # 문자열은 시퀀스형, 변경불가
    str1 = "First String"
    str2 = "Second String"

    print(str1, "Length:", len(str1))
    print(str2, "Length:", len(str2))

    print(str1[6], str1[7], str1[8])

    print(str1[-6], str1[-5], str1[-4])

    # str1[6] = "s" # TypeError

    #슬라이싱
    print("str1[6:9]:", str1[6:9])
    print("str1[-6:-3]:", str1[-6:-3])


    print("str1[6:]:", str1[6:])
    print("str1[:6]:", str1[:6])





    #포함여부
    print("S" in str1)
    print("S" not in str1)


def search_methods():

    """문자열 검색 관련 예제
    """

    s = "I like Python, I like Java Also"

    print("Count:", s.count("like")) # 문자열 내 검색어 개수
    i=s.find("like")
    print("Find:", i)
    i = s.find("like", i+1)
    print("Find 2nd:",i)
    i = s.find("like", i + 1)
    print("Find 3nd:", i)

    i = s.index("like")
    print("index:", i)
    i = s.index("like",i+1)
    print("index 2nd:", i)
    #i = s.index("like", i + 1) # 검색어가 없으면 ValueError
    #print("index 3nd:", i)

    #rfind 역방향 검색
    i = s.rfind("like")
    print("rfind 1st : ",i)
    i = s.rfind("like", 0, i) # 검색 범위 지정 가능
    print("rfind 2st : ", i)

    # startswith, endswith
    url = "http://www.naver.com"
    surl = "https://www.naver.com"
    ftp = "ftp://ftp.naver.com"

    print(url.startswith("http://")) # url이 http:// 로 시작하는가?
    print(surl.startswith("https://")) # surl이 https:// 로 시작하는가
    print(ftp.endswith("naver.com")) # ftp 가 naver.com으로 끝나는가

    print(url.startswith(("http://", "https://")))

    print("ftp.startswith : ", ftp.startswith("ftp://"))
    print(ftp.startswith("htp://", 3, 10))


def modify_replace_ex():
    s = "      Alice and the Heart Queen     "
    print("STRIP:[", s.strip(), "]", sep="")
    print("LSTRIP:{", s.lstrip(), "]", sep="")
    print("RSTRIP:{", s.rstrip(), "]", sep="")

    s = "*********Alice and the Heart Queen ******"
    print(s.strip("*"))

    # 치환 : replace
    s = "I like Java"
    print("REPLACE:", s.replace("Java", "Python"))

def split_joun_methods():
    s = "Ham and Cheese and Breads and Ketchup"
    print("SPLIT", s.split())
    ingredients = s.split(" and")
    print("재료:", ingredients)

    # 연결 join
    print(" : ".join(ingredients)) #연결 문자를 기준으로 join
    print(s.split(" and ", 2)) # 구분자르 기준으로 2개 추출
    print(s.rsplit(" and ",2 )) # 구분자를 기준으로 뒤에서 2개 추출

    lines = """
    Java is fun
    Python is fun
    Linux is fun?
    """

    print(lines.split())
    print(lines.splitlines())
    print(lines.splitlines(True))


def string_format():
    """
    문자열 포매팅 예제
    :return:
    """
    print("문자열 포매팅 예제")

    # C - Style
    # %s %d %f %o %x

    fmt = "%d개의 %s 중에 %d개를 먹었다."# % (10, "사과", 5)

    print(fmt % (5, "배", 2))

    print("현재 이자율은 %f 입니다." % 1.234)
    print("현재 이자율은 %.2f 입니다." % 1.234)

    # PlaceHolder 방식의 포매팅
    fmt2 = "{}개의 {} 중에 {}개를 먹었다."
    print(fmt2.format(10, "사과", 3))

    fmt3 = "{0}개의 {1}중에 {2}개를 먹었다."
    print(fmt3.format(11, "귤", 5))

    fmt4 = "{total}개의 {fruit} 중에 {eat} 개를 먹었다"
    print(fmt4.format(total=6, fruit="오렌지", eat=1))

    values = {
        "fruit": "오렌지",
        "eat": 5,
        "total": 7
    }

    print(fmt4.format_map(values))

if __name__ == "__main__":
    #int_ex()
    #float_ex()
    #bit_oper()
    #str_ex()
    #define_str()
    #string_oper()
    #search_methods()
    #modify_replace_ex()
    #split_joun_methods()
    string_format()
    # s = "Alice and the Heart Queen"
    #
    # print(s.center(60))
    # print(s.center(60, '-'))
    # print(s.ljust(60, '-'))
    # print(s.rjust(60,'='))
    # print('20'.zfill(5))
    # print('1234'.zfill(5))
