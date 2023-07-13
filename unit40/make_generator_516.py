# 제너레이터 만들기


""" 제너레이터와 yield에 대해 알아보았으니 이번에는 range(횟수)처럼 동작을 하는 제너레이터를 만들어보겠다."""


def number_generator(stop):
    n=0             # 숫자는 0부터 시작
    while n<stop:   # 현재 숫자가 반복을 끝낼 숫자보다 작을 때 반복
        yield n     # 현재 숫자를 바깥으로 전달
        n+=1        # 현재 숫자를 증가시킴


for i in number_generator(3):
    print(i)



""" 제너레이터 안에서 변수 n을 만들고 0을 저장한다. 그리고 while n< stop:과 같이 반복을 끝낼 숫자보다 작을 때
    반복하도록 한다. 반복문 안에서는 yield n으로 숫자를 바깥으로 전달한 뒤 n을 1 증가시키면 된다. 여기서는 yield가
    3번 나오므로 for 반복문도 3번 반복한다."""


""" 물론 next 함수(__next__ 메서드)도 3번 사용할 수 있다."""


g=number_generator(3)

print(next(g))
# 0

print(next(g))
# 1

print(next(g))
# 2

""" print(next(g))"""
# 오류



# yield에서 함수 호출하기

""" 그럼 yield에서 함수(메서드)를 호출하면 어떻게 될까? 다음은 리스트에 들어있는 문자열을 대문자로 변환하여 함수 바깥으로 전달한다."""


def upper_generator(x):
    for i in x:
        yield i.upper()     # 함수의 반환값으로 바깥으로 전달

fruits=['apple','pear','pineapple','orange']

for i in upper_generator(fruits):
    print(i)



""" 리스트 fruits에 들어있는 문자열이 모두 대문자로 출력되었다. yield i,upper()와 같이 yield에서 함수(메서드)를 호출하면 해당 함수의
    반환값을 바깥으로 전달한다. upper는 호출했을 때 대문자로 된 문자열을 반환하므로 yield는 이 문자열을 바깥으로 전달한다. 즉, yield에
    무엇을 지정하든 결과만 바깥으로 전달한다(함수의 반환값, 식의 결과).
    
    
    이처럼 yield의 동작 방식만 이해하면 이터레이터보다 훨씬 간단하게 만들 수 있다."""