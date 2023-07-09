# map에 객체를 여러 개 넣기


""" map은 리스트 등의 반복 가능한 객체를 여러 개 넣을 수도 있다. 다음은 두 리스트의 요소를 곱해서 세 리스트를 만든다."""


a=[1,2,3,4,5]
b=[2,4,6,8,10]
print(list(map(lambda x,y: x*y, a,b)))
# [2,8,18,32,50]


""" 이렇게 리스트 두 개를 처리할 때는 람다 표현식에선 lambda x,y: x*y 처럼 매개변수를 두 개로 지정하면 된다. 그리고 map에 람다 표현식을 넣고
    그 다음에 리스트 두 개를 콤마로 구분해서 넣어준다. 즉, 람다 표현식의 매개변수 개수에 맞게 반복 가능한 객체도 콤마로 구분해서 넣어주면 된다."""





# filter 사용하기


""" 이번에는 filter를 사용해 보겠다. filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데 filter에 지정한 함수의 반환값이 True 일 때만
    해당 요소를 가져온다.
    
    * filter(함수, 반복가능한객체)
    
    
    """


""" 먼저 def로 함수를 만들어서 filter를 사용해본다. 다음은 리스트에서 5보다 크면서 10보다 작은 숫자를 가져온다."""

a=[8,3,2,10,15,7,1,9,0,11]

def f(x):
    return x>5 and x<10

print(list(filter(f,a)))
# [8, 7, 9]



""" 리스트 a에서 8,7,9를 가져왔다. 즉 filter는 x>5 and x<10의 결과가 참인 요소만 가져오고 거짓인 요소는 버린다."""


""" 그럼 함수 f를 람다 표현식으로 만들어서 filter에 넣어본다."""


a=[8,3,2,10,15,7,1,9,0,11]
print(list(filter(lambda x:x>5 and x<10,a)))
# [8, 7, 9]



""" 람다표현식 lambda x: x>5 and x <10 을 filter에 넣어서 5보다 크면 10 보다 작은 수를 가져오도록 한다."""




# reduce 사용하기


""" 마지막으로 reduce를 사용해보겠다. reduce는 반복이 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수이다. 
    (reduce는 파이썬3부터 내장함수가 아니다. 그래서 functools 모듈에서 reduce 함수를 가져와야 한다. )
    
    * from functools import reduce
    * reduce(함수, 반복가능한객체)
    
    
    """

def f(x,y):
    return x+y


a=[1,2,3,4,5]
from functools import reduce
print(reduce(f,a))
# 15



""" reduce의 반환값이 15가 나왔다. 함수 f에서 x+y를 반환하도록 만들었으므로 reduce는 그림과 가이 요소 두 개를 계속 더하면서 결과를 누적한다."""
""" 이제 함수 f를 표현시긍로 만들어서 reduce에 넣어보겠다."""

a=[1,2,3,4,5]
from functools import reduce
reduce(lambda x,y:x+y,a)
# 15



""" lambda x,y:x+y와 같이 매개변수 x,y를 지정한 뒤 x와 y를 더한 결과를 반환하도록 만든다."""





# 참고 : map, filter, reduce 리스트 표현식


""" 리스트(딕셔너리, 세트) 표현식으로 처리할 수 있는 경우에는 map, filter와 람다 표현식 대신 리스트 표현식을 사용하는 것이 좋다.
    list(filter(lambda x: x>5 and x<10 ,a))는 다음과 같이 리스트 표현식으로도 만들 수 있다."""


a=[8,3,2,10,15,7,1,9,0,11]
print([i for i in a if i>5 and i<10])
# [8, 7, 9]


""" 리스트 표현식이 좀 더 알아보기 수비고 속도도 더 빠르다. 또한, for, while 반복문으로 처리할 수 있는 경우에는 reduce 대신, for, while을 사용하는
    것이 좋다. 왜냐하면 reduce는 코드가 조금만 복잡해저도 의미하는 바를 한눈에 알아보기가 힘들기 때문이다. 이러한 이유로 파이썬 3 부터는 reduce가 내장
    함수에서 제외되었다."""