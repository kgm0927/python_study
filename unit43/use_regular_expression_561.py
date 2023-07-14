# 정규 표현식 사용하기


""" 정규표현식(regular expression)은 일정한 규칙(패턴)을 가진 문자열을 표현하는 문자열이다. 복잡한 문자열 속에서
    특정한 규칙으로 된 문자열을 검색한 뒤 추출하거나 바꿀 때 사용한다. 또는, 문자열이 정해진 규칙에 맞는지 판단할 때도 사용한다."""


# judging_the_string ( 문자열 판단하기.)


""" 간단하게 문자열에 특정 문자열이 포함되어 있는지 판단해보겠다. 정규표현식은 re 모듈을 가져와서 사용하여
    match 함수에 정규표현식 패턴과 판단할 문자열을 넣는다(re는 regular expression의 약자).
    
    * re.match('패턴',문자열)

    다음은 'Hello, world!' 문자열에 'Hello'와 'Python'이 있는지 판단한다.    
    """

import re
print(re.match('Hello','Hello, world!'))
# <re.Match object; span=(0, 5), match='Hello'>

print(re.match('Python','Hello, world!'))   # 문자열이 없으므로 아무것도 변환되지 않음
# None



""" 문자열이 있으면 매치(SRE_Match) 객체가 변환되고 없으면 아무것도 반환되지 않는다. 여기서는 'Hello'가 있으므로 match='Hello'와 같이
    패턴에 매칭된 문자열이 표시된다."""

""" 사실 이런 판단은 'Hello, world!'.find('Hello')처럼 문자열 메서드로도 충분히 가능하다."""




# 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단하기


""" 정규표현식은 특정 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단할 수 있다."""

""" 문자열 앞에 ^을 붙이면 문자열이 맨 앞에 오는지 판단하고 문자열 뒤에 $를 붙이면 문자열이 맨 뒤에 오는지
    판단한다(특정 문자열로 끝나는지).
    
    단, 이때는 match 대시 search 함수를 사용해야 한다. match 함수는 문자열 처음부터 매칭되는지 판단하지만,
    search는 문자열 일부분이 매칭되는지 판단한다.

    * re.search('패턴','문자열')
    


    ^ 와 $를 쉽게 설명하면, '^Hello'는 'Hello,world!'가 'Hello'로 시작하는지 판단하고 'world$'는 'Hello,world'가 'world!'로
    끝나는지 판단한다.

    """

print(re.search('^Hello','Hello, world!')) # Hello로 시작하므로 패턴에 매칭됨
# <re.Match object; span=(0, 5), match='Hello'>
print(re.search('world!$','Hello, world!')) # Hello!로 시작하므로 패턴에 매칭됨
# <re.Match object; span=(7, 13), match='world!'>


# 지정된 문자열이 하나라도 포함되는지 판단하기

""" |는 특정 무자열에서 지정된 문자열(문자)이 하나라도 포함되는지 판단한다. 기본 개념은 OR 연산자와 가다.

    * 문자열|문자열                                                 * 문자열|문자열|문자열|문자열
    
   
    
     
      
       
        

    
     
      
       
        
    'hello|world'는 문자열에서 'hello' 또는 'world'가 포함되어 있는지 판단한다.
      """

print(re.match('hello|world', 'hello'))
# <re.Match object; span=(0, 5), match='hello'>