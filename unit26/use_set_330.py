# 세트 만들기

""" 파이썬은 집합을 표현하는 세트(set)라는 자료형을 제공한다. 집합을 영어로 하면 세트인데 수학에서 배우는
그 집합니다. 따라서 세트는 합집합, 교집합, 차집합 등의 연산이 가능하다."""



# 세트 만들기

"""세트는 {}(중괄호 )안에 값을 저장하면 각 값은 ,(콤마)로 구분을 해 준다.

    * 세트={값1, 값2, 값3}
"""

""" 간단하게 과일이 들어있는 세트를 만들어 보겠다."""


fruits={'strawberry','grape','orange','pineapple','cherry'}
print(fruits)
# {'orange', 'cherry', 'grape', 'pineapple', 'strawberry'}




""" 특히 세트는 리스트, 튜플, 딕셔너리와 달리 [](대괄호)로 특정 요소만 출력할 수는 없다."""



# 세트에 특정 값이 있는지 확인하기

""" 특정 세트에  특정 값이 있는지 확인하려면 어떻게 해야 하는가? 지금까지 리스트, 튜플, 딕셔너리에 사용했던 in 연산자를 사용하면 된다.

    * 값 in 세트

"""

fruits=['strawberry','grape','orange','pineapple','cherry']
print('orange' in fruits)
# True

print('peach' in fruits)
# False


""" 이처럼 세트에 특정 값이 있으면 True, 없으면 False가 나온다. 세트 fruits에 'orange'가 있으므로 True,
'peach'가 없으므로 False가 나왔다."""



""" 반대로 in 앞에 not을 붙이면 특정 값이 없는지 확인한다.

    * 값 not in 세트
"""


print('peach' not in fruits)
# True

print('orange' not in fruits)
# False


# set를 사용하여 세트 만들기

""" 이번에는 set를 사용하여 세트를 만들어 보겠다.

    * set(반복가능한객체)
"""


""" set에는 반복 가능한 객체(iterable)를 넣는다. (반복 가능한 객체는 unit39에 있다.). 여기서는 간단히 문자열과 range로 세트를 만들어보겠다."""


""" set('apple')과 같이 영문 문자열을 세트로 만들면 'apple'에서 유일한 문자인 'a','p','l'.'e' 만 세트로 만들어진다. 즉, 중복된 문자는 포함되지
    않는다."""

a=set('apple')
print(a)
# {'l', 'p', 'e', 'a'}



""" 그리고 set(range(5))와 같이 숫자를 만들어내는 range를 사용하면 0부터 4까지 숫자를 가진 세트를 만들 수 있다."""

b=set(range(5))
print(b)
# {0, 1, 2, 3, 4}



""" 빈 세트는 c=set()과 같이 아무것도 지정하지 않으면 된다."""

c=set()
print(c)
# set()


""" 단, 세트가 {}를 사용한다고 해서 c={}와 같이 만들면 빈 딕셔너리가 만들어지므로 주의해야 한다. 다음과 같이 type을 사용하면
    자료형의 종류는 알 수 있다.
    
        * type(객체)
    """

c={}
print(type(c))
# <class 'dict'>

c=set()
print(type(c))
# <class 'set'>



# 참고 : 프로즌 세트

""" 파이썬은 내용을 변경할 수 없는 세트도 제공한다.

    * 프로즌세트=frozenset(range(10))

"""

a=frozenset(range(10))
print(a)
# frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})



""" 이름 그대로 얼어 있는(frozen)세트이다. frozenset는 뒤에서 설명할 집합 연산과 메서드에서 요소를 추가하거나 삭제하는 연산,
    메서드는 사용할 수 없다. 즉, 다음과 같이 frozenset의 요소를 변경하려고 하면 에러가 발생한다."""


""" 그런데 요소를 변경할 수 없는 frozenset는 왜 사용하는가? frozenset는 세트 안에 세트를 넣고 싶을 때 사용한다. 다음과 같이
frozenset은 frozenset은 중첩해서 넣을 수 있다. 단, frozenset만 넣을 수 있고, 일반 set은 넣을 수 없다."""


print(frozenset({frozenset({1,2}),frozenset({3,4})}))
# frozenset({frozenset({3, 4}), frozenset({1, 2})})



# 집합 연산 사용하기


""" | 연산자 합집합(union)을 구하며 OR 연산자를 |를 사용한다. set.union 메서드와
    동작이 같다. 다음은 세트 {1,2,3,4}와 {3,4,5,6}을 모두 포함하므로 {1,2,3,4,5,6}나온다.
    
        * 세트1 | 세트2
        * set.union(세트1, 세트2)
    
    
    """

a={1,2,3,4}
b={3,4,5,6}

print(a|b)
# {1, 2, 3, 4, 5, 6}

print(set.union(a,b))
# {1, 2, 3, 4, 5, 6}



""" & 연산자 교집합(intersection)을 구하며 AND 연산자와 &를 사용한다. set.intersection 메서드와 동작이 같다. 다음은
    세트 {1,2,3,4}와 {3,4,5,6} 중에서 겹치는 부분을 구하므로 {3, 4}가 나온다.
    

    * 세트1 & 세트2
    * set.intersection(세트1, 세트2)

    """

print(a&b)
# {3, 4}

print(set.intersection(a,b))
# {3, 4}



""" - 연산자 차집합(difference)을 구하며 뺄셈 연산자 -를 사용한다. set.difference 메서드와 동작이 같다. 다음은 {1, 2, 3, 4}에서
    {3, 4, 5, 6}과 겹치는 3과 4를 뺐으므로 {1, 2}가 나온다.
    
    
        * 세트1 -세트2
        * set.difference(세트1, 세트2)"""


print(a-b)
print(set.difference(a,b))




""" ^ 연산자는 대칭차집합(symmetric difference)을 구하며 XOR 연산자 ^을 사용한다. set.symmetric_difference 메서드와 동작이 같다.

    대칭차집합 집합은 XOR 연산자의 특성을 그대로 따르는데 XOR은 서로 다르면 참이다. 따라서 집합에서는 두 집합 중 겹치지 않는 요소만 
    포함한다. 다음은 세트{1,2,3,4}와 {3,4,5,6} 중에서 값은 값 3과 4를 제외한 다른 모든 요소를 구하므로 {1, 2, 5, 6}이 나온다.
    
    
        * a^b
        * set.symmetric_difference(a,b)
    """


print(a^b)
# {1, 2, 5, 6}

print(set.symmetric_difference(a,b))
# {1, 2, 5, 6}



# 부분집합과 상위집합 확인하기

""" 세트는 부분집합, 진부분집합, 상위집합, 진상위집합 과 같이 속하는 관계를 표현할 수도 있다. 현재 세트가
다른 세트의 (진)부분집합 또는 (진)상위집합인지 확인할 때에는 세트 자료형에 부등호와 등호를 사용한다."""

""" <=은 현재 세트가 다른 세트의 부분집합(subset)인지 확인하며 issubset메서드와 같다. 다음은 세트{1, 2, 3, 4}가
    {1, 2, 3, 4}의 부분집합이므로 참이다.
    
    * 현재세트 <= 다른세트
    * 현재세트.issubset(다른세트)
    
    """


a={1,2,3,4}
print(a<={1,2,3,4})
# True

print(a.issubset({1,2,3,4,5}))
# True




""" <은 현재 세트가 다른 세트의 진부분집합(proper subset)인지 확인하며 메서드는 없다. 다음은 세트 {1,2,3,4}가
    {1,2,3,4,5}의 진부분집합이므로 참이다. 즉, 부분집합이지만 같지는 않을 때 참이다."""

a={1,2,3,4}
print(a<{1,2,3,4,5})
# True





""" >=은 현재 세트가 다른 세트의 상위집합(superset)인지 확인하며 issuperset 메서드와 같다. 다음은 세트 {1,2,3,4}
    가 {1,2,3,4}의 상위집합이므로 참이다."""


a={1,2,3,4}
print(a>={1,2,3,4})
# True

print(a.issuperset({1,2,3,4}))
#  True



""" >은 현재 세트가 다른 세트의 진상위집합(proper superset)인지 확인하며 메서드는 없다. 다음은 세트{1,2,3,4}가 {1,2,3}의 
    진상위집합이므로 참이다. 즉, 상위집합이지만 같지 않을 때는 참이다.
    
    
        * 현재세트 > 다른세트
        
"""


a={1,2,3,4}
print(a>{1,2,3})
# True




# 세트가 같은지 다른지 확인하기

""" 세트 == 연산자를 사용하여 서로 같은지 확인할 수 있다. """

a={1,2,3,4}
a=={1,2,3,4}

print(a=={4,2,1,3})
# True

""" != 연산자는 세트가 다른지 확인한다."""

a={1,2,3,4}
print(a!={1,2,3})
# True



# 세트가 겹치지 않는지 확인하기

""" disjoint 현재 세트가 다른 세트와 겹치지 않는지 확인한다. 겹치는 요소가 없으면 True, 있으면 False이다.

    * 현재세트.isdisjoint(다른세트)

"""

a={1,2,3,4}
print(a.isdisjoint({5,6,7,8}))  # 겹치는 요소가 없음
# True

print(a.isdisjoint({3,4,5,6}))  # a와 3, 4가 겹칩
# False



