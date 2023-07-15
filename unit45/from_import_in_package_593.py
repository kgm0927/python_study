# 패키지에서 from import 응용하기

""" 지금까지 calcpkg 패키지의 모듈을 가지고 올 때 import calc.operation 처럼 'import 패키지.모듈'형식으로 가져왔다.
    그러면 import calcpkg처럼 import 패키지 형식으로 패키지만 가져와서 모듈을 사용할 수 있는가? 
    calcpkg 패키지의 __init__.py 파일을 다음과 같이 수정한다.
    
    from . import 모듈
    
"""

""" 파이썬에서 __init__.py 파일은 폴더(디렉터리)가 패키지로 인식되도록 하는 역할도 하고,
    이름 그대로 패키지를 초기화하는 역할도 한다. 즉, import로 패키지를 가져오면 __init__.py
    파일이 실행되므로 이 파일에서 from. import 모듈 형식으로 현재 패키지에서 모듈을 가져오게
    만들어야 한다. 참고로 .(점)은 현재 패키지라는 뜻이다."""



""" 이제 이 파일에서 import calcpkg와 같이 패키지만 가져오도록 수정한 뒤 실행한다."""

import calcpkg

print(calcpkg.operation.add(10,20))
print(calcpkg.operation.mul(10,20))

print(calcpkg.geometry.triangle_area(30,40))
print(calcpkg.geometry.rectangle_area(30,40))

# 30
# 200
# 600.0
# 1200
#
#
#


""" calcpkg의 __init__.py에서 하위 모듈을 함께 가져오게 만들었으므로 import calcpkg로 패키지만 가져와도
    calcpkg.operation.add(10,20)처럼 사용할 수 있다."""



# from import로 패키지에 속한 모든 변수, 함수, 클래스 가져오기

""" 앞에서 from import 문법 중에 *(애스터리스크)를 지정하여 모든 변수, 함수, 클래스를 가져오는 방법이 있었다.
    그럼 패키지에 속한 모든 변수, 함수, 클래스를 가져오려면 어떻게 해야 할까?
    
    먼저 main.py에서 'import calcpkg'를 'from calcpkg import *' 와 같이 수정하고, 각 함수들도 앞에 붙은
    calcpkg.operation, calcpkg.geometry를 삭제한 뒤 실행해본다.
    
    * from 패키지 import *
    """


""" 하지만 이러한 실행을 해 보면 add가 정의되지 않았다면서 에러가 발생한다. 
    왜냐하면 __init__.py에서 모듈만 가져왔을 뿐 안의 함수는 가져오지 않았기 때문이다.
    
    IDLE의 파이썬 프롬프트에서 dir 함수를 호출해서 현재 네임스페이스를 확인해 봐라.
"""



print(dir())

# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calcpkg']


""" 현재 네임스페이스에는 calcpkg (책에서는 operation, geometry가 있다고 하는데 여기서는 조금 다르다. 아마 실행 위치에 따라 다른 것 같다.)만 들어
    있어서 add,mul처럼 함수 이름 만으로 호출할 수가 없다."""


""" 이때는 __init__.py에서 모듈 안의 함수를 가져오게 만들어야 한다. 특히 현재 패키지(calcpkg)라는 것을 명확하게 나타내기
    위해 모듈 앞에 .(점)을 붙인다.
    
    
    
    * from .모듈 import 변수, 함수, 클래스
    
    """

from calcpkg import *   # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴

print(add(10,20))       # operation 모듈의 add 함수 사용
print(mul(10,20))       # operation 모듈의 mul 함수 사용

print(triangle_area(30,40))     # geometry 모듈의 triangle_area 함수 사용
print(rectangle_area(30,40))    # geometry 모듈의 rectnagle_area 함수 사용

# 30
# 200
# 600.0
# 1200




""" 물론 __init__.py 파일에서 특정 함수(변수, 클래스)를 지정하지 않고 *를 사용해서 모든 함수(변수, 클래스)를 가져와도
    상관없다.
    
    * from .모듈 import *
    
"""


# __init__.py의 세 번째 단락
""" 이렇게 패키지의 __init__.py에서 'from.모듈 import 변수,함수,클래스' 또는 'from.모듈 import*' 형식으로 작성했다면 패키지를
    가져오는 스크립트에서는 패키지.함수() 형식으로 사용할 수 있다(변수, 클래스도 같은 형식). 이때는 import calcpkg와 같이 패키지만
    가져오면 된다.
    
    
    * import 패키지
    * 패키지.변수
    * 패키지.함수()
    * 패키지.클래스()"""


import calcpkg              # calcpkg 패키지만 가져옴

print(calcpkg.add(10,20))   # 패키지.함수 형식으로 operation 모듈의 add 함수 사용
print(calcpkg.mul(10,20))   # 패키지.함수 형식으로 operation 모듈의 mul 함수 사용


print(calcpkg.triangle_area(30,40)) # 패키지. 함수 형식으로 geometry 모듈의 triangle_area 함수 사용
print(calcpkg.rectangle_area(30,40))# 패키지. 함수 형식으로 geometry 모듈의 rectangle_area 함수 사용

""" __init.py 에서 from.모듈 import 변수,함수,클래스' 또는 'from.모듈 import*' 형식으로 모듈을 가져오면 calcpkg 패키지의
    네임스페이스에는 add,mul, triangle_area, rectangle_area가 들어간다. 따라서 모듈을 거치지 않고 calcpkg.add처럼 패키지에서
    함수를 바로 사용할 수 있다."""




# 참고 __all__로 필요한 것만 공개하기

""" 패키지의 __init__.py에서 from.모듈 import *로 모든 변수, 함수, 클래스를 가져오면 패키지 외부에 공개하고 싶지 않은 것까지 공개하게
    된다. 이때는 __all__에 공개할 모듈, 변수, 클래스를 리스트 형태로 지정해주면 된다. __all__ 이라는 이름 그대로 모든 것(*)을 가져갈 때에
    목록을 정한다.
    

    


    * __init__.py

    __all__=['add','triangle_area']

    from .operation import *
    from .geometry improt *

    


   * 메인파일.py

    from calcpkg import *   # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴

    print(add(10,20))       # add 함수는 공개되어 있으므로 사용할 수 있음
    print(mul(10,20))       # 에러: mul 함수는 공개되어 있지 않으므로 사용할 수 없음

    print(triangle_area(30,40)) # triangle_area 함수는 공개되어 있으므로 사용할 수 있음
    print(triangle_area(30,40)) # 에러: rectangle_area 함수는 공개되어 있으므로 사용할 수 있음


    메인파일.py에서 from calcpkg import *로 패키지의 모든 변수, 함수, 클래스를 가져온다 하더라도 __all__에 지정된 add, triangle_area 함수만
    사용할 수 있다.

    
    
    """




# 참고: 하위 패키지 사용하기


""" 파이썬의 패키지는 패키지 안에 하위 패키지를 만들 수 있다. 즉, 패키지 안에 폴더(디렉터리)를 만들고 __init__.py와 모듈을 넣으면 하위 패키지가
    된다.
    
    예를 들어서 다음과 같이 calcpkg 안에 operation과 geometry 하위 패키지가 있고, 그 아래에 모듈이 있다.
    


    unit45 --------> 메인파일.py
               \--->operation
                |        |
                |        |
                |        |-> __init__.py
                |        |
                |        |-> element.py  -------> add,mul
                |        |-> logic.py    --------> nand,nor
                |
                |
                |------->geometry.py
                            |
                            |-> __init__.py
                            |-> shape.py --------------> triangle_area, rectangle_area
                            |-> vector.py--------------> product, dot




    import로 하위 패키지의 모듈을 가져올 때는 계층 순서대로 .(점)을 가져오면 된다.


    * import 패키지.하위패키지.모듈

    함수를 사용할 때는 calcpkg.operation.element.add(10,20)이 된다.


    만약, import calcpkg처럼 패키지만 가져와서 사용하고 싶다면 calcpkg/__init__.py에서 하위 패키지의 모듈에 들어있는 변수, 함수, 클래스를
    모두 가져오게 만들면 된다.

    calcpkg/__init__.py
    from .operation.element import *
    from .operation.logic import *
    from .geometry.shape import *
    from .geometry.vector import *


    이렇게 하면 calcpkg.add(10,20), calcpkg.triangle_area(30,40) 또는 , add(10,20), triangle_area(30,40)처럼 사용할 수 있다.


    참고로 하위 패키지 안에서 옆에 있는 패키지의 요소를 가져와서 사용하려면 ..을 사용해야 한다. ..은 상위 폴더(디렉토리)라는 뜻이며
    ..패키지 또는 .. 모듈은 상위 폴더에 있는 패키지, 모듈이라는 뜻이다. 즉, 현재 패키지와 같은 계층의 패키지 또는 모듈이다. 그리고
    ...은 상위 폴더의 상위 폴더 라는 뜻이며 위로 올라갈 수록, .이 하나씩 늘어난다.


    * from ..패키지 import 모듈
    * from ..패키지.모듈 import 클래스, 변수, 함수
    * from ..패키지.모듈 import *
    
    예를 들어 calcpkg/geometry/shape.py에서 옆에 있는 calcpkg/operation 패키지의 element 모듈을 사용한다면 다음과 같이 from ..operation import element
    로 지정해준다. 또는, 'from ..operation.element import mul'과 같이 지정하면 mul을 함수 그대로 사용할 수 있다.
    """




# 참고: 모듈과 패키지의 독스트링


""" 모듈의 독스트링은 모듈 파일의 첫 줄에 큰따옴표 세 개, 작은 따옴표 세 개를 사용하여 문자열을 넣는다."""


""" 패키지의 독스트링은 __init__.py 파일의 첫 줄에  큰따옴표 세 개, 작은 따옴표 세 개를 넣어 문자열을 만든다.

    __init__.py
    
        '''패키지의 독스트링'''
    
    
    모듈과 패키지의 독스트링을 출력하려면 모듈 패키지의 __doc__를 출력하면 된다.

    모듈.__doc__
    패키지.__doc__
    
    """