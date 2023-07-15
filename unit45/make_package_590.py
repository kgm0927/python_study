# 패키지 만들기

""" 이번에는 패키지를 만들어본다. 모듈은 스크립트 파일이 한 개지만 폴더(디렉토리)로 구성되어 있다.
    패키지의 구성은 다음과 같다.
    
    
    unit45 ----------> make_package_590.py
                    \_>    calcpkg
                            |
                            |
                            |-> __init__.py
                            |
                            |
                            |->operation.py
                            |
                            |->geometry.py
                            |
    """


""" 먼저 unit45폴더 안에 calcpkg 폴더를 만든다. 그리고 다음 내용을 calcpkg 폴더 안에 __init__.py 파일로 저장한다."""


""" 폴더(디렉터리) 안에 __init__.py 파일이 있으면 해당 폴더는 패키지로 인식이 된다. 그리고  기본적으로 __init__.py 파일의
    내용은 비워 둘 수 있다.
    (파이썬 3.3 부터는 __init__.py 이 없어도 패키지로 인식이 된다. 하지만 하위 버전에 호환이 되도록 작성하는 것을 권한다.)"""






# 패키지에 모듈 만들기

""" 이제 calcpkg 패키지에 모듈을 두 개 만들갰다. 첫 번째 모듈은 덧셈, 곱셈 함수가 있는 operation 모듈이고, 두번째 모듈은 삼각형, 사각형 넓이 계산 함수가
    들어있는 geometry 모듈이다.
    
    먼저 calcpkg 폴더 안에 operation.py 파일로 저장한다."""




# 패키지 사용하기

""" 이제 스크립트 파일에서 패키지의 모듈을 사용해보겠다. 다음 내용을 프로젝트 폴더(unit45) 안의 make_package_590.py 안에서 실행해 보아라.

    * import 패키지.모듈
    * 패키지.모듈.변수
    * 패키지.모듈.함수()
    * 패키지.모듈.클래스()
"""

import calcpkg.operation            # calcpkg 패키지의 operation 모듈을 가져옴
import calcpkg.geometry             # calcpkg 패키지의 geometry 모듈을 가져옴

print(calcpkg.operation.add(10,20)) # operation 모듈의 add 함수 사용
print(calcpkg.operation.mul(10,20)) # operation 모듈의 mul 함수 사용


print(calcpkg.geometry.triangle_area(30,40))        # geometry 모듈의 triangle_area 함수 사용
print(calcpkg.geometry.rectangle_area(30,40))       # geometry 모듈의 rectangle_area 함수 사용

# 30
# 200
# 600.0
# 1200


""" calcpkg 패키지의 operation 모듈과 geometry 모듈을 가져와서 안에 들어있는 함수를 호출한다.

    이처럼 패키지의 모듈을 가져올 때는 'import 패키지.모듈' 형식으로 가져온다. 그리고 '패키지.모듈.함수()' 형식으로
    모듈의 함수를 사용한다(변수와 클래스도 같은 형식).
"""




# from import로 패키지의 모듈에서 변수, 함수, 클래스 가져오기

""" 물론 패키지의 모듈에서 from import로 함수(변수, 클래스)를 가져온 뒤 패키지와 모듈 이름을 붙이지 않고 사용할 수도 있다.

    * from 패키지.모듈 import 변수
    
    * from 패키지.모듈 import 함수
    
    * from 패키지.모듈 import 클래스
"""


from calcpkg.operation import add, mul

print(add(10,20))
# 30
print(mul(10,20))
# 200



""" 지금까지 만든 make_package_590.py 파일과 calcpkg 패키지의 계층을 나타내면 __main__ 인 make_package_590.py 파일이 있는 폴더에
    calcpkg 패키지가 있고, 그 패키지 않에 __init__.py, operation.py, geometry.py 파일이 있다.
"""



# 참고: 패키지의 모듈과 __name__

""" 패키지의 모듈에서는 __name__ 변수에 패키지.모듈 형식으로 이름이 들어간다. 즉, calcpkg 패키지의 geometry.py에서 __name__의 값을
    출력하도록 만들고, import를 가져오면 'calcpkg.geometry'가 나온다.
"""


# 참고: 모듈과 패키지를 찾는 경로

""" 지금까지 모듈과 패키지는 현재 폴더(디렉토리)에 만들었다. 파이썬에서는 현재 모듈, 패키지가 없다면 다음 경로에 모듈, 패키지를 찾는다."""

import sys

print(sys.path)
""" ['C:\\Users\\kgm09\\OneDrive\\문서\\GitHub\\python_study\\unit45', 
'C:\\Users\\kgm09\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip', 
'C:\\Users\\kgm09\\AppData\\Local\\Programs\\Python\\Python311\\DLLs', 
'C:\\Users\\kgm09\\AppData\\Local\\Programs\\Python\\Python311\\Lib', 
'C:\\Users\\kgm09\\AppData\\Local\\Programs\\Python\\Python311',
 'C:\\Users\\kgm09\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages']

 
    sys 모듈의 path 변수에는 모듈, 패키지를 찾는 경로가 들어있다. 여기서 site-packages 폴더는 pip로 설치한
    패키지가 들어간다. 그리고 자기가 만든 모듈, 패키지도 site-packages 폴더에 넣으면 스크립트 파일이 어디에
    있든 모듈, 패키지를 사용할 수 있다.
    
    만약 가상 환경(virtual environment)을 만들어 모듈과 패키지를 관리하면 가상 환경/Lib/site-packages 폴더에
    모듈과 패키지가 들어간다. 

"""



