# iter, next 함수 사용하기


""" iter는 객체의 __iter__ 메서드를 호출해주고, next는 객체의 __next__ 메서드를 호출해준다.
    그럼 range(3)에 iter에 next를 사용해보겠다. """



it=iter(range(3))


print(next(it))
# 0

print(next(it))
# 1

print(next(it))
# 2


""" iter는 반복 가능한 객체에서 이터레이터를 반환하고 next는 이터레이터에서 값을 차례대로 꺼낸다.
    iter와 next를 이런 기능 외에도 다양한 방식으로 사용할 수 있다."""



# iter

""" iter는 반복을 끝낼 값을 지정하면 특정 값이 나올 때 반복을 끝낸다. 이 경우에는 반복 가능한 객체 대시 호출 가능한 객체(callable)를 넣어준다.
    참고로 반복을 끝낼 값은 sentinel이라고 부르는데 감시병이라는 뜻이다. 즉, 반복만을 감시하다가 특정한 값이 나오면 반복을 끝낸다고 해서 sentinal이다.
    
    
    *iter(호출가능한객체, 반복을 끝낼값)
    
    예를 들어 radom.randint(0,5)와 같이 무려 0~5까지 무작위로 숫자를 생성할 때 2가 나오면 반복을 끝내도록 만들 수 있다. 이때 호출 가능한 객체를 넣어야 하므로
    매개변수가 없는 함수 또는 람다 표현식으로 만들어준다."""


import random
it=iter(lambda: random.randint(0,5),2)

"""
print(next(it))
#
print(next(it))

print(next(it))"""


"""next(it)로 숫자를 계속 만들다가 2가 나오면 StopIteration이 발생한다. 물론 숫작 무작위로 생성되었으므로 next(it)를 호출하는 횟수도 달라진다.
    물론 다음과 같이 for 반복문에 넣어서 사용할 수도 있다."""


import random
for i in iter(lambda: random.randint(0,5),2):
    print(i,end=' ')



""" 이렇게 iter 함수를 활용하면 if 조건문으로 매번 숫자가 2인지 검사하지 않아도 되므로 코드가 좀 더 간단해진다. 즉, 다음 코드와 동작이 같다."""

import random

while True:
    i=random.randint(0,5)
    if i==2:
        break
    print(i,end=' ')




# next

""" next는 기본값을 지정할 수 있다. 기본값을 지정하면 반복이 끝나더라도 StopIteration이 발생하지 않고 기본값을 출력한다. 즉, 반복할 수 있을 때는
    해당 값을 출력하고, 반복이 끝났을 때는 기본값을 출력한다.
    
    다음은 range(3)으로 0,1,2 세 번 반복하는데 next에 기본값으로 10을 지정했다.
    
    * next(반복가능한객체, 기본값)"""


it=iter(range(3))

print()
print(next(it,10),next(it,10),next(it,10),next(it,10),sep='\n')

# 0
# 1
# 2
# 10
#
#
#


""" 0,1,2까지 나온 뒤에도 next(it,10)을 호출하면 예외가 발생하지 않고 계속 10이 나온다."""