# 하위 코루틴의 반환값 가져오기


""" 제너레이터에서 yield from을 사용하면 값을 바깥으로 여러 번 전달했다고 했다.(yield_from_several_out_517.py) 하지만 코루틴에서는
    약간 다르게 사용한다. yield from에 코루틴을 지정하면 해당 코루틴에서 return으로 반환한 값을 가져온다.
    
    
    * 변수=yield from 코루틴()"""



def accumulate():
    total=0
    while True:
        x=(yield)       # 코루틴 바깥에서 값을 받아옴
        
        if x is None:       # 받아온 값이 None이면
            return total    # 합계 total을 반환
        
        total+=x




def sum_coroutine():
    while True:
        total=yield from accumulate()       # accumulate의 반환값을 가져옴
        print(total)


co=sum_coroutine()
next(co)


for i in range(1,11):   # 1부터 10까지 반복
    co.send(i)          # 코루틴 accumulate에 숫자를 보냄
co.send(None)           # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄

for i in range(1,101):  # 1 부터 100까지 반복
    co.send(i)          # 코루틴 accumulate에 숫자를 보냄
co.send(None)           # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄


""" 코루틴에 1부터 10까지 보내서 합계 55를 구하고, 다시 1부터 100까지 보내서 합계 5050을 구했다.

    먼저 숫자를 받아서 누적할 코루틴을 만든다. x=(yield)와 같이 코루틴 바깥에서 값을 받아온 뒤 total에 계속 더한다.
    특히 이 코루틴은 while True:로 무한힌 반복하지만 코루틴을 끝낼 방법이 필요하다.
    
    여기서는 코루틴 바깥에서 받아온 값이 None이면 return으로 total을 반환하고 코루틴을 끝낸다."""


""" 이제 합계를 출력할 코루틴을 만든다. 먼저 while True:로 무한히 반복한다. 그리고 total=yield from accumulate()와 같이
    yield from을 사용해서 코루틴 accumulate의 반환값을 가져온다.
    
    
    코루틴에서 yield from을 사용하면 코루틴 바깥에서 send로 하위 코루틴까지 값을 보낼 수 있다. 따라서 co=sum_coroutine()으로
    코루틴 객체를 만든 뒤 co.send로 값을 보내면 accumulate에서 값을 받는다.
    
    
    co.send로 숫자를 계속 보내다가 누적을 끝내고 싶으면 None을 보내면 된다.
    
    이때 accumulate는 None을 받으면 코루틴이 완전히 끝나지만 sum_coroutine에서 무한 루프로 반복하고 있으므로 print로 total을 출력한 뒤 다시
    yield from accumulate()로 accumulate를 실행하게 된다"""


#  StopIteration 예외 발생시키기

""" 코루틴도 제너레이터이므로 return을 사용하면 StopIteration이 발생한다. 그래서 코루틴에서 return 값은 raise StopIteration(값)처럼 사용할 수도 있다.
    이렇게 raise로 StopIteration 예외를 직접 발생시키고 값을 저장하면 yield from으로 값을 가져올 수 있다.(다만 이 방법은 3.6 이하에서만 가능하다.
        그 이후는 그냥 return을 써야 한다.)"""



# 참고: 코루틴의 yield from으로 값을 발생시키기

""" 이번 예제에서는 x=(yield)와 같이 코루틴을 바깥에서 받아왔다. 하지만 코루틴에서 yield에 값을 지정해서 바깥에서 전달했다면 yield from은
    해당 값을 다시 바깥으로 전달한다."""


def number_coroutine():
    x=None
    while True:
        x=(yield x) # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        if x==3:
            return x
        

def print_coroutine():
    while True:
        x=yield from number_coroutine() # 하위 코루틴의 yield에 저장된 값을 다시 바깥으로 전달
        print('print_coroutine',x)


co=print_coroutine()
next(co)

x=co.send(1)        # number_coroutine으로 1을 보냄
print(x)            # 1: number_coroutine의 yield에서 바깥으로 전달한 값

x=co.send(2)        # number_coroutine으로 2를 보냄
print(x)            # 2: number_coroutine의 yield에서 바깥으로 전달한 값

co.send(3)          # 3을 보내서 반환값을 출력하도록 만듦

# 1
# 2
# print_coroutine 3