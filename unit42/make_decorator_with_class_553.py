# 클래스로 데코레이터 만들기


""" 이번에는 클래스로 데코레이터를 만드는 방법을 알아보겠다. 특히 클래스를 활용할 때는 인스턴스 함수처럼 호출하게 해 주는 __call__ 메서드를 구현해야
    한다. 특히 클래스를 활용할 때는 인스턴스 함수를 호출하게 해 주는
    __call__ 메서드를 구현해야 한다."""


class Trace:
    def __init__(self,func) -> None:            # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func=func                          # 호출할 함수를 속성 func저장

    def __call__(self):
        print(self.func.__name__,'함수 시작') # __name__으로 함수 이름 출력
        self.func()                          # 속성 func에 저장된 함수 호출
        print(self.func.__name__,' 함수 끝')  


@ Trace     # @데코레이터
def hello():
    print('hello')


hello() # 함수를 그대로 호출



""" 클래스로 데코레이터를 만들 때는 먼저 __init__ 메서드를 만들고 호출할 함수를 초깃값으로 받는다. 그리고
    매개변수로 받은 함수를 속성으로 저장한다."""


""" 이제 인스턴스를 호출할 수 있도록 __call__ 메서드를 만든다. __call__ 메서드에서는 함수의 시작을 알리는 문자열을
    출력하고, 속성 func에 저장된 함수를 호출한다. 그다음에 함수의 끝을 알리는 문자열을 출력한다."""


""" 데코레이터를 사용하는 방법은 클로저 형태의 데코레이터와 같다. 호출할 함수 위에 @를 붙이고 데코레이터를 지정하면 된다.



    @데코레이터:
    def 함수이름():
        코드
        
        
    @ Trace     # @ 데코레이터
    def hello():
        print('hello')
        
        


        
    
        





    @ 으로 데코레이터를 지정했으므로 함수는 그대로 호출해준다.
    hello() # 함수를 그대로 호출


    참고로 클래스로 만든 데코레이터는 @을 지정하지 않고 데코레이터 반환값을 호출하는 방식으로도
    확인할 수 있다. 다음과 같이 데코레이터에 호출할 함수를 넣어서 인스턴스를 생성한 뒤 인스턴스를 호출해주면
    된다. 즉, 클래스에 __call__ 메서드를 정의했으므로 함수처럼 ()(괄호)를 붙여서 호출할 수 있다.
        """


def hello():        # @ 데코레이터를 지정하지 않음
    print('hello')

trace_hello=Trace(hello)        # 데코레이터를 호출할 함수를 넣어서 인스턴스 생성
trace_hello()                   # 인스턴스를 호출.__call__ 메서드가 호출됨