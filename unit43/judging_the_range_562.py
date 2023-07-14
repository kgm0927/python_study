# 범위 판단하기 

""" 이번에는 문자열이 숫자로 되어있는지 판단해 본다. 다음과 같이 [](대괄호)안에 숫자 범위를 넣으며* 또는 +를 붙인다.
    숫자 범위는 0-9처럼 표현하며 *는 문자(숫자)가 0개 이상 있는지, +는 1개 이상 있는지 판단한다.
    
    
    
    * [0-9]*
    
    * [0-9]+"""

import re
print(re.match('[0-9]*','1234'))
    # 1234는 0부터 9까지 숫자가 0개 이상 있으므로 패턴에 매칭됨
    # <re.Match object; span=(0, 5), match='Hello'>
print(re.match('[0-9]+','1234'))
    # 1234는 0부터 9까지 숫자가 1개 이상 있으므로 패턴에 매칭됨
    # <re.Match object; span=(7, 13), match='world!'>

print(re.match('[0-9]+','abcd'))
    # abcd는 0부터 9까지 숫자가 1개 이상 없으므로 패턴에 매칭됨
    # <re.Match object; span=(0, 5), match='hello'>


print()
print()
""" 그럼 *와 +는 어디에 활용하겠는가? 다음과 같이 a*b와 a+b를 확인해보녀 쉽게 알 수 있다."""

print(re.match('a*b','b')) # b에는 a가 0개 이상 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 1), match='b'>
print(re.match('a+b','b')) # b에는 a가 1개 이상 없으므로 패턴에 매칭되지 않음
# None
print(re.match('a*b','aab')) # aab에는 a가 0개 이상 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 3), match='aab'>
print(re.match('a+b','aab')) # aab는 a가 1개 이상 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 3), match='aab'>



""" a*b,a+b에서 b는 무조건 있어야 하는 문자고, a*는 a가 0개 이상 있어야 하므로 b는 매칭이 된다. 하지만 a+는 a가 1개 이상
    있어야 하므로 b는 매칭되지 않는다. 그리고 'ab', 'aab', 'aaab' 처럼 a가 0개 이상 또는 1개 이상 있을 때는 a*b와 a+b를 모두 만족한다."""



# 문자가 한 개만 있는지 판단하기

""" 문자가 여러 개 있는지 판단할 때는 *과 +를 사용했지만, 문자가 1 개만 있는지 판단할 때는 어떻게 해야 할까?
    이때는 ?와 .를 사용한다. 
    ?는 ? 앞의 문자(범위)가 0개 또는 1개인지 판단하고, 
    .은 .이 있는 위치에 아무 문자(숫자)가 1개 있는지 판단한다.
    
        * 문자?

        * [0-9]?
    
    """


print(re.match('abc?d','abd'))      # abd에서 c 위치에 c가 0개 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 3), match='abd'>
print(re.match('ab[0-9]?c','ab3c')) # [0-9] 위치에 숫자가 1개 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 4), match='ab3c'>
print(re.match('ab.d','abxd'))      # . 이 있는 위치에 문자가 1개 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 4), match='abxd'>






# 문자 개수 판단하기

""" 그럼 문자(숫자)가 정확히 몇 개 있는지 판단하고 싶을 수 있다. 이때는 문자 뒤에 {개수} 형식을 지정한다.
    문자열의 경우에는 문자열을 괄호로 묶고 뒤에{개수} 형식을 지정한다.
    
    * 문자{개수}
    
    * (문자열){개수}
    
    h{3}은 h가 3개 있는지 판단하고, (hello){3}은 hello가 3개 있는지 판단한다."""



print(re.match('h{3}','hhhello'))
# <re.Match object; span=(0, 3), match='hhh'>

print(re.match('(hello){3}','hellohellohelloworld'))
# <re.Match object; span=(0, 15), match='hellohellohello'>



""" 특정 범위의 문자(숫자)가 몇 개 있는지 판단할 수도 있다. 이때는 범위 [] 뒤에 {개수} 형식을 지정한다.

        *[0-9]개수
        
"""

print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}','010-0000-1000')) # 숫자 3개 -4개 -4개
# <re.Match object; span=(0, 13), match='010-0000-1000'>        # 패턴에 매칭됨

print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}','010-1000-100'))    # 숫자 3개-4개-4개
# None                                                          # 패턴에 매칭되지 않음




""" 이 기능은 문자(숫자)의 개수 범위도 지정할 수 있다. {시작개수, 끝개수} 형식으로 시작 개수와 끝 개수를
    지정해주면 특정 개수 사이에 들어가는지 판단한다.
    
    
        * (문자){시작개수, 끝 개수}

        * (문자){시작개수, 끝 개수}

        * (문자){시작개수, 끝 개수}
    
    """

print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}','02-100-1000')) # 2~3개 -3~4개 -4개
# <re.Match object; span=(0, 11), match='02-100-1000'>          # 패턴에 매칭됨

print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}','02-10-1000'))  # 2~3개-3~4개 -4개
# None                                                          # 패턴에 매칭되지 않음





# 숫자와 영문 문자를 조합해서 판단하기

""" 지금까지 숫자 범위만 판단해 보았으니 이제 숫자와 영문 문자를 조합해서 판단해보겠다. 영문 문자 범위는
    a-z, A-Z와 같이 표현한다.
    
    * a-z
    * A-Z
    
    
    """


print(re.match('[a-zA-Z0-9]+','Hello1234')) # a부터 z, A부터 Z, 0부터 9까지 1개 이상
# <re.Match object; span=(0, 9), match='Hello1234'>     # 있으므로 패턴에 매칭

print(re.match('[A-Z0-9]+','hello'))        # 대문자, 숫자는 없고 소문자만 있으므로 
# None                                          # 패턴에 매칭되지 않음



""" 이처럼 숫자, 영문 문자 범위는 a-zA-Z0-9 또는 A-Z0-9와 같이 붙여 쓰면 된다."""


""" 그럼 한글은 어떻게 사용할까? 영문 문자와 방법이 같다. '가-힣'처럼 나올 수 있는 한글 조합을 정해주면
    된다.
    
        * 가- 힣
        
"""


print(re.match('[가-힣]+','홍길동'))    #가 부터 힣 까지 1개 이상 있으므로 패턴에 매칭됨
# <re.Match object; span=(0, 3), match='홍길동'>






# 특정 문자 범위에 포함되지 않는지 판단하기

""" 지금까지 정규표현식으로 특정 문자 범위에 포함되는지 살펴보았다. 그럼 특정 문자 범위에 포함되지 않는지 판단하려면 어떻게 해야 할까?
    다음과 같이 문자(숫자) 범위 앞에 ^을 붙이면 해당 범위를 제외한다.
    
    
        * [^범위]*
        * [^범위]+
        
        
        즉 '[^A-Z]+'는 대문자를 제외한 모든 문자(숫자)가 1개 있는지 판단한다.
"""


print(re.match('[^A-Z]+','Hello'))  # 대문자를 제외
# None                              # 대문자가 있으므로 패턴에 매칭되지 않음

print(re.match('[^A-Z]+','hello'))  # 대문자를 제외. 대문자가 없으므로 패턴에 매칭됨
# <re.Match object; span=(0, 5), match='hello'>




""" 앞에서 특정 문자열로 시작하는지 판단할 때도 ^을 사용했는데 문법이 비슷해서 이 부분은 헷갈리기 쉽다.
    범위를 제외할 때는 '[^A-Z]+'와 같이 [] 안에 넣어주고, 특정 문자 범위로 시작할 때는 '^[A-Z]+'와
    같이 [] 앞에 붙여준다.  그래서 다음과 같이 '^[A-Z]+'는 영문 대문자로 시작하는지 판단한다.
    
    
    * ^[범위]*

    * ^[범위]+
    
    """


print(re.search('^[A-Z]+','Hello'))         # 대문자로 시작하므로 패턴에 매칭됨
# <re.Match object; span=(0, 1), match='H'>


""" 물론 특정 문자(숫자) 범위로 끝나는지 확인할 때는 정규표현식 뒤에 $를 붙이면 된다.

    * [범위]*$
    * [범위]+$
    
    """

