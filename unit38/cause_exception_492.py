# 예외 발생시키기


""" 지금까지 숫자를 0으로 나눴을 때, 에러, 리스트의 범위를 벗어난 인덱스에 접근했을 때 에러 등 파이썬에서 정해진 예외만 처리했었다.
    이번에는 직접 예외를 만들어서 발생시킬 것이다.
    
        * raise 예외('에러메시지')
        
"""


try:
    x=int(input('3의 배수를 입력하세요: '))
    if x%3!=0:
        raise Exception('3의 배수가 아닙니다.')
    print(x)

except Exception as e:
    print('예외가 발생했습니다.',e)

# 3의 배수를 입력하세요: 5
# 예외가 발생했습니다. 3의 배수가 아닙니다.


""" raise Exception('3의 배수가 아닙니다.')으로 예외를 발생시켰다. 이때 Exception에 넣은 에러 메시지는 except Exception as e:의 e에 들어간다.


    그리고 raise로 예외를 발생시키면 raise 아래에 있는 코드는 실행되지 않고 바로 except로 넘어간다. 따라서 try의 나머지인 print(x)는 실행되지 않는다.
    
    
    참고로 이 예제에서는 예외로 Exception을 사용했는데 RuntimeError, NotImplementedError 등 다른 예외를 사용해도 상관이 없다."""



# raise의 처리 과정

""" 다음은 함수 안에서 raise를 사용하지만 함수 안에는 try except가 없는 상태이다."""


def three_multiple():
    x=int(input('3의 배수를 입력하세요.:'))
    if x%3!=0:                                          # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아니다.')           # 예외를 발생시킴
    print(x)                                            # 현재 함수 안에는 except가 없으므로
                                                        # 예외를 상위 코드 블록으로 넘김

                                        


try:
    three_multiple()
except Exception as e:                  # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('예외가 발생했습니다.',e)

# 3의 배수를 입력하세요.:5
# 예외가 발생했습니다. 3의 배수가 아니다.
#



"""three_multiple 함수는 안에 try except가 없는 상태에서 raise로 예외를 발생시켰다. 이렇게 되면 함수 바깥에 있는 except에서 예외가 처리된다.
    즉, 예외가 발생하더라도 현재 코드 블록에서 처리해줄 except가 없다면 except가 나올 때까지 계속 상위 코드 블록으로 올라간다.
    
    
    만약 함수 바깥에도 처리해줄 except가 없다면 코드 실행은 중지되고 에러가 표시된다.
     
      
       three_multiple()
        
     
          

    
     

       
         """



# 현재 예외를 다시 발생시키기

""" 이번에는 try except에서 처리한 예외를 다시 발생시키는 방법이다. except 안에서 raise를 사용하면 현재 예외를 다시 발생시킨다(re-raise).



    * raise
    
"""

""" 다음은 three_multiple 코드 블록의 예외를 다시 발생시킨 뒤 상위 코드 블록에서 예외를 처리한다."""

def three_multiple():
    try:
        x=int(input('3의 배수를 입력하세요:'))
        if x%3!=0:                                  # x가 3의 배수가 아니면
            raise Exception('3의 배수가 아닙니다.')  # 예외를 발생시킴   
        print(x)
    
    except Exception as e:                          # 함수 안에서 예외를 처리함
        print('three_multiple 함수에서 예외가 발생했습니다.',e)
        raise   # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김



try:
    three_multiple()
except Exception as e: # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('스크립트 파일에서 예외가 발생했습니다.',e)


# 3의 배수를 입력하세요:5
# three_multiple 함수에서 예외가 발생했습니다. 3의 배수가 아닙니다.
# 스크립트 파일에서 예외가 발생했습니다. 3의 배수가 아닙니다.



""" three_multiple 함수 안에서 발생한 예외를 함수 안의 except에서 한 번 처리하고 raise로 예외를 다시 발생시켜서 상위 코드 블록으로 넘겼다.
    그다음에 함수 바깥의 except에서 예외를 처리했다. 이런 방식으로 같은 예외를 계속 처리해줄 수 있다."""


""" 참고로 rasie만 사용하면 같은 예외를 상위 코드 블록으로 넘기지만 raise에 다른 예외를 지정하고 에러 메시지를 넣을 수 있다.

    raise 예외('에러메시지')
    
  
    
        if x%3!=0:
            raise Exception('3의 배수가 아니다.')
            print(x)

except Exception as e:
    print('three_multiple 함수에서 예외가 발생했다.',e)
    raise RuntimeError('three_multiple 함수에서 예외가 발생하였다.')
    
    
    
    """






# 참고 : assert로 예외 발생시키기

""" 예외를 발생시키는 방법 중에는 assert를 사용하는 법도 있다. assert는 지정된 조건식이 거짓일 때 AssertionError 예외를 발생시키면 조건식이 참이면
    그냥 넘어간다. 보통 assert는 나와서는 안되는 조건을 검사할 때 사용한다.
    
        * assert 조건식
        * assert 조건식, 에러메세지"""


x=int(input('3의 배수를 입력하세요.'))
assert x%3==0, '3의 배수가 아닙니다.'
print(x)
""" 위의 코드는 5를 입력하면 오류가 날 수밖에 없다."""

"""assert는 디버깅 모드에서만 실행된다. 특히 파이썬은 기본적으로 디버깅 모드이며(__debug__의 값이 True)assert가 실행되지 않게 하려면 py에 -O를 붙여서 실행한다."""


