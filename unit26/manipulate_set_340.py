# 세트 조작하기

""" 이번에는 세트를 조작하는 메서드와 세트의 길이(요소 개수)를 구하는 방법을 알아본다."""



# 세트에 요소를 추가하기

""" add(요소)는 세트에 요소를 추가한다."""

a={1,2,3,4}
a.add(5)
print(a)
# {1, 2, 3, 4, 5}


# 세트에서 특정 요소를 삭제하기

""" remove(요소)는 세트에서 특정 요소를 삭제하고 요소가 없으면
    에러를 발생한다."""


a.remove(3)
print(a)



""" discard(요소)는 세트에서 특정 요소를 삭제하고 요소가 없으면 그냥 넘어간다. 다음은 세트 a에 2가 있으므로
    2를 삭제하고, 3은 없으므로 그냥 넘어간다."""

a.discard(2)
print(a)
# {1,4,5}

a.discard(3)
print(a)
# {1,4,5}




# 세트에서 임의의 요소를 삭제하기

""" pop()은 세트에서 임의의 요소를 삭제하고 해당 요소를 반환한다. 없으면 에러를 발생한다. """

a={1,2,3,4}
print(a.pop())
# 1

print(a)
# {2, 3, 4}


# 세트의 모든 요소를 삭제하기

""" clear()는 세트에서 모든 요소를 삭제한다."""

a.clear()
print(a)



# 세트의 요소 개수 정하기
""" 지금까지 리스트, 튜플, 문자열, range, 딕셔너리의 요소 개수를 구할 때 len 함수를 쓴다. 
    마찬가지로 len(세트)는 요소 개수(길이)를 구한다."""

a={1,2,3,4}
print(len(a))



# 세트의 할당과 복사
""" 세트도 리스트, 딕셔너리처럼 할당과 복사의 차이점이 있다. 먼저 세트를 만든 뒤 다른 변수에 할당한다."""

a={1,2,3,4}
b=a

""" b=a와 같이 세트를 다른 변수에 할당하면 세트는 두 개가 될 것 같지만 실제로는 세트가 한 개이다. a와 b를 is 연산자로
    비교해보면 True가 나온다. 즉, 변수 이름만 다를 뿐 세트 a와 b는 같은 객체다."""

print(a is b)


""" a와 b는 같으므로 b에 요소를 추가하면 세트 a와 b에 모두 반영이 된다."""
b.add(5)

print(a)
# {1, 2, 3, 4, 5}

print(b)
# {1, 2, 3, 4, 5}



""" 세트 a와 c를 완전히 두 개로 만들려면 copy메서드로 모든 요소를 복사해야 한다."""

a={1,2,3,4}
b=a.copy()


""" 이제 a와 b를 is 연산자로 비교해보면 False가 나온다. 즉, 두 세트는 다른 객체이다 그러나
복사한 요소는 같으므로  ==로 비교하면 True가 나온다. """

print(a is b)
# False

print(a==b)
# True



