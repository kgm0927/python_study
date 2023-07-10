# 클래스 메서드 사용하기

""" 정적 메서드와 비슷하지만 약간의 차이점이 있는 클래스 메서드를 사용해보겠다."""

""" 클래스 메서든느 다음과 같이 메서드 위에 @classmethod를 붙인다. 이때 클래스 메서드는 첫 번째 매개변수에 cls를 지정해야 한다.
    (cls는 class에서 따왔다.)
    
    class 클래스이름:
        @classmethod
        def 메서드(cls,매개변수1,매개변수2):
            코드



    이렇게 해서 사람 클래스 Person을 만들고 인스턴스가 몇 개 만들어졌는지 출력하는 메서드를 만들어보겠다.
    
    """


class Person:
    count=0 # 클래스 속성

    def __init__(self) -> None:
        Person.count +=1 # 인스턴스가 만들어질 때
                         # 클래스 속성 count에 1을 더함


    @classmethod
    def print_count(cls):
        print('{0}명 생성되었다.'.format(cls.count)) # cls로 클래스 속성에 접근



james=Person()
maria=Person()


Person.print_count()    # 2명 생성되었다.





""" 먼저 인스턴스가 만들어질 때마다 숫자를 세야 하므로 __init__ 메서드에서 클래스 속성 count에 1을 더해 준다. 물론 클래스 속성에 접근한다는 것을
    명확하게 하기 위해 Person.count와 같이 만들어준다."""


""" 이제 @classmethod를 붙여서 클래스 메서드를 만든다. 클래스 메서드는 첫 번째 매개변수가 cls인데 여기에는 현재 클래스가 들어온다. 따라서 cls.count처럼
    cls로 클래스 속성 count에 접근할 수 있다.(인스턴스에도 접근이 가능하다.)"""



""" Person으로 인스턴스를 두 개 만들었으므로 print_count를 출력해보면 '2명 생성되었습니다.'가 출력된다. 물론 print_count 클래스 메서드이므로 Person.print_count()
    처럼 클래스로 호출해준다."""



""" 클래스 메서드는 정적 메서드처럼 인스턴스 없이 호출할 수 있다는 점이 같다. 하지만 클래스 메서드는 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용한다."""


""" 특히 cls를 쓰면 메서드 안에서 현재 클래스의 인스턴스를 만들 수 있다. 즉, cls는 클래스이므로 cls()는 Person()과 같다.


        @classmethod
        def create(cls):
        p=cls() # cls()로 인스턴스 생성
        return p

"""

