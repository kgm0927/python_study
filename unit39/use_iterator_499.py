# 이터레이터 사용하기

""" 이터레이터(iterator)는 값으로 차례대로 꺼낼 수 있는 객체(object)이다."""


""" 이는 숫자를 모두 만들어 내는 것이 아니라 0부터 99까지 값을 차례대로 꺼낼 수 있는 이터레이터 하나만 만들어 내는 것이다.
    이후 반복할 때마다 이터레이터에서 숫자를 하나씩 꺼내서 반복한다."""


""" 만약 연속된 숫자를 만들면 숫자가 적을 때는 상관없지만 숫자가 아주 많을 때는 메모리를 많이 사용하게 되므로 성능에도 불리하다.
    그래서 파이썬에서는 이터레이터만 생성하고 값이 필요한 시점이 되었을 때 값을 만드는 방식을 이용한다. 즉, 데이터 생성을 뒤로 미루는
    것인데 이러한 방식을 지연 평가(lazy evaluation)라고 한다."""






# 반복 가능한 객체 알아보기


""" 이터레이터를 만들기 전에 반복 가능한 객체(iterable)에 대해서 알아보겠다. 반복 가능한 객체는 말 그대로 반복할 수 있는 객체인데 우리가
    흔히 사용하는 문자열, 리스트, 딕셔너리, 세트가 반복 가능한 객체이다. 즉, 요소가 여러 개 들어있고, 한 번에 하나씩 꺼낼 수 있는 객체이다."""


""" 객체작 반복 가능한 객체인지 알아보는 방법은 객체에 __iter__ 메서드가 있는지 확인해 보면 된다. 다음과 같이 dir 함수를 사용하면 객체의 메서드를 확인할
    수 있다."""


print(dir([1,2,3]))
"""['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', 
'__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
'__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
'__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']"""




""" 이 리스트에서 __iter__를 호출해보면 이터레이터가 나온다."""


print([1,2,3].__iter__())
# <list_iterator object at 0x000002820455AB00>



""" 리스트의 이터레이터를 변수에 저장한 뒤 __next__ 메서드를 호출해보면 요소를 차례대로 꺼낼 수 있다."""

it=[1,2,3].__iter__()

print(it.__next__())
# 1
print(it.__next__())
# 2
print(it.__next__())
# 3


""" it에서 __next__를 호출할 때마다 리스트에 들어있는 1, 2, 3이 나온다. 그리고 3 다음에 __next__를 호출하면 StopIteration 예외가 발생한다.
    
    이처럼 이터레이터는 __next__로 요소를 계속 꺼내다가 꺼낼 요소가 없다면 StopIteration 예외를 발생시켜서 반복을 끝낸다.
    
    물론, 리스트뿐만 아니라 문자열, 딕셔너리, 세트도 __iter__를 호출하면 이터레이터가 나온다. 그리고 이터레이터에서 __next__를 호출하면 차례대로
    값을 꺼낸다(__next__ 호출은 생략한다)."""


print('Hello, world!'.__iter__())
# <str_ascii_iterator object at 0x000001270983BFA0>
print({'a':1,'b':2}.__iter__())
# <dict_keyiterator object at 0x00000127099471A0>
print({1,2,3}.__iter__())
# <set_iterator object at 0x000001270994EA40>

""" 리스트, 문자열, 딕셔너리, 세트는 요소가 눈에 보이는 반복 가능한 객체이다. 이번에는 요소가 눈에 보이지 않는 range를 살펴보겠다. 다음과 같이
    range(3)에서 __iter__로 이터레이터를 얻어낸 뒤 __next__ 메서드를 호출한다."""



it=range(3).__iter__()

print(it.__next__())
# 0
print(it.__next__())
# 1
print(it.__next__())
# 2



""" it에서 __next__를 호출할 때마다 0부터 숫자가 증가해서 2까지 나왔다. 그리고 2 다음에 __next__를 호출했을 때 StopIteration 예외가 발생했다. 즉,
    range(3) 이므로 0,1,2 세 번 반복하여 요소가 눈에 보이지 않지만 지정된 만큼 숫자를 꺼내서 반복할 수 있다."""





# for와 반복 가능한 객체


""" 다음과 같이 for에 range(3)를 사용했다면 먼저 range에서 __iter__로 이터레이터를 얻는다. 그리고 한 번 반복할 때마다 이터레이터에서 __next__로 숫자를
    꺼내서 i에 저장하고 지정된 숫자 3이 되면 StopIteration을 발생시켜서 반복을 끝낸다."""


for i in range(3):
    print(i)

    """여기서 range(3)은"""

    it.__next__()
    it.__next__()
    it.__next__()
    """ 이렇게 3번 하는 것과 같다."""



""" 여기서는 반복 가능한 객체와 이터레이터가 분리되어 있지만 클래스에 __iter__와 __next__메서드를 모두 구현하면 이터레이터를 만들 수 있다. 특히 __iter__,
    __next__를 가진 객체를 이터레이터 프로토콜(iterator protocol)을 지원한다고 말한다."""


""" 정리하면 반복 가능한 객체는 요소를 한 번에 하나식 가져올 수 있는 객체이고, 이터레이터는 __next__ 메서드를 사용해서 차례대로 값을 꺼낼 수 있는 객체이다.
    반복 가능한 객체(iterable)와 이터레이터(iterator)는 별개의 객체이므로 둘은 구분해야 한다. 즉, 반복 가능한 객체에서 __iter__ 메서드로 이터레이터를 얻는다."""



# 참고

"""Unit11에서 '시퀀스 자료형 사용하기'에서 리스트, 튜플, range, 문자열은 시퀀스 객체라고 했는데 이 유닛에서는 반복 가능한 객체라고 했다. 시퀀스 객체와
    반복 가능한 객체의 차이점은 무엇인가?
    
    반복 가능한 객체는 시퀀스 객체를 포함한다. 
    
    리스트, 튜플, range, 문자열은 반복 가능한 객체이면서 시퀀스 객체이다. 하지만, 딕셔너리와 세트는 반복 가능한 객체이지만 시퀀스 객체는 아니다. 왜냐하면
    시퀀스 객체는 요소의 순서가 정해져 있고 연속적(sequence)으로 이어져 있어야 하는데, 딕셔너리와 세트의 요소는(키)의 순서가 정해져 있지 않기 때문이다.
    
    따라서 시퀀스의 객체가 반복 가능한 객체보다 더 좁은 개념이다.
    
    
    
    
                _________________________________________ 반복 가능한 객체 ______________________________________
               |                                                                                                |
               |                                                                                                |
               |                    ------------------ 시퀀스 객체      ----------------                         |
               |                    |                                                   |                       |
               |                    |                                                   |                       |
               |                    |    리스트(list)           튜플(tuple)              |                       |
               |                    |                                                   |                       |
               |                    |                                                   |                       |
               |                    |                                                   |                       |
               |                    |   range                  문자열(str)               |                       |
               |                    |                                                   |                       | 
               |                    |                                                   |                       |
               |                    |_________________________________________________  |                       |
               |                                                                                                |
               |                딕셔너리(dict)                                 세트(set)                         |
               |                                                                                                |
               |________________________________________________________________________________________________|        


    
    
    """


