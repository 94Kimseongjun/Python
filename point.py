# point.py

class Point:
    instance_count = 0 # 클래스 멤버
                        # 해당 클래스를 기반으로 한 모든 인스턴스에서 공유

    def __init__(self, x=0, y=0): # 생성자, 초기화 코드
        self.x = x
        self.y = y
        Point.instance_count += 1   # 클래스 멤버에 접근

    def __del__(self):  # 소멸자, 정리 코드
        Point.instance_count -= 1

    def __str__(self): # 출력을 위한 코드
        return "Point x={0}, y={1}".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __add__(self, other): # + 연산자
        if isinstance(other, int):
            self.x += other
            self.y += other
        elif isinstance(other,Point):
            self.x += other.x
            self.y += other.y
        else:
            self += other

    def __eq__(self, other):
        print()
        return self.x == other.x and self.y ==other.y


    def setX(self, x):
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y


def bound_class_method():
    p = Point() # 인스턴스 객체 생성
    p.setX(10)
    p.setY(10)

    print(p)


def unbound_class_method():
    p = Point() # 인스턴스 객체 생성
    Point.setX(p, 20)
    Point.setY(p, 20)

    print(Point.getX(p))
    print(Point.getY(p))


if __name__ == "__main__":
    #bound_class_method()
    unbound_class_method()