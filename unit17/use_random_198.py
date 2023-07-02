"""이번에는 난수를 생성해서 숫자에 따라 반복을 끝내
보겠다. 난수란 특정 주기로 반복되지 않으며 규치없이 무작위로 나열되는 숫자를
의미한다."""

"""파이썬에서 난수를 생성하려면 random 모듈이 필요하다. 모듈은 다음과 같이 import 키워드를 사용하여 가져올 수 있다."""

import random # random 모듈을 가져옴

print(random.random())

print(random.random())
print(random.random())



"""random 모듈의 randint 함수를 사용해 보아야 한다. 다음과 같이 randint 함수는 난수를 생성할 범위를
지정하며, 범위에 지정한 숫자도 난수에 포함이 된다."""

print(random.randint(1,6))
print(random.randint(1,6))
print(random.randint(1,6))


"""random.chioce"""

"""random.chioce 함수를 사용하면 시퀀스 객체에서 요소를 무작위로 선택할 수 있다. 다음은 1,2,3,4,5,6이 들어있는 리스트에서 무작위로 숫자를 선택한다."""


dice=[1,2,3,4,5,6]
print(random.choice(dice))


# 참고
# NameError: name 'true' is not defined: True 첫 글자만 대문자이다. T를 소문자로 입력하지 않았는지, 전부 대문자로 입력하지 않았는지 확인해야 한다.