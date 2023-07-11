# 예외 만들기


""" 지금까지 파이썬에 내장된 예외를 처리했는데, 이번에는 예외를 직접 만들어서 발생시켜보겠다.
    프로그래메가 직접 만든 예외를 사용자 정의 예제라고 한다."""




""" 예외를 만드는 방법은 간단하다. 그냥 Exception을 상속받아서 새로운 클래스를 만들면 된다. 그리고 __init__ 메서드에서
    기반 클래스의 __init__ 메서드를 호출하면서 에러 메시지를 넣어주면 된다.
    
    class 예외이름(Exception):
        def __init__(self):
            super().__init__('에러페이지')"""


""" 이제 입력된 숫자가 3의 배수가 아닐 때 발생시킬 예외를 만들어보겠다."""


class NotThreeMultipleError(Exception):     # Exception을 상속받아서 새로운 예외를 만듦
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')



def three_multiple():
    try:
        x=int(input('3의 배수를 입력하세요: '))
        if x%3!=0:                          # x가 3의 배수가 아니면
            raise NotThreeMultipleError     # NotThreeMultipleError 예외를 발생시킴
        print(x)

    except Exception as e:
        print('예외가 발생했습니다.',e)


three_multiple()



""" 5를 입력하면 3의 배수가 아니므로 NotThreeMultipleError 예외가 발생한다."""

# 3의 배수를 입력하세요: 5
# 예외가 발생했습니다. 3의 배수가 아닙니다.


""" 먼저 Exception을 상속받아서 NotThreeMultipleError 예외를 만들었다. 그리고 __init__ 메서드 안에서 기반 클래스의 __init_
    메서드를 호출하면서 에러 메시지를 넣었다."""


""" 예외를 발생시킬 때는 raise NotThreeMultipleError와 같이 raise에 새로 만든 예외를 지정해주면 된다.
    참고로 다음과 같이 Exception만 상속받고 pass를 넣어서 아무것도 구현하지 않아도 된다."""

class NotThreeMultipleError(Exception):
    pass

""" 이때는 예외를 발생시킬 때 에러 메시지를 넣어주면 된다.

    raise NotThreeMultipleError('3의 배수가 아닙니다.')"""