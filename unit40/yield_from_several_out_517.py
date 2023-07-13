# yield from으로 값을 여러 번 바깥으로 전달하기

""" 지금까지 yield로 값을 한 번씩 바깥으로 전달한다. 그래서 값을 여러 번 바깥으로 전달할 때는 for 또는 while 반복문으로
    반복하면서 yield를 사용했다. 다음은 리스트의 1, 2, 3을 바깥으로 전달한다."""



def number_generator():
    x=[1,2,3]
    for i in x:
        yield i



for i in number_generator():
    print(i)


""" 이런 경우에는 매변 반복문을 사용하지 않고, yield from을 사용하면 된다. yield from에는 반복 가능한 객체, 이터레이터, 제너레이터 객체를
    지정한다. (yield from은 파이썬 3.3 이상부터 사용이 가능하다)
    
    * yield from 반복가능한 객체

    * yield from 이터레이터

    * yield from 제너레이터 객체
    
    """

def number_generator():
    x=[1,2,3]
    yield from x    # 리스트에 들어있는 요소를 한 개씩 바깥으로 전달


for i in number_generator():
    print(i)

# 1
# 2
# 3


""" 위의 방법과 같이 하면 리스트에 들어있는 요소를 한 개씩 바깥으로 전달한다. 즉, yield from을 한 번 사용하여 값을 세 번 바깥으로 전달한다.
    따라서 next 함수(__next__ 메서드)를 세번 호출할 수 있다."""


g=number_generator()

print(next(g))
# 1
print(next(g))
# 2

print(next(g))
# 3



# yield from 제너레이터 객체 지정하기

""" 이번에는 yield from에 제너레이터 객체를 지정해보겠다(이터레이터는 제너레이터와 동작이 같으니 생략한다.)."""

def number_generator(stop):
    n=0
    while n<stop:
        yield n
        n+=1


def three_generator():
    yield from number_generator(3)  # 숫자를 세 번 바깥으로 전달한다.


for i in three_generator():
    print(i)

# 0
# 1
# 2


""" 먼저 제너리터 number_generator는 매개변수로 받은 숫자 직전까지 숫자를 만들어 낸다. 그리고 three_generator에서는 
    yield from number_generator(3)과 같이 yield from 에 제너레이터 객체를 지정했다.
    
    number_generator(3)은 숫자를 세 개를 만들어내므로  yield from number_generator(3)는 숫자를 세 번 바깥으로 전달한다.
    따라서 for 반복문에 three_generator()를 사용하면 숫자를 세 번 출력한다(next 함수 또는 __next__ 메서드도 세 번 호출 가능)."""



# 참고: 제너레이터 표현식

""" 리스트 표현식을 사용할 때 [](대괄호)를 사용했다. 같은 리스트 표현식을 ()(괄호)로 묶으면 제너레이터 표현식이 된다. 리스트 표현식은
    처음부터 리스트의 요소를 만들어내지만 제너레이터 표현식은 필요할 때 요소를 만들어내므로 메모리를 절약할 수 있다.
    
    
    * (식 for 변수 in 반복가능한객체)
    
    """

print([i for i in range(50) if i%2==0])


print((i for i in range(50) if i%2==0 ))