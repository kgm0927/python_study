# 코루틴에 값 보내기


""" 코루틴은 제너레이터의 특별한 형태이다.

    제너레이터는 yield로 값을 발생시키지만 코루틴은 yield로 값을 받아올 수 있다. 다음과 같이 코루틴에 값을 보내면서 코드를 실행할 때는 
    send 메서드를 사용한다. 그리고 send 메서드가 보낸 값을 받아오려면 (yield) 형식으로 yield를 괄호로 묶어준 뒤 변수에 저장한다.
    
            * 코루틴객체.send(값)
            * 변수=(yield)
            
"""

def number_coroutine():
    while True:         # 코루틴을 계속 유지하기 위해 무한 루프 사용
        x=(yield)       # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
        print(x)

co=number_coroutine()
next(co)                # 코루틴 안의 yield까지 코드 실행(최초 실행)


co.send(1)              # 코루틴에 숫자 1을 보냄
co.send(2)              # 코루틴에 숫자 2을 보냄
co.send(3)              # 코루틴에 숫자 3을 보냄


""" 먼저 코루틴 number_corountine은 while True: 로 무한히 반복하도록 한다. 왜냐하면 코루틴을 종료하지 않고 계속 유지시키기 위해
    무한 루프를 사용한다.
    
    그리고 x=(yield)와 같이 코루틴 바깥에서 보낸 값을 받아서 x에 저장하고, print로 x의 값을 출력한다."""


""" 코루틴 바깥에서는 co=number_coroutine()과 같이 코루틴 객체를 생성한 뒤 next(co)로 코루틴 안의 코드를 최초로 실행하여 yield까지
    코드를 실행한다(co.__next__()를 호출해도 상관이 없다.).
    
    
    * next(코루틴 객체)"""


""" 그 다음에 co.send로 숫자 1, 2, 3을 보내면 코루틴 안에서 숫자를 받은 뒤 print로 출력한다.

    먼저 next(co)로 코루틴의 코드를 최초로 실행하면 x=(yield)의 yield에서 대기하고 다시 메인 루틴으로 돌아온다.
    
    
    그 다음에 메인 루틴에서 co.send(1)을 1을 보내면 코루틴은 대기 상태에서 풀리고 x(yield)의 x=부분이 실행된 뒤 print(x)로
    숫자를 출력한다. 이 코루틴은 while true:로 반복하는 구조이므로 다시 x=(yield)의 yield에서 대기한다. 그리고 나서 메인 루틴으로 돌아온다.
    이런 과정으로 send가 보낸 값을 (yield)가 받게 된다.
    
    계속 같은 과정으로 send를 사용하여 값을 보내면 코루틴에서 값을 받아서 출력한다.
    
    정리하자면 next 함수(__next__ 메서드)로 코루틴의 코드를 최초로 실행하고, send 메서드로 코루틴에 값을 보내면서 대기하고 있던 코루틴의 코드를 다시
    실행한다."""


# 참고: send로 코루틴의 코드를 최초로 실행하기

""" 지금까지 코루틴의 코드를 최초로 실행할 때 next 함수(__next__ 메서드)를 사용했지만, 코루틴객체.send(None)과 같이 send 메서드에 None을 지정해도
    코루틴의 코드를 최초로 실행할 수 있다."""