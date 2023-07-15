# 모듈과 패키지 사용하기


""" 지금까지 파이썬 코드를 작성하면서 내장 함수(built-in function)를 주로 사용했는데, 주로 사용했는데, 내장 함수 만으로는 할 수 있는 게
    별로 없다. 그래서 좀 더 복잡한 프로그램을 만들렴년 파이썬의 모듈과 패키지를 사용해야 한다."""


""" 모듈(module)은 각종 변수, 함수, 클래스를 담고 있는 파일이고, 패키지(package)는 여러 모듈을 묶은 것이다. 파이썬을 설치할 대 다양한 모듈과
    패키지가 기본으로 설치가 된다. 만약 기본 모듈과 패키지로 부족하다면 다른 사람이 만든 유명 모듈과 패키지를 설치해서 쓸 수도 있다."""


# 참고: 모듈, 패키지, 라이브러리

""" 파이썬을 배우다 보면 모듈, 패키지, 파이썬 표준 라이브러리와 같은 용어를 접하게 되는데 서로 비슷한 개념이지만 약간의 차이가 있다.

    * 모듈: 특정 기능을 .py 파일 단위로 작성한 것이다.
    * 패키지: 특정 기능과 관련된 여러 모듈을 묶은 것이다. 패키지는 모듈에 네임스페이스(namespace, 이름공간)를 제공한다.
    * 파이썬 표준 라이브러리: 파이썬에 기본으로 설치된 모듈과 패키지, 내장 함수를 묶으로 파이선 표준 라이브러리(Python Standard Library, PSL)
                            라 부른다.

                            
"""


# bring_module(모듈 가져오기)

""" 모듈 import 키워드로 가져올 수 있다(모듈을 여러 개 가져올 때는 모듈을 콤마로 구분).


    * import 모듈
    * import 모듈1, 모듈2
    * 모듈.변수
    * 모듈.함수()
    * 모듈.클래스()
    
"""

""" 그럼 간단하게 파이선 표준 라이브러리의 수학 모듈 math를 가져와서 원주율을 출력해본다."""

import math

print(math.pi)
# 3.141592653589793


""" import에 모듈 이름을 지정하면 해당 모듈을 가져올 수 있으며 maht.pi와 같이 모듈.변수 형식으로
    모듈의 변수를 사용한다.
"""

print(math.sqrt(4.0))
# 2.0

print(math.sqrt(2.0))
# 1.4142135623730951


""" 모듈의 함수는 math.sqrt(4.0)와 같이 모듈.함수() 형식으로 사용한다."""

# 잠시 알아 두어야 할 것

"""
    * ModuleNotFoundError: No module named ...: 모듈의 이름이 잘못되었을 때 발생하는 에러이다. 모듈 이름이
                                                맞는지 확인해라.

    * AttributeError: module ... has no attribute ...: 

"""
    
# import as로 모듈 이름 지정하기


""" 모듈의 함수를 사용할 때 math.sqrt처럼 일일이 math를 입력하기 귀찮은 경우도 있을 것이다. 이때는 import as를 사용하여 모듈의 이름을
    지정할 수 있다.
    
    * import 모듈 as 이름

    이제 math 모듈을 m으로 줄여보겠다.
    """


import math as m    # math 모듈을 가져오면서 이름을 m으로 지정
print(m.sqrt(4.0))
# 2.0
print(m.sqrt(2.0))  # m으로 제곱근 함수 사용
# 1.4142135623730951


""" import math as m과 같이 모듈을 가져오면서 as 뒤에 이름을 지정해 준다. 이후 math 모듈을 사용할 때 m으로 줄여서 사용할 수 있다."""



# from import로 모듈의 일부만 가져오기

""" import as로 모듈의 이름을 지정하는 방법보다 좀 더 편한 방법이 있다. 이번에는 from import로 원하는 변수만 가져와 보겠다.
    
    * from 모듈 import 변수
    
    다음은 math 모듈에서 변수 pi만 가져와 본다.
"""

from math import pi

print(pi)
# 3.141592653589793



""" from math import pi와 같이 from 뒤에 모듈 이름을 지정하고 import 뒤에 가져올 변수를 입력한다. 이후 가져온 변수를
    사용할 때는 pi와 같이 모듈 이름을 붙이지 않고 바로 사용하면 된다.
    
    모듈의 변수를 가져왔으니 이번에는 함수를 가져와 보겠다. (물론 클래스도 가져올 수 있다.)
    
        * from 모듈 import 함수 
        * from 모듈 import 클래스
    
    다음은 math 모듈에서 sqrt 함수만 가져온다.
"""

from math import sqrt # math 모듈에서 sqrt 함수만 가져옴
print(sqrt(4.0))      # sqrt 함수를 바로 사용
# 2.0

print(sqrt(2.0))        # sqrt 함수를 바로 사용
# 1.4142135623730951


""" math 모듈에서 sqrt 함수만 가져왔으므로 sqrt(4.0)처럼 앞에 math를 붙이지 않고 함수를 바로 사용할 수 있다.

    지금까지 변수나 함수를 하나만 가져왔다. 하지만 math 모듈에서 가져올 변수와 함수와 여러 개일 수도 있다.
    이때는 import 뒤에 가져올 변수, 함수, 클래스를 콤마로 구분하여 여러 개를 지정해주면 된다.
    
    * from 모듈 import 변수, 함수, 클래스
    
    다음은 math 모듈에서 pi, sqrt를 가져온다.
"""


from math import pi, sqrt           # math  모듈에서 pi, sqrt를 가져옴

print(pi)                           # pi로 원주율 출력
# 3.141592653589793


print(sqrt(4.0))                    # sqrt 함수 사용
# 2.0
print(sqrt(2.0))                    # sqrt 함수 사용
# 1.4142135623730951                              





""" from math import pi, sqrt와 같이 pi와 sqrt 두 개를 가져왔다. 하지만 변수, 함수, 클래스가 두세개라면 괜찮지만
    수십 개가 된다면 입력하기가 상당히 번거롭다.
    
    from import는 모듈의 모든 변수, 함수, 클래스를 가져오는 기능도 있다.
    
    
    * from 모듈 import *
"""

from math import *  # math 모듈의 모든 변수, 함수, 클래스를 가져옴

print(pi)           # pi로 원주율 출력
# 3.141592653589793
print(sqrt(4.0))    # sqrt 함수 사용
# 2.0

print(sqrt(2.0))    # sqrt 함수 사용
# 1.4142135623730951

""" from math import * 와 같이 지정하면 math 모듈의 모든 함수, 클래스를 가져온다(보통
    컴퓨터에서 *(asterisk, 애스터리스크)기호는 모든 것이라는 뜻으로 사용한다.)."""





# from import로 모듈의 일부를 가져온 뒤 이름 지정하기

""" 이번에는 from import로 변수, 함수, 클래스를 가져온 뒤 이름을 지정해 보겠다.
    
    
    * from 모듈 import 변수 as 이름
    * from 모듈 import 함수 as 이름
    * from 모듈 import 클래스 as 이름


    다음은 math 모듈에서 sqrt 함수를 가져오면서 이름을 s로 지정한다.
    
    """

from math import sqrt as s      # math 모듈에서 sqrt 함수를 가져오면서 이름을 s로 지정


print(s(4.0))                   # s로 sqrt 함수 사용
#  2.0
print(s(2.0))                   # s로 sqrt 함수 사용
# 1.4142135623730951



""" from import로 가져온 변수, 함수, 클래스 뒤에 as로 이름을 지정해주면 된다."""


""" 여러 개를 가져왔을 때 각각 이름을 지정할 수는 없을까? 이때는 각 변수, 함수, 클래스 등을 콤마로 구분하여 as를 여러 개 지정하면 된다.

    * from 모듈 import 변수 as 이름1, 함수 as 이름2, 클래스 as 이름3
    
    
    다음은 math 모듈의 pi를 가져오면서 이름을 p로, sqrt를 가져오면서 이름을 s로 지정한다.
    """


from math import pi as p, sqrt as s

print(p)
# 3.141592653589793
print(s(4.0))
# 2.0

print(s(2.0))
# 1.4142135623730951


""" 이렇게 as를 사용하면 모듈의 이름을 원하는 대로 지정해서 사용할 수 있다."""





# 참고: 가져온 모듈 해체하기, 다시 가져오기

""" import로 가져온 모듈(변수, 함수, 클래스)은 del로 해제할 수 있다."""

import math
del math

"""모듈을 다시 가져오려면 importlib.reload를 사용한다."""


import importlib
import math
importlib.reload(math)