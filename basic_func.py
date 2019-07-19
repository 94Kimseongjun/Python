# 주로 함수 인수 다루기를 중심으로

def sum(a,b):
    return a+b

def multiply(a,b=2): # a * b
    return a*b


print(multiply(10))
print(multiply(10,4))


def area(width,height):
    return width * height

print("4 * 6의 면적",area(4,6)) # width = 6, height = 4
print("4 * 6의 면적(키워드):",area(height=6,width=4))

def get_total(*args):
    print("ARGS:",args)

    total=0
    for i in args:
        total+=i

    return total

def get_total2(*args,**kwd):

    option1 = kwd.get("option1",None)
    print("옵션 인자:",option1)
    total = 0
    for i in args:
        if isinstance(i,(int, float)):
            total += i

    return total

print(get_total(1, 2))
print(get_total(1,2,3))
#print(get_total(1,2,"python",3,4))
print("get_total2: ",get_total2(1,2,"python",3,4,option1=True,option2="옵션"))

# 확장 연습
# 안쪽에 리스트나 튜플이 있으면
# 리스트 튜플 내부의 합산 가능한 int, float도 함께 합산


# 함수도 객체다 (1급 시민)
def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def calc(a,b,*func): # 함수를 가변 인자로 받음
    for f in func:
        if callable(f): # 함수 인가?
            print(f(a,b))

print("============")
calc(10,20,plus)

# Lambda
calc(10,20,lambda a, b : a * b) # 일회성 함수 주입

# Lambda 함수를 이용한 리스트 소트 키 변경
strings = "Life is too short, you need python"\
    .upper().replace(",","").split()
print(strings)
strings.sort(key=lambda  s:len(s))
print(strings)


