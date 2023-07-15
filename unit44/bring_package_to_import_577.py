# import로 패키지 가져오기


""" 패키지는 특정 기능과 관련된 여러 모듈을 묶은 것인데, 패키지에 들어있는 모듈도 import를 사용하여 가져온다.
    (패키지는 일종의 디렉토리 형태로 이루어져 있다.)
    
    * import 패키지.모듈
    
    * import 패키지.모듈1, 패키지.모듈2
    
    * 패키지.모듈.함수()
    
    * 패키지.모듈.함수()
    
    * 패키지.모듈.변수

"""


""" 여기서는 파이썬 표준 라이브러리에서 urllib 패키지의 request 모듈을 가져와 보겠다.(urllib은 url 처리에 관련된 모듈을 모아 놓은 패키지이다.)
"""


import urllib.request

response=urllib.request.urlopen('http://www.google.co.kr')

print(response.status)
# 200

""" 패키지에 들어있는 모듈은 import urlib.request와 같이 '패키지.모듈' 형식으로 가져온다. 마찬가지로 모듈의 함수를 사용할 때도 urllib.request.urlopen()
    과  같이 '패키지.모듈.함수()' 형식으로 패키지 이름과 모듈 이름을 모두 입력해준다."""



# 참고: urlopen 함수

""" urllib.request.urlopen은 url을 여는 함수인데 url 열기에 성공하면 response.status의 값이 200이 나온다. 이 200은
    HTTP 상태 코드이며 웹 서버가 요청을 제대로 처리했다는 의미이다."""




# import as로 패키지 모듈 이름 지정하기

""" 패키지 안에 들어있는 모듈도 import as를 사용하여 이름을 지정할 수 있다.

    * import 패키지.모듈 as 이름
    
    다음은 urllib 패키지의 request 모듈을 가져오면서 이름을 r로 정한다."""


import urllib.request as r          # urllib 패키지의 request 모듈을 가져오면서
                                    # 이름을 r로 지정
response=r.urlopen('http://www.google.co.kr')       # r로 urlopen 함수 사용

print(response.status)
# 200


""" 패키지 이름에 모듈 이름까지 더하면 상당히 길어지는데 import as를 사용하니 코드가 더 간단해진다."""




# from import로 패키지의 모듈에서 일부만 가져오기

""" 패키지도 from import를 사용하여 모듈에서 변수, 함수, 클래스를 가져올 수 있다.

    
    * from 패키지.모듈 import 변수
    
    * from 패키지.모듈 import 클래스
    
    * from 패키지.모듈 import 함수
   
    * from 패키지.모듈 import 변수, 함수, 클래스
    
"""


""" 다시 urllib 패키지의 request 모듈에서 urlopen 함수와 Request 클래스를 가져와 보겠다."""

from urllib.request import Request, urlopen     # urlopen 함수, Request 클래스를 가져옴

req=Request('http://www.google.co.kr')           # Request 클래스를 사용하여 req 생성
response=urlopen(req)                            # urlopen 함수 사용
print(response.status)       
# 200



""" 참고로 urlopen 함수에 url을 바로 넣어도 되고, Request('http://www.google.co.kr')와 같이
    Request 클래스에 URL을 넣은 뒤에 req를 생성해서 urlopen 함수에 넣어도 된다.
    
    패키지의 모듈에서 모든 변수, 함수, 클래스를 가져오는 방법은 다음과 같다.
    
    * from 패키지.모듈 import*
    
    
    다음은 urllib의 request 모듈에서 모든 변수, 함수, 클래스를 가져온다.
    
    """



from urllib.request import *

req=Request('http://www.google.co.kr')
response=urlopen(req)

print(response.status)
# 200



# from import로 패키지의 모듈의 일부를 가져온 뒤 이름 지정하기

""" 이번 from import로 패키지의 모듈에서 변수, 함수, 클래스를 가져온 뒤 이름을 지정해본다.
    
    * from 패키지.모듈 import 변수 as 이름
    * from 패키지.모듈 import 변수 as 이름, 함수 as 이름, 클래스 as 이름
    
    
    다음은 urllib 패키지의 request 모듈에서 Request 클래스를 가져온 뒤 이름을 r로 지정하고, urlopen 함수를 가져온뒤 이름을 
    u로 지정한다.
    
"""

from urllib.request import Request as r, urlopen as u
req=r('http://www.google.co.kr')    # r로 Request 클래스 사용
response=u(req)                     # u로 urlopen 함수 사용
print(response.status)
# 200



# pip_package (파이썬 패키지 인덱스에서 패키지 설지하기) 다음 챕터이나 이것은 생략하겠다.