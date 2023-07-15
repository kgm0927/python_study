# 모듈과 시작점 알아보기


""" 인터넷이 있는 파이썬 코드를 보다 보면 if __name__=='__main__'으로 시작하는 부분을 자주 만나게 된다."""


""" 이 코드는 현재 스크립트 파일이 실행되는 상태를 파악하기 위해 사용한다.

    먼저 __name__부터 알아보겠다. 다음 내용을 unit48 폴더 안에 hello.py 파일로 저장한다."""



""" 그리고 현재 이 파일에 저장하여 실행한다."""

import hello    # hello 모듈을 가져옴

print(' find_module_and_startpoint.py __name__:',__name__)

# hello 모듈 시작
# hello.py __name__: hello
# hello 모듈 끝
# find_module_and_startpoint.py __name__: __main__

""" 실행을 해 보면 hello.py 파일과 find_module_and_startpoint_586.py 파일의 __name__ 변숫값이 출력된다.
    
    파이썬에서 import로 모듈을 가져오면 해당 스크립트 파일이 한 번 실행된다. 따라서 hello 모듈을 가져오면
    hello.py 안의 코드가 실행이 된다. 따라서 hello.py의 __name__ 변수에는 'hello'가 들어가고 find_module_and_startpoint_586.py의
    __name__ 변수에는 '__main__'이 들어간다. (여기서 알아야 할 것은 파일이 실행되는 주체가 무엇인지에 따라 '__main__'이 달라진다.
    이는 즉 최초의 시작점이라는 의미이다.)
"""

""" 즉, __name__은 모듈의 이름이 저장되는 변수이며 import로 모듈을 가져왔을 때 모듈의 이름이 들어간다. 하지만 파이썬 인터프리터로 스크립트
    파일을 직접 실행했을 때는 모듈의 이름이 아니라 '__main__'이 들어간다.
    
    (참고로 __name__과 __main__을 헷갈려서는 안된다. 같은 네 글자에 알파벳 모양이 비슷해서 헷갈리기가 쉽다.)
"""

""" if__name__=='__main__': 처럼 __name__ 변수의 값이 '__main__'인지 확인하는 코드는 현재 스크립트 파일이 프로그램의 시작점이 맞는지
    판단하는 작업이다. 즉, 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도이다."""





# 스크립트 파일로 실행하거나 모듈로 사용하는 코드 만들기

""" 그럼 스크립트 파일을 그대로 실행할 수도 있고, 모듈로도 사용할 수 있는 코드를 만들어보겠다. 다음 내용을 프로젝트 폴더 안에 이 파일로
    저장한 뒤 실행해본다."""


def add(a,b):
    return a+b


def mul(a,b):
    return a*b

if __name__=='__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
    print(add(10,20))
    print(mul(10,20))

# 30
# 200


""" IDLE에서 실행하거나 python calc.py와 같이 파이썬 인터프리터로 실행하면 10,20의 합고 곱이 출력이된다.
    즉, 프로그램의 시작점일 때는 if__name__=='__main__': 아래의 코드가 실행이 된다."""