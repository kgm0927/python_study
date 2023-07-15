# __init__.py 파일은 비워도 된다.

"""
from . import operation # 현재 패키지에서 operation 모듈을 가져옴
from . import geometry  # 현재 패키지에서 geometry 모듈을 가져옴


"""
# 현재 패키지의 operation, geometry 모듈에서 각 함수를 가져옴
"""from .operation import add,mul
from .geometry import triangle_area,rectangle_area
"""



from .operation import *        # 현재 패키지의 operation 모듈에서
                                # 모든 변수, 함수, 클래스를 가져옴
from .geometry import *         # 현재 패키지의 geometry 모듈에서
                                # 모든 변수, 함수, 패키지를 가져옴






                              