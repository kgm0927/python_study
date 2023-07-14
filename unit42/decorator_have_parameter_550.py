# 매개변수가 있는 데코레이터 만들기



""" 이런 방식의 데코레이터는 값을 지정해서 동작을 바꿀 수 있다.
    다음은 함수의 반환값이 특정 수의 배수인지 확인하는 데코레이터다."""


def is_multiple(x):                     # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):           # 호출할 함수를 매개변수로 받음
        def wrapper(a,b):               # 호출할 함수의 매개변수와 똑같이 지정
            r=func(a,b)                 # func를 호출하고 반환값을 변수에 저장
            if r%x==0:                  # func의 반환값이 x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수이다.'.format(func.__name__,x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아니다.'.format(func.__name__,x))
            return r                    # func의 반환값을 반환
        return wrapper                  # wrapper 함수
    return real_decorator               # real_decorator 함수 반환




@ is_multiple(3)
def add(a,b):
    return a+b

print(add(10,20))
print(add(2,5))


# add의 반환값은 3의 배수이다.
# 30
# add의 반환값은 3의 배수가 아니다.
# 7
#
#
#


""" 지금까지 데코레이터를 만들 때 함수 안에 함수를 하나만 만들었다. 하지만 매개변수가 있는 데코레이터를 만들 대는 함수를 하나 더 만들어야 한다."""


""" 먼저 is_multiple 함수를 만들고 데코레이터가 사용할 매개변수 x를 지정한다. 그리고 is_multiple 함수 안에서 실제 데코레이터 역할을 하는 real_decorator
    를 만든다. 즉, 이 함수에서 호출할 함수를 매개변수로 받는다. 그 다음에 real_decorator 함수 안에서 wrapper 함수를 만든다."""
"""(즉, 총 3개의 함수가 필요하다.)"""


""" wrapper 함수 안에는 먼저 func의 결과가 데코레이터 매개변수 x의 배수인지 확인한다. 그다음에 func의 반환값을 반환다."""


""" 여기서는 real_decorator, wrapper 함수를 두 개 만들었으므로 함수를 만든 뒤에 return으로 두 함수를 반환해준다.


         return wrapper                  # wrapper 함수
    return real_decorator 
        """


""" 데코레이터를 쓸 때에는 데코레이터에 ()(괄호)를 붙인 뒤 인수를 넣어주면 된다.

    @데코레이터(인수):
    def 함수이름():
        코드"""


""" 여기서는 is_mutliple에 3을 지정해서 add 함수의 반환값이 3의 배수인지 확인했다. 물론 is_multiple에 다른 숫자를 넣으면 함수의 반환값이
    해당 숫자의 배수인지 확인해준다. """






# 참고: 매개변수가 있는 데코레이터 여러 개 지정하기

""" 매개변수가 있는 데코레이터 여러 개 지정할 때는 다음과 같이 인수를 넣은 데코레이터를 여러 줄로 지정해준다.

        @ 데코레이터1(인수)
@ 데코레이터2(인수)
def 함수이름():
    코드

"""



@ is_multiple(3)
@ is_multiple(7)


def add(a,b):
    return a+b


print(add(10,20))

# add의 반환값은 7의 배수가 아니다.
# wrapper의 반환값은 3의 배수이다.
 

""" @을 사용하지 않았을 시는 다음 코드와 동작이 똑같다.
 
 
    decorated_add=is_multiple(3)(is_mutliple(7)(add))
    decorated_add(10,20)
"""


# 참고: 원래 함수 이름이 안나온다면?

""" 데코레이터를 여러 개 사용하면 데코레이터에서 반환된 wrapper 함수가 데코레이터로 들어간다. 따라서 함수의 __name__을 출력해보면
    wrapper가 나온다.
    
    add의 반환값은 7의 배수가 아니다.
    wrapper의 반환값은 3의 배수이다.
    

    함수의 원래 이름을 출력하고 싶다면 functools 모듈의 wraps 데코레이터를 사용해야 한다. 다음과 같이 @functools.wraps에 func를
    넣은 뒤 wrapper 함수 위에 지정해준다(from functools import wraps로 데코레이터를 가져왔다면 @wraps(func)를 지정).
    """


import functools


def is_multiple(x):
    def real_decorator(func):
        @functools.wraps(func)
        def wrapper(a,b):
            r=func(a,b)
            if r%x==0:
                print('{0}의 변환값은 {1}의 배수이다.'.format(func.__name__,x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아니다.'.format(func.__name__,x))
            return r
        return wrapper
    return real_decorator



@ is_multiple(3)
@ is_multiple(7)
def add(a,b):
    return a+b


print(add(10,20))

# add의 반환값은 7의 배수가 아니다.
# add의 변환값은 3의 배수이다.
# 30
#

""" @functools.wraps는 원래 함수의 정보를 유지시켜준다. 따라서 디버깅을 할 때 유용하므로 데코레이션을 만들 때는 @functools.wraps를 사용하는
    것이 좋다."""



