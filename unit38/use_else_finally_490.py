# else와 finally 사용하기


""" 이번에는 예외가 발생하지 않았을 때 코드를 실행하는 else를 사용해보겠다. 다음과 같이 else는 except 바로 다음에 와야 하며 except를 생략할 수 없다.

    try:
        실행할 코드
    
    except:
        예외가 발생했을 대 처리하는 코드
    
    else:
        예외가 발생하지 않았을 때 실행할 코드"""


try:
    x=int(input('나눌 숫자를 입력하세요:'))
    y=10/x
except ZeroDivisionError:
    print('숫자를 0으로 나눌 수 없습니다.')

else:
    print(y)

# 나눌 숫자를 입력하세요:2
# 5.0


"""2를 입력했으르모 y=10/x에서 예외가 발생하지 않는다. 따라서 else 코드가 실행되고 계산결과가 출력이 된다.

    물론 0을 입력해서 예외가 발행하면 except의 코드만 실행되고 else의 코드는 실행되지 않는다."""


# 나눌 숫자를 입력하세요:0
# 숫자를 0으로 나눌 수 없습니다.
#




# 예외와는 상관없이 항상 코드 실행하기

""" 이번에는 예외 발생 여부와 상관없이 항상 코드를 실행하는 finally를 사용해보겠다. 특히 finally는 except와 else를 생략할 수 있다.


    try:
        실행할 코드
    except:
        예외가 발생했을 때 처리하는 코드
    else:
        예외가 발생하지 않았을 때 실행할 코드
    finally:
        예외 발생 여부와 상관없이 항상 실행할 코드
        
        
        """



try:
    x=int(input('나눌 숫자를 입력하세요.:'))
    y=10/x

except ZeroDivisionError:   # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없다.')

else:                       # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)

finally:                    # 예외 발생 여부와 상관없이 항상 실행됨
    print('코드 실행이 끝이 났다.')

""" 2를 눌렀을 시 """
# 나눌 숫자를 입력하세요.:2
# 5.0
# 코드 실행이 끝이 났다.


""" 0을 눌렀을 시"""

# 나눌 숫자를 입력하세요.:0
# 숫자를 0으로 나눌 수 없다.
# 코드 실행이 끝이 났다.







# 참고: try 안에서 만든 변수는 try 바깥에서 사용할 수 있나?

""" try는 함수가 아니더라도 스택 프레임을 만들지 않는다. 따라서 try 안에서 변수를 만들더라도 try 바깥에서 사용할 수 있다. 물론 except, else, finally에서도
    사용할 수 있다."""