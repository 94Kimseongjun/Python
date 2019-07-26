# paint.py
from point import Point

p = Point(10, 10)   # 생성자 __init__ 호출
print("P: x={}, y={}".format(p.getX(), p.getY()))
print("Point instance count:", Point.instance_count)

p2 = Point(20, 20)
print("P2: x={}, y={}".format(p2.getX(), p2.getY()))
print("Point instance count:", Point.instance_count)

del p2  # 소멸자 __del__ 호출
print("Point instance count:", Point.instance_count)


print("P1:", p)

#__str__ vs __repr__
print("STR:",str(p)) # __str__ 호출
print("REPR:",repr(p)) # __repr__ 호출

# 객체 p를 전달 받았을 때, 해당 객체가 어떻게 생성되었는가를 확인
rep=eval(repr(p))
print(rep, type(rep))

print(type(p))
# 연산자 오버로딩 테스트
print("p + 10 ?",p + 10) # add 메서드 호출
print(p)
print("p + Point(20, 10) ?", p + Point(20,10))

print("p:",p)
print("p == Point(40, 40)?",p == Point(40, 40))

# 비교 연산자 오버로딩 테스트 ==
print("p:",p)
print("p == Point(40, 30)?",p == Point(40, 40))