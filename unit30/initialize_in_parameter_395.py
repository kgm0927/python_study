# 매개변수에 초깃값 지정하기

""" 인수를 생략할 수 있는가? 이때는 함수의 매개변수에 초깃값을 지정하면 된다. 초깃값은 다음과 같이 함수를 만들 때 '매개변수=값' 형식으로
    저장한다.

    def 함수 이름(매개변수=값):    
        코드
    
    """




""" 매개변수의 초깃값은 주로 사용하는 값이 있으면서 가끔 다른 값을 사용해야 할때 활용한다. 대표적으로 print 함수인데, print 하뭇의 초깃값이 ' '(공백)으로 
    지정되어 있으며 대부분 그대로 사용하고 가끔 sep에 다른 값을 넣어서 쓴다."""


""" 이제 personal_info 함수에서 매개변수 address의 초깃값이 '비공개'로 지정해 보겠다."""

def person_info(name,age,address='비공개'):
    print('이름: ',name)
    print('나이: ',age)
    print('주소: ',address)


"""address는 초깃값이 있으므로 personal_info()는 다음과 같이 address 부분을 비워두고 호출할 수 있다."""

person_info('홍길동',30)

# 이름:  홍길동
# 나이:  30
# 주소:  비공개



""" 매개변수에 초깃값이 지정되어 있더라도 값을 넣으면 해당 값이 전달이 된다."""

person_info('홍길동',30,'서울시 용산구 이촌동')
# 이름:  홍길동
# 나이:  30
# 주소:  서울시 용산구 이촌동



# 초깃값이 지정된 매개변수의 위치

""" 매개변수의 초깃값을 지정할 때 한 가지 주의해야 할 점이 있다. 초깃값이 지정된 매개변수 다음에는 초깃값이 없는 매개변수가 올 수 없다."""


""" 잘못된 표기 :def person_info(name,address='비공개',age):
 """


""" 잘못된 방법이므로 매개변수는 뒤쪽에 몰아주어야 한다."""



