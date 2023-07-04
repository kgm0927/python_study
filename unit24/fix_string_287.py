# 문자열 조작하기

"""replace('바꿀문자열','새문자열')은 문자열 안의 문자열을 다른 문자열로 바꾼다.(문자열 자체는 변경하지 않으며 바뀐 결과를 반환한다.)
 다음은 문자열 'Hello, world!'에서 'world'를 'Python'으로 바꾼 뒤 결과를 반환한다."""

print("Hello world!".replace("world","Python"))

"""만약 바뀐 결괄르 유지하고 싶다면 문자열이 저장된 변수에 replace를 사용한 뒤 변수에 할당해주면 된다."""

s='Hello, world!'
s=s.replace('world!','Python')
print(s)



# 문자 바꾸기

""" translate는 문자열 안의 문자를 다른 문자로 바꾼다. 먼저 str.maketrans('바꿀문자','새문자')로 변환 테이블을 만든다.
그 다음에 translate(테이블)을 사용하면 문자를 바꾼 뒤 결과를 반환한다. 다음은 문자열 'apple'에서 a를 1, e를 2, i를 3, o를 4, u를 5로 바꾼다."""

table=str.maketrans('aeiou','12345')
print('apple'.translate(table))





# 문자열 분리하기


""" split()은 공백을 기준으로 문자열을 분리하여 리스트로 만든다. 지금까지 input으로 문자열을 입력받은 뒤 리스트로 만든 메서드가 바로 이 split이다."""

print('apple pear grape pineapple orange'.split())


"""split()과 같이 기준 문자열을 지정하면 기준 문자열로 문자열을 분리한다. 즉, 문자열에서 각 단어가
,(콤마)와 공백으로 구분되어 있을 때 ', '으로 문자열을 분리하면 단어만 리스트로 만든다."""


print('apple, prear, grape, pineapple, orange'.split(', '))


