# 딕셔너리의 할당과 복사

""" 리스트와 마찬가지로 딕셔너리도 할당과 복사는 큰 차이점이 있다. 먼저 딕셔너리를 만든 뒤 다른 변수에 할당을 한다."""

x={'a':0,'b':0,'c':0,'d':0}
y=x


"""y=x와 같이 딕셔너리를 다른 변수에 할당하면 딕셔너리는 두 개가 될 것 같지만 실제로는 딕셔너리가 한 개이다."""

"""x와 y를 is 연산자로 비교해보면 True가 나온다. 즉, 변수 이름만 다른 뿐 딕셔너리 x와 y는 같은 객체이다."""

print(x is y)

# True


""" x와 y는 같으므로 y['a']=99와 같이 키 'a'의 값을 변경하면 딕셔너리 x와 y에 모두 반영이 된다."""

y['a']=99
print(x)
# {'a': 99, 'b': 0, 'c': 0, 'd': 0}
print(y)
# {'a': 99, 'b': 0, 'c': 0, 'd': 0}





""" 만약에 x와 y를 완전히 두 개로 만들려면 copy 메서드로 모든 키-값 쌍을 복사해야 한다."""

x={'a':0,'b':0,'c':0,'d':0}
z=x.copy()


""" 이제 x와 z를 is 연산자로 비교해보면 False가 나온다. 즉, 두 딕셔너리는 다른 객체이다. 그러나 복사한 키-값 쌍은 같으므로 ==로 비교를 하면 True가 나온다.
    (is 키워드는 말 그대로 x와 다른 리스트 객체의 레퍼런스가 같은지 확인하는 키워드이다.)

"""

print(x is z)
# False
print(x==z)
# True



# 중첩 딕셔너리의 할당과 복사 알아보기

""" 그러면 딕셔너리 안에 딕셔너리가 들어있는 중첩 딕셔너리도 copy 메서드로 복사하면 어떻게 될까? 다음과 같이 중첩 딕셔너리를 만든 뒤 
copy 메서드로 복사한다."""

x={'a':{'python':'2.7'},'b':{'python':'3.6'}}
y=x.copy()


""" 이제 y['a']['python']='2.7.15'와 같이 y의 값을 변경해보면 x와 y에 모두 반영이 된다."""
y['a']['python']='2.7.15'

print(x)
# {'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}
print(y)
# {'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}



""" 중첩 딕셔너리를 완전히 복사하려면 copy 메서드 대신 copy 모듈의 deepcopy 함수를 사용해야 한다."""

x={'a':{'python':'2.7'},'b':{'python':'3.6'}}
import copy
y=copy.deepcopy(x)
y['a']['python']='2.7.15'


print(x)
# {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}

print(y)
# {'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}


""" 이제 딕셔너리 y의 값을 변경해도 딕셔너리 x에는 영향을 미치지 않는다. copy.deepcopy 함수는 중첩된 딕셔너리에 들어있는 모든 딕셔너리를 복사하는
깊은 복사(deepcopy)를 해 준다."""