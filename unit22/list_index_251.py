""" 리스트에서 특정 값의 인덱스"""


""" index(값)은 리스트에서 특정 값의 인덱스를 구한다. 이때 같은 값이 여러
개일 경우 처음 찾은 인덱스를 구한다. 다음은 20이 두 번째에 있으므로 인덱스 1이
나온다."""

a=[10,20,30,15,20,40]
print(a.index(10))



""" 특정 값의 개수 구하기"""


"""count(값)은 리스트에서 특정 값의 개수를 구한다. 다음은 리스트 [10,20,30,15,40]에서 20의
개수를 구한다."""

a=[10,20,30,15,20,40]
print(a.count(20))



"""리스트의 순서를 뒤집기"""


""" reverse()는 리스트에서 요소의 순서를 반대로 뒤집는다. 다음은 리스트
[10,20,30,15,20,40]의 순서를 반대로 뒤집어서 [40,20,15,30,20,10]이 된다."""

a=[10,20,30,15,20,40]
a.reverse()
print(a)


"""리스트의 요소를 정렬하기"""

"""sort()는 리스트의 요소를 작은 순서대로 정렬한다. 다음은 리스트
[10,20,30,15,20,40]의 값을 작은 순서대로 정렬하여 [10,15,20,20,30,40]이
된다."""

a=[10,20,30,15,20,40]
a.sort()
print(a)


# 참고
""" 파이썬은 리스트의 sort 메서드 뿐만 아니라 내장 함수 sorted도 제공한다.
sort와 sorted 모두 정렬을 해주는 함수지만, 약간 차이점이 있다. sort는 메서드를
사용한 리스트를 변경하지만, sorted 함수는 정렬된 새 리스트를 생성한다."""

a=[10,20,30,15,20,40]
a.sort()
print(a)

b=[10,20,30,15,20,40]
c=sorted(b)
print(c)


""" 리스트의 모든 요소를 삭제하기."""

"""clear()는 리스트의 모든 요소를 삭제한다. 다음은 리스트 [10,20,30]의 모든 요소를 삭제하여 빈 리스트 []가
된다."""

a=[10,20,30]
a.clear()
print(a)


"""clear 대신 del a[:]와 같이 시작, 끝 인덱스를 생략하여 모든 요소를 삭제할 수도 있다."""
a=[10,20,30]
del a[:]
print(a)


"""리스트를 슬라이스로 조작하기."""

"""리스트는 메서드를 사용하지 않고, 슬라이스로 조작할 수 있다. 다음은 리스트 끝에 값이 한 개 들어있는 리스트를 추가한다."""

a=[10,20,30]
a[len(a):]=[500]
print(a)


"""a[len(a):]는 시작 인덱스를 len(a)로 지정해서 리스트의 마지막 인덱스보타 1이 더 큰 상태이다.
즉, 그림과 리스트 끝에서 시작하겠다는 뜻이다."""


"""a[len(a):]=[500]과 같이 값이 한개 들어있는 리스트를 할당하면 리스트 a 끝에 값을 한 개 추가하여 
a.append(500)과 같다.

그리고 a[len(a):]=[500,600]과 같이 요소가 여러 개 들어있는 리스틀르 할당하면 리스트 a 끝에 다른 리스트를
연결하여 a.extend([500,600])과 같다."""

a=[10,20,30]
a[len(a):]=[500,600]
print(a)


# 리스트가 비어 있는지 확인하기

"""시퀀스 객체가 비어 있는지 확인하려면 어떻게 해야 하는가? len()함수를 이용하여 리스트가 비어 있는지 확인할 수 있다."""

""" 하지만 파이썬에서는 이 방법보다 리스트를 바로 if 조건문으로 판단하는 것이 좋다."""

# if not seq:
# if seq:
