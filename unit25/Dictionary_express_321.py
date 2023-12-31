# 딕셔너리 표현식 사용하기

""" 리스트와 마찬가지로 딕셔너리도 for 반복문과 if 조건문을 사용하여 딕셔너리를 생성할 수 있다. 다음과
    같이 딕셔너리 안에 키와 값, for 문을 지정하면 된다.
    
    
    * {키: 값 for 키, 값 in 딕셔너리}
    * dict({키: 값 for 키, 값 in 딕셔너리})
        """


keys=['a','b','c','d']
x={key: value for key, value in dict.fromkeys(keys).items()}

print(x)
# {'a': None, 'b': None, 'c': None, 'd': None}



""" 딕셔너리 표현식을 사용할 때는 for in 다음에 딕셔너리를 지정하고 items를 사용한다. 그리고 키, 값을
    가져온 뒤에는 키:값 형식으로 변수나 값을 배치하여 딕셔너리를 생성하면 된다."""


""" 물론 그냥 keys로 키만 가져온 뒤 특정 값을 넣거나, value로 값을 가져온 뒤 값을 키로 사용할 수도 있다."""


""" 또는, 키와 값의 자리를 바꾸는 등 여러 가지로 응용할 수 있다."""

print({value: key for key, value in {'a':10,'b':20,'c':30,'d':40}.items()})
# {10: 'a', 20: 'b', 30: 'c', 40: 'd'}






# 딕셔너리 표현식에서 if 조건문 사용하기



""" 딕셔너리 표현식은 딕셔너리에서 특정 값을 찾아서 삭제할 때 유용하다.

    딕셔너리는 특정 키를 삭제하는 pop메서드만 제공할 뿐 특정 값을 삭제하는
    메서드는 제공하지 않는다. 그러면 특정 값을 찾아서 키-값 쌍을 삭제하려면 어떻게
    해야 하는가? 간단하게 for 반복문으로 반복하면서 del로 삭제하는 방식을 떠올릴 수
    있다."""
x={'a':10, 'b':20, 'c':30, 'd':40}

"""
for key, value in x.items():
    if value==20:
        del x[key]
print(x)"""




""" 별 문제 없이 잘 삭제가 될 것 같았지만 반복 도중에 딕셔너리의 크기가 바뀌었다는 에러가
발생했다. 즉, 딕셔너리는 for 반복문으로 반복하면서 키-값 쌍을 삭제해서는 안된다.

이때는 딕셔너리 표현식에서 if 조건문을 사용하여 삭제할 값을 제외하면 된다.

    * {키: 값 for 키,값 in 딕셔너리 if 조건식}
    * dict({키: 값 for 키,값 in 딕셔너리 if 조건식})

"""

x={'a':10,'b':20,'c':30,'d':40}
x={key: value for key, value in x.items() if value!=20}
print(x)
# {'a': 10, 'c': 30, 'd': 40}
