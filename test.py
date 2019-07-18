

def arith_open():
    print("==산술연산")
    print(7/3)
    print(7//3)
    print(7%3)

    print(7**3)
    print(pow(7,3))
    print(divmod(7,3))
    print("=====================")
    print(divmod(7,3)[0])
    print(divmod(7, 3)[1])



def complex_ex():
    print("===== 복소수")
    print(3+4j)
    print(3 + 4j.real)
    print(3 + 4j.imag)
    print(3 + 4j.conjugate())

def assigment_ex():
    a=1
    b=a+1
    print(a,b)
    c,d=3,5
    print(c,d)
    x=y=z=10

    print(x,y,z)

    c, d = d, c
    print("swap", c, d)

    #동적 타이핑
    a=1
    print(a, "is", type(a))
    a = "Ptthon"
    print(a, "is", type(a))

    print("a는 str 객체?", isinstance(a, str))

    total=0
    a="Python"
    if isinstance(a, (int, float)):
        total += a

    print("total = ", total)

def var_ex():
    import keyword
    print(keyword.kwlist)

    print("break" in keyword.kwlist)

def logical_oper():
    a = 20; b = 30
    print(not a < b)
    print(a < b and a != b)
    print(a == b or a != b)
    c = True

    print(c, "is", type(c))
    print(isinstance(c, bool))
    print(isinstance(c, int))

    print("-----------bool 캐스팅")
    print(bool(10), bool(0))
    print(bool(3.14), bool(0))
    print(bool("Python"), bool(""))
    print(bool([1, 2, 3]), bool([]))

if __name__=="__main__":
    #arith_open()
    #print(")))))))))))))))))))))))")
    #complex_ex()
    #var_ex()
    #assigment_ex()
    logical_oper()