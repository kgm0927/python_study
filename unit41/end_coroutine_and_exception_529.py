# 코루틴을 종료하고 예외 처리하기

""" 보통 코루틴은 실행 상태를 유지하기 위해 while True:를 사용해서 끝나지 않는 무한 루프로 동작한다. 만약
    코루틴을 강제로 종료하고 싶다면 close 메서드를 사용한다.
    
    * 코루틴객체.close()

    """

""" 다음은 코루틴에 숫자를 20개 보낸 뒤 코루틴을 종료한다."""
def number_corountine():
    while True:
        x=(yield)
        print(x,end=' ')


co=number_corountine()
next(co)

for i in range(20):
    co.send(i)


co.close() # 코루틴 종료

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 


""" 코루틴 객체에서 close 메서드를 사용하면 코루틴이 종료된다. 사실 파이썬 스크립트가 끝나면 코루틴도 끝나기 때문에
    close를 사용하지 않을 것과 별 차이가 없다. 하지만 close는 코루틴 종료 시점을 알아야 할 때 사용하면 편리하다."""




print()


# GeneratorExit 예외 처리하기


""" 코루틴 객체에서 close 메서들르 호출하면 코루틴이 종료될 때 GeneratorExit 예외가 발생한다. 따라서 이 예외를 처리하면
    코루틴의 종료 시점을 알 수 있다."""


def number_coroutine():
    try:
        while True:
            x=(yield)
            print(x,end=' ')
    except GeneratorExit:   # 코루틴이 종료될 때 GeneratorExit 예외 발생
        print()
        print('코루틴 종료')

co=number_coroutine()
next(co)

for i in range(20):
    co.send(i)


co.close()    

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
# 코루틴 종료


""" 코루틴 안에서 try except로 GeneratorExit 예외가 발생하면 '코루틴 종료'가 출력되도록 만들었다. 이렇게 하면 close 메서드로
    코루틴을 종료할 때 원하는 코드를 실행할 수 있다."""



# 코루틴 안에 예외 발생시키기


""" 코루틴 안에 예외를 발생시켜서 코루틴을 종료해보겠다.

    코루틴 안에 예외를 발생시킬 때는 throw 메서드를 사용한다. throw는 말 그대로 '던지다'라는 뜻으로 예외를 코루틴 안으로 던진다.
    이때 throw 메서드에 지정한 에러 메시지는 except as의 변수에 들어간다.
    
    
    * 코루틴객체.throw(예외이름, 에러메시지)
    
    다음은 코루틴에 숫자를 보내서 누적하다가 RuntimeError 예외가 발생하면 에러 메시지를 출력하고 누적된 값을 코루틴 바깥으로 전달한다."""


def sum_coroutine():
    try:
        total=0
        while True:
            x=(yield)
            total +=x
    except RuntimeError as e:
        print(e)
        yield total # 코루틴 바깥으로 값 전달


co=sum_coroutine()
next(co)


for i in range(20):
    co.send(i)



print(co.throw(RuntimeError,'예외로 코루틴 끝내기')) # 190
                                                    # 코루틴의 except에서 yield로 전달받은 값

# 예외로 코루틴 끝내기
# 190



""" 코루틴 안에서 try except로 RuntimeError 예외가 발생하면 print로 에러 메시지를 출력하고 yield를 사용하여 total을 
    바깥으로 전달하도록 만들었다."""

""" 코루틴 바깥에서는 co.throw(RuntimeError,'예외로 코루틴 끝내기')와 같이 throw 메서드에 RuntimeError 예외와 에러 메시지를
    지정하면 코루틴 안에서 예외가 발생한다. 그리고 코루틴 안의 except에서 yield를 사용하여 바깥으로 전달한 값은 throw 메서드의 반환값을
    나온다.
    
    여기서는 코루틴 안에서 예외 처리를 했으므로 '예외로 코루틴 끝내기'가 출력되고, 코루틴 바깥에서는 누적된 값이 190이 출력된다."""