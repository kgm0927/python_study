# 속성 사용하기

""" 지금까지 클래스에서 메서드를 만들고 호출해보았다. 이번에는 클래스에서 속성을 만들고 사용해본다.
    속성(attribute)을 만들 때는 __init__ 메서드 안에서 self.속성에 값을 할당한다.
    
    
    
    class 클래스이름:
        def __init__(self):
        self.속성=값

        
        """


class Person:
    def __init__(s):
        s.hello='안녕하세요.'
    
    def greeting(self):
        print(self.hello)


james=Person()
james.greeting()
# 안녕하세요


""" Person 클래스의 __init_ 메서드에서 self.hello에 '안녕하세요.' 인사말을 넣었다."""


""" __init 메서드는 james=Person()처럼 클래스에 ()(괄호)를 붙여서 '인스턴스를 만들 때 호출되는 특별한 메서드'이다. 즉,
    __init__(initialize)이라는 이름은 그대로 인스턴스(객체)를 초기화한다."""


""" 특히 이렇게 앞뒤로 __(밑줄 두 개)가 붙은 메서드는 파이썬이 자동으로 호출해주는 메서드인데 스페셜 메서드(special method) 또는 매직 메서드
    (magic method)라고 한다. 앞으로 파이썬의 여러 가지 기능을 사용할 때 이 스페셜 메서드를 채우는 식으로 사용한다."""



""" self는 무엇인가? self는 인스턴스 자기 자신을 의미한다. 우리는 인스턴스가 생성될 때 self.hello='안녕하세요.' 처럼 자기 자신에
    속성을 추가하였다. 여기서 __init__의 매개변수 self에 들어가는 값은 Person()이라 할 수 있다. 그리고 self가 완성된 뒤 james에 할당을 한다.
    이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어온다. 그래서 greeting 메서드에서 print(self.hello)처럼 속성을 출력할 수
    있었던 것이다."""



# 인스턴스를 만들 때 값 받기

""" 클래스로 인스턴스를 만들 때 값을 받는 방법을 알아보겠다. 다음과 같이 __init__ 메서드에서 self 다음에 값을 받을 매개변수를
    지정한다. 그리고 매개변수를 self.속성을 넣어준다.
    
    
    class 클래스이름:
        def __init__(self, 매개변수1, 매개변수2):
        self.속성1=매개변수1
        self.속성2=매개변수2
    
    """


""" 그럼 Person 클래스로 인스턴스를 만들 때 이름, 나이, 주소를 받아본다."""

class Person:
    def __init__(self,name,age,address):
        self.hello='안녕하세요.'
        self.name=name
        self.age=age
        self.address=address

    def greeting(self):
        print('{0} 저는 {1} 입니다.'.format(self.hello,self.name))






maria=Person('마리아',20,'서울시 서초구 반포동')
maria.greeting()
# 안녕하세요. 저는 마리아 입니다.

print('이름:',maria.name)
print('나이:',maria.age)
print('주소:',maria.address)

# 이름: 마리아
# 나이: 20
# 주소: 서울시 서초구 반포동


""" __init__ 메서드를 보면 self 다음에 name,age,address를 지정한다. 그리고 메서드 안에서는 self.name=name 처럼 매개변수를 그대로 self에 넣어서
    속성으로 만든다."""


""" greeting 메서드는 인사를 하고 이름을 출력하도록 수정했다. 물론 name 속성에 접근할 때는 self.name처럼 사용한다.
    
    
    클래스 안에서 속성에 접근할 때는 self.속성 형식이었다. 클래스 바깥에서 접근할 때는 인스턴스.속성 형식으로 접근한다. 다음과 같이 maria.name, maria.age,
    maria.address의 값을 출력해보면 Person으로 인스턴스를 만들 때 넣었던 값이 출력이 된다.
    
    
    이렇게 인스턴스를 통해 접근하는 속성을 '인스턴스 속성'이라 한다."""










# 참고: 클래스의 위치 인수, 키워드 인수


""" 클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수를 사용할 수 있다. 규칙은 함수와 같다. 위치 인수와 리스트 언패킹을 사용하려면 다음과 같이
    *args를 사용하면 된다. 이때 매개변수에서 값을 가져오려면 args[0]처럼 사용해야 한다."""

class Person:
    def __init__(self,*args):
        self.name=args[0]
        self.age=args[1]
        self.address=args[2]

maria=Person(*['마리아',20,'서울시 서초구 반포동'])


""" 키워드 인수와 딕셔너리 언패킹을 사용하려면 다음과 가팅 **kwargs를 사용하면 된다. 이때 매개변수에서 값을 가져오려면 kwargs['name']처럼 사용해야
    한다."""


class Person:
    def __init__(self,**kwargs):
        self.name=kwargs['name']
        self.age=kwargs['age']
        self.address=kwargs['address']

maria1=Person(name='마리아',age=20,address='서울시 서초구 반포동')
maria2=Person(**{'name':'마리아','age':20,'address':'서울시 서초구 반포동'})



# 참고: 인스턴스를 생성한 뒤 속성 추가하기. 특정 속성만 허용하기


""" 지금까지 클래스의 인스턴스 속성은 __init__ 메서드에서 추가한 뒤 사용했다. 하지만 클래스로 인스턴스를 만든 뒤에도 '인스턴스','속성=값' 형식으로
    속성을 계속 추가할 수 있다. 다음 Person 클래스는 빈 클래스이지만 인스턴스를 만든 뒤 name 속성을 추가한다."""


class Person:
    pass

maria=Person()  # 인스턴스 속성
maria.name1='마리아'    # 인스턴스를 만든 뒤 속성 추가
print(maria.name1)


""" 이렇게 추가한 속성은 해당 인스턴스에만 생성된다. 따라서 클래스로 다른 인스턴스를 만들었을 때는 추가한 속성이 생성되지 않았다."""


james=Person()  # james 인스턴스 생성
#james.name      # maria 인스턴스에만 name 속성을 추가했으므로 james 인스턴스에는 name 속성이 없음




""" 인스턴스는 생성한 뒤에 속성을 추가할 수 있으므로 __init__ 메서드가 아닌 다른 메서드에서도 속성을 추가할 수 있다. 단, 이때는 메서드를 호출해야
    속성이 생성이 된다."""


class Person:
    def greeting(self):
        self.hello='안녕하세요.'    # greeting 메서드에서 hello 속성 추가


maria=Person()
#maria.helle # 아직 속성이 없음


maria.greeting()    # greeting 메서드를 호출해야
print(maria.hello )        # hello 속성이 생성됨




""" 인스턴스는 자유롭게 속성을 추가할 수 있지만 특정 속성만 허용하고 다른 속성은 제한하고 싶을 수도 있다. 이때는 클래스에서 __slots__에 허용할
    속성 이름을 리스트로 넣어주면 된다. 특히 속성 이름은 반드시 문자열로 지정해준다.
    
    
    * __slots__=['속성이름1','속성이름2']
    
    
    """


class Person:
    __slots__=['name','age']


maria=Person()
maria.name='마리아'                     # 허용된 속성
maria.age=20                            # 허용된 속성 
# maria.address='서울시 서초구 반포동'    # 허용되지 않은 속성은 추가할 때 에러가 발생함




