
""" 리스트 컴프리핸션(list comprehension):

리스트 안에 식, for 반복문, if 조건문 등을 지정하여 리스트를 새성하는 것을 의미."""


# 형태

# [식 for 변수 in 리스트]
# list(식 for 변수 in 리스트)


a=[i for i in range(10)]
print(a)

b=list(i for i in range(10))
print(b)

""" 리스트 안에 식, for, 변수, in, 리스트 순서로 들어 있지만
뒤에서 앞으로 읽으면 간단하다. 즉, range(10)으로 0부터 9까지 생성하여
변수 i에 숫자를 꺼내고, 최종적으로 i를 이용하여 리스트를 만든다는 것이다."""



"""[i for i in range(10)]는 변수 i를 그대로 사용해도 되지만, 다음과 같이
식 부분에서 i를 다른 값과 연산하면 각 연산의 결과를 리스트로 생성한다."""


c=[i+5 for i in range(10)]
print(c)

d=[i*2 for i in range(10)]
print(d)


# 대괄호와 list() 리스트 표현식

""" 리스트 표현식은 [식 for 변수 in 리스트]처럼 [](대괄호)로 만들 수 있고, list(식 for 변수 in 리스트)처럼
list로 만들 수 있다. 둘 중에 성능은 대괄호 방식이 더 좋다. 특히 list의 방식은 C언어 스타일이라 대괄호 방식이
파이썬 다운 코드이다. 따라서 리스트 표현식은 대괄호 방식을 사용하는 것이 좋다. list는 리스트 표현식을 만들 수 있다는
것만 알면 된다."""



# 리스트 표현식에서 if 조건문 사용하기

""" 이번에는 리스트 표현식에서 if 조건문을 사용해 본다. 다음과 같이 if 조건문은 for 반복문 뒤에 지정한다."""

    # [식 for 변수 in 리스트 if 조건식]
    # list(식 for 변수 in 리스트 if 조건식)


a=[i for i in range(10) if i%2==0]
print(a)


"""물론 다음과 같이 i를 다른 값과 연산해서 리스트를 만들어도 된다."""

b=[i+5 for i in range(10) if i%2==0]
print(b)