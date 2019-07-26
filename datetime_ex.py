
import datetime # 모듈 임포트

def get_datetime():
    """
    날짜와 시간의 획득
    :return:
    """

    # 현재 날짜
    dt = datetime.datetime.now()
    print("현재 날짜와 시간:",dt)
    print(type(dt))
    print(dt.year, dt.month, dt.day, dt.hour,
          dt.minute, dt.second, dt.microsecond) # 속성접근

     # 생성자를 이용한 날짜 시간 정보의 획득
    # 연 월 일 시 분 초 마이크로 세컨드 순으로 매개변수 부여
    # 단 최소 연 월 일은 필요
    past = datetime.datetime(1999,12,31)
    print("PAST:",past)

    # 요일의 확인 weekday()
    print("오늘은 무슨 요일?",dt.weekday())


    # 날짜 정보의 추출
    nowdate = dt.date() # 날짜 정보 추출
    print("NOWDATE:",nowdate,type(nowdate))

    nowtime=dt.time()
    print("NOWTIME:",nowtime,type(nowtime))

    print(dt>past) #더 최근 시간이 큰 값


def timedelta_ex():
    """
    날짜/시간 차이값 : timedelta 객체
    :return: 
    """

    now = datetime.datetime.now() # 현재
    past = datetime.datetime(1999,12,31) # 과거

    diff = now - past
    print("DIFF:",diff,type(diff))

    # 미래로 가 보기
    days=datetime.timedelta(100,0,0)
    print("DAYS",days)

    print("FUTURE(100일 후):",now+days)


def format_date():
    now=datetime.datetime.now()
    print("now",now)

    #date_str = now

    print("format:",now.strftime("%Y/%m/%d"))


    import locale
    locale.setlocale(locale.LC_ALL, "ko_KR.UTF-8")
    # Windows 로케일 정보가 맞지 않을 때의 처리
    print("format:", now.strftime("%Y년 %m월 %d일"))

    # 문자열로 저장된 날짜 정보를 다시 datetime 형태로 변환

    s= "2012-09-24 14:00"
    dt= datetime.datetime.strptime(s, "%Y-%m-%d %H:%M")
    print("CONWERTED:",dt,type(dt))



if __name__ == "__main__":
    #get_datetime()
    #timedelta_ex()
    format_date()