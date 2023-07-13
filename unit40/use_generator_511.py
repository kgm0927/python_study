# 제너레이터 사용하기

""" 제너레이터는 이터레이터를 생성해주는 함수입니다. 이터레이터는 클래스에 __iter__, __next__ 또는 __getitem__ 메서드를 구현해야 하지만
    제너레이터는 함수 안에서 yield라는 키워드만 사용하면 끝이다. 그래서 더 간단하게 제너레이터를 이터레이터보다 작성할 수 있다."""


""" 참고로 제너레이터를 '발생자'라고 하기도 한다."""


# 제너레이터와 yield 알아보기

""" 함수 안에서 yield를 사용하면 함수는 제너레이터가 되며 yield에는 값(변수)을 저장한다.

    * yield 값
    
    이제 yield를 사용하여 제너레이터를 만들고 for 반복문에서 0,1,2 숫자 세 개를 출력해본다."""


def number_generator():
    yield 0
    yield 1
    yield 2


for i in number_generator():
    print(i)

""" for 반복문에서 number_generator()를 지정해서 값을 출력해보면 yield에 지정했던 0,1,2가 나온다."""



# 제너레이터 객체가 이터레이터인지 확인하기

""" number_generator 함수로 만든 객체가 정말 이터레이터인지 살펴보겠다. 다음과 같이 dir함수로 메서드 목록을 확인해본다."""

g=number_generator()


print(g)
# <generator object number_generator at 0x0000021A18F88A90>
print(dir(g))
""" ['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__', 
 '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 
 'gi_code', 'gi_frame', 'gi_running', 'gi_suspended', 'gi_yieldfrom', 'send', 'throw']"""


"""
    number_generator 함수를 호출하면 제너레이터 객체(generator object)가 반환이 된다. 이 객체를 dir 함수로 살펴보면 이터레이터에서 볼 수 있는
    __iter__, __next__ 메서드가 들어있다.

"""

""" 실제로 제너레이터 객체의 __next__를 호출해보면 숫자 0,1,2rk 나오다가 StopIteration 예외가 발생한다."""

print(g.__next__())
# 0
print(g.__next__())
# 1
print(g.__next__())
# 2


""" 이터레이터와 동작이 똑같다.

    이처럼 함수에 yield만 사용해서 간단하게 이터레이터를 구현할 수 있다. 단, 이터레이터는 __next__메서드 안에 직접 return으로 값을 반환했지만 제너레이터는
    yield에 지정한 값이 __next__ 메서드(next 함수) 반환값으로 나온다. 
    
    또한, 이터레이터는 raise로 StopIteration 예외를 직접 발생시켰지만 제너레이터는 함수의 끝까지 도달하면 StopIteration 예외가 자동으로 발생한다.
    
    제너레이터는 제너레이터 객체에서 __next__ 메서드를 호출할 때마다 함수 안의 yield까지 코드를 실행하며 yield에서 값을 발생시킨다(generate).
    그래서 이름이 제너레이터(generator)다."""


# for와 제너레이터

""" 그럼 for 반복문과 제너레이터를 살펴보겠다. 다음과 같이 for 반복문은 반복할 때마다 __next__를 호출하므로 yield에서 발생시킨 값을 가져온다.
    그리고 StopIteration 예외가 발생하면 반복을 끝낸다.
    
    
    for i in number_generator():    ->      __iter__()          --->        __next__() -> yield 0 ->0     
        print(i)                                                                |
                                                                                |
                                                                            __next__()-> yield 1  ->1
                                                                                |
                                                                                |
                                                                            __next__()-> yield2   ->2
                                                                                |
                                                                                |
                                                                            Stopiteration -> 반복 끝

                                                                            
참고로 제너레이터 객체에서 __iter__를 호출하면 self를 반환하므로 같은 객체가 나온다
(제너레이터 함수 호출> 제너레이터 객체>__iter__는 self 반환> 제너레이터 객체). 

그런데 generate라는 키워드를 사용하면 되는데 왜 yield라고 이름을 지었을까? yield는 생산하다라는 뜻과 함께
양보하다 라는 뜻도 가지고 있다. 즉, yield를 사용하면 값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보한다.

따라서 yield는 현재 함수를 잠시 중단하고 함수 바깥의 코드가 실행하도록 만든다.
                                                                            
                                                                                
                                                                                """


# yield의 동작 과정 알아보기

""" 그럼 yield의 동작 과정을 알아보기 위해 for 반복문 대신 next 함수로 __next__ 메서드를 직접 호출해 본다.

    * 변수=next(제너레이터 객체)"""


def number_generator():
    yield 0     # 0을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 1     # 1을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 2     # 2을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보


g=number_generator()


a=next(g) # yield를 사용하여 함수 바깥으로 전달한 값은 next의 반환값으로 나옴
print(a)    #0

b=next(g)
print(b)    #1

c=next(g)
print(c)    #2



""" yield를 사용하여 바깥으로 전달한 값은 next 함수(__next__ 메서드)의 반환값으로 나온다고 했다. 따라서 next(g)의 반환값을 출력해보면
    yield에 지정한 0,1,2가 차례대로 나온다. 즉, 제너레이터 함수가 실행되는 중간에 next 값을 가져온다.
    
    먼저 g=number_generator()와 같이 제너레이터 객체를 만든다. 그 다음에 next(g)를 호출하면 제너레이터 안의 yield 0이 실행되어 숫자 0을 전달한뒤
    바깥의 코드가 실행되도록 양보한다. 함수 바깥에서는 print(a)로 next(g)에서 반환된 값ㅇ르 출력한다."""


""" 값을 출력했으면 next(g)로 다시 제너레이터 안의 코드를 실행한다. 이때는 yield 1이 실행되고 숫자를 발생시켜서 바깥으로 전달한다. 그리고 함수
    바깥에서는 print(b)로 next(g)에서 반환된 값을 출력한다."""



# 참고: 제너레이터와 return

""" 제너레이터 함수 끝까지 도달하면 StopIteration 예외가 발생한다. 마찬가지로 return도 함수를 끝내므로 return을 사용해서 함수 중간에 빠져 나오면
    StopIteration 예외가 발생한다.
    
    특히 제너레이터 안에서 return에 반환값을 지정하면 StopIteration 예외의 에러 메시지로 들어간다."""


def one_generator():
    yield 1
    return 'return에 저장한 값'

try:
    g=one_generator()
    next(g)
    next(g)

except StopIteration as e:
    print(e)