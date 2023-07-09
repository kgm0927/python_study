# 비공개 속성 사용하기

""" 앞에서 만든 Person 클래스는 hello, name, age, address 속성이 있었다. """


class Person:
    def __init__(self,name,age,address) -> None:
        self.hello='안녕하세요.'
        self.name=name
        self.age=age
        self.address=address




""" 이 속성들은 메서드에서 self로 접근할 수 있고, 인스턴스.속성 형식으로 클래스 바깥에서도 접근할 수 있다."""

maria=Person('마리아',20,'서울시 서초구 반포동')

print(maria.name)
# 마리아


""" 이번에는 클래스 바깥에서는 접근할 수 없고 클래스 안에서만 사용할 수 없는 비공개 속성(private attribute)을 사용해보겠다.

    비공개 속성은 '__속성'과 같이 이름이 __(밑줄 두 개)로 시작해야 한다. 단, __속성__처럼 밑줄 두 개가 양 옆에 왔을 때는 비공개 속성이
    아니므로 주의해야 한다.
    
    class 클래스이름:
        def __init__(self,매개변수)
            self.__속성=값
    
    
    """


""" 그럼 Person 클래스에 지갑 속성 __wallet을 넣어보겠다. 다음 내용을 작성해 보도록 하겠다."""


class Person:
    def __init__(self,name,age,address,wallet) -> None:
        self.name=name
        self.age=age
        self.address=address
        self.__wallet=wallet # 변수 앞에 __를 붙여서 비공개 속성으로 만듦


maria=Person('마리아',20,'서울시 서초구 반포동',10000)
# maria.__wallet-=10000 # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함




""" 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있다. 다음과 같이 돈을 내는 pay 메서드를 만들어본다."""

class Person:
    def __init__(self,name,age,address,wallet):
        self.name=name
        self.age=age
        self.address=address
        self.__wallet=wallet # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

    def pay(self,amount)->None:
        self.__wallet-=amount    # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있다.
        print('이제 {0}원 남았네요.'.format(self.__wallet))


maria=Person('마리아',20,'서울시 서초구 반포동',10000)
print(maria.pay(3000))



""" pay는 돈을 내면 해당 금액을 지갑에서 빼도록 만들었다. 이제 지갑에서 돈을 쓸 수 있게 되었다."""


""" 이처럼 비공개 속성은 클래스 바깥으로 드러내고 싶지 않은 값에 사용한다. 즉, 중요한 값인데 바깥에서 함부로
    바꾸면 안 될 때 비공개 속성을 주로 사용한다. 비공개 속성을 바꾸는 경우는 클래스의 메서드로 한정한다. """



# 참고: 공개 속성과 비공개 속성

""" 클래스 바깥에서 접근할 수 있는 속성을 공개 속성(public attribute)이라 부르고, 클래스 안에서만 접근할 수 있는 속성을 비공개 속성이라고 부른다."""






# 참고: 비공개 메서드 사용하기

""" 속성뿐만 아니라 메서드도 이름이 __(밑줄 두 개)로 시작하면 클래스 안에서만 호출할 수 있는 비공개 메서드가 된다."""


class Person:
    def __greeting(self):
        print('Hello')

    def hello(self):
        self.__greeting()   # 클래스 안에서는 비공개 메서드를 호출할 수 있음


james=Person()
# james.__greeting() # 에러: 클래스 바깥에서는 비공개 메서드를 호출할 수 없음


""" 비공개 메서드도 메서드를 클래스 바깥으로 드러내고 싶지 않을 때 사용한다. 보통 내부에서만 호출되어야 하는 메서드를 비공개 메서드로 만든다."""