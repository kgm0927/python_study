# 데코레이터 만들기

""" 데코레이터는 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용한다. 예를 들어서 함수의 시작과 끝을 출력하고 싶다면 다음과 같이 함수 시작,
    끝부분에 print를 넣어 주어야 한다."""



def hello():
    print('함수 시작')    
    print('hello')
    print('함수 시작')

def world():
    print('함수 시작')    
    print('hello')
    print('함수 시작')

hello()
world()



print()

""" 하지만 이런 경우에는 데코레이터를 활용하면 편리하다. 다음은 함수의 시작과 끝을 출력하는 데코레이터이다."""

def trace(func):                            # 호출할 함수를 매개변수로 받음
    def wrapper():                          # 호출할 함수를 감싸는 함수
        print(func.__name__,'함수 시작')    # __name__으로 함수 이름 출력
        func()                              # 매개변수로 받은 함수를 호출
        print(func.__name__,'함수 끝')
    return wrapper                          # wrapper 함수 반환

def hello():
    print('hello')

def world():
    print('world')


trace_hello=trace(hello)        # 데코레이터에 호출할 함수를 넣음
trace_hello()                   # 반환된 함수를 호출

trace_world=trace(world)        # 데코레이터에 호출할 함수를 넣음
trace_world()                   # 반환된 함수를 호출



""" hello와 world 함수의 시작과 끝이 출력되었다. 먼저 데코레이터 trace는 호출할 함수를 매개변수로 받는다
    (trace는 추적하다라는 뜻으로 프로그래밍에서 함수의 실행 상황을 추적할 때 trace라는 말을 사용한다)."""


""" trace 함수 안에서는 호출할 함수를 감싸는 함수 wrapper를 만든다."""


""" 이제 wrapper 함수에서는 함수의 시작을 알리는 문자열을 출력하고, trace에서 매개변수로 받은 func를 호출한다.
    그 다음에 함수의 끝을 알리는 문자열을 출력한다. 여기서 매개변수로 받은 함수의 원래 이름을 출력할 때는 __name__
    속성을 활용한다. 마지막으로 wrapper 함수를 다 만들었으면 return을 사용하여 wrapper 함수 자체를 반환한다."""


""" 즉 함수 안에서 함수를 만들고 반환하는 클로저인 셈이다."""

""" 데코레이터를 사용할 때는 trace에 함수를 호출할 함수 hello 또는 world를 넣는다. 그 다음에 데코레이터에서 반환된 함수를 호출한다. 이렇게
    하면 데코레이터에 인수로 넣은 함수를 호출하고 시작과 끝을 출력한다."""


""" 물론 trace에 다른 함수를 넣은 뒤 반환된 함수를 호출하면 해당 함수의 시작과 끝을 출력할 수 있다."""





# @으로 데코레이터 사용하기

""" 다음과 같이 호출할 함수 위에 @데코레이터 형식으로 지정한다.

    @데코레이터
    def 함수이름():
        코드
        
"""
print()
print()


def trace(func):                                # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__,'함수 시작')         # __name__으로 함수 이름 출력
        func()                                  # 매개변수로 받은 함수를 출력
        print(func.__name__,'함수 끝')          
    return wrapper                              # wrapper 함수 반환



@ trace
def hello():    # @데코레이터
    print('hello')

@ trace
def world():    # @데코레이터
    print('world')


hello()         # 함수를 그대로 호출
world()         # 함수를 그대로 호출

""" hello와 world 함수 위에 @trace를 붙인 뒤에 hello와 world 함수를 그대로 출력하면 된다."""


""" 물론 다른 함수 위에 @trace를 붙인 뒤 함수를 호출하면 해당 함수의 시작과 끝을 출력할 수 있다."""

""" 이 원리를 말로 설명하겠다. 함수 trace는 함수를 매개변수로 삼는다. @데코레이터를 hello 와 world 함수에서 사용할 시
    hello와 world는 trace의 인자가 된다. 그래서 trace 안에 있는 함수 wrapper에서 func()를 실행하도록 한다."""


""" 이렇게 데코레이터는 함수를 감싸는 형태로 이루어져 있다. 따라서 데코레이터는 기존 함수를 수정하지 않으면서 추가 가능을 구현할 때 사용한다."""




# 참고: 데코레이터 여러 개 지정하기


""" 함수에는 데코레이터 여러 개 지정할 수 있다. 다음과 같이 함수 위에 데코레이터를 여러 줄로 지정해준다. 이때 데코레이터가 실행되는 순서는 위에서
    아래 순이다.
    
    
    @ 데코레이터1
    @ 데코레이터2
    def 함수이름():
        코드
    
    
    """


def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper


def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper




@ decorator1
@ decorator2
def hello():
    print('hello')



hello()
# decorator1
# decorator2
# hello
#
#

