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