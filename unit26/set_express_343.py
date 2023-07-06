# 세트 표현식 사용하기

""" 세트는 for 반복문과 if 조건문을 사용하여 세트를 생성할 수 있다. 다음과 같이 세트 안에 식과
    for 반복문을 지정하면 된다.
    
    * {식 for 변수 in 반복가능한객체}
    * set(식 for 변수 in 반복가능한 객체)
    """

a={i for i in 'apple'}

print(a)
# {'e', 'p', 'a', 'l'}


""" {} 또는 set() 안에 식, for, 변수, in, 반복 가능한 객체를 지정하여 세트를 생성한다. 여기서는 반복 가능한 객체로 문자열
    'apple'을 지정했다. """




# 세트 표현식에 if 조건문 사용하기

""" 이번에는 세트 표현식에서 if 조건문을 사용해본다. 다음과 같이 if 조건문 뒤에 지정한다.


    * {식 for 변수 in 세트 if 조건식}
    * set(식 for 변수 in 세트 if 조건식)
"""


a={i for i in 'pineapple' if i not in 'apl'}

print(a)
# {'i', 'e', 'n'}

""" {i for i in 'pineapple' if i not in 'apl'}은 문자열 'pineapple에서 'a','p','l'을 제외한 문자들로 세트를 생성한다. 즉, 
    다음과 같이 for 반복문 뒤에서 if 조건문을 지정하면 if 조건문에서 특정 요소를 제외한 뒤 세트를 생성한다.
    
    위의 코딩의 아래와 같이 할 수 있다.
    '"""


a={ i for i in 'pineapple' if i!='a' and i!='p' and i!='l'}

print(a)