# 클래스 속성과 정적, 클래스 메서드 사용하기


""" 이번에는 클래스에 속해 있는 클래스 속성에 대해 알아보겠다. 그리고 인스턴스를 만들지 않고 클래스로 호출하는 정적 메서드와 클래스 메서드도
    사용해보겠다."""



# 클래스 속성과 인스턴스 속성 알아보기

""" 속성에서는 클래스 속성과 인스턴스 속성 두 가지가 있다. __init 메서드에서 만들었던 속성은 인스턴스 속성이다."""


# 클래스 속성 사용하기

""" 클래스 속성을 사용해보겠다. 클래스 속성은 다음과 같이 클래스에 바로 속성을 만든다.

    class 클래스이름:
        속성=값"""




""" 이제 간단하게 사람 클래스에 클래스 속성으로 가방 속성을 넣고 사용해보겠다. 다음과 같이 Person 클래스에
    바로 bag 속성을 넣고, put-bag 메서드를 만든다. 그리고 인스턴스 두 개를 만든 뒤 각각 put_bag 메서드를 사용한다."""


class Person:
    bag=[]


    def put_bag(self,stuff):
        self.bag.append(stuff)


james=Person()
james.put_bag('책')


maria=Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)
# ['책', '열쇠']
# ['책', '열쇠']

""" 여기서 이상한 점은 james와 maria 인스턴스를 만들고 각자 put_bag 메서드로 물건을 넣었는데, james.bag과 maria.bag을 출력해보면
    넣었던 물건이 합쳐져서 나온다. 즉, 클래스 속성은 클래스에 속해 있으며 모든 인스턴스에서 공유한다."""




""" put_bag 메서드에서 클래스 속성 bag에 접근할 때 self를 사용했다. 사실 self는 현재 인스턴스를 뜻하므로 클래스 속성을 지치하기에는
    모호하다."""


""" 그래서 클래스 속성에 접근할 때는 다음과 같이 클래스 이름으로 접근하면 좀 더 코드가 명확해진다."""


class Person:
    bag=[]

    def put_bag(self,stuff):
        Person.bag.append(stuff)    # 클래스 이름으로 클래스 속성에 접근



""" Person.bag 이라고 하니 클래스 Person에 속한 bag 속성이라는 것을 알 수 있다. 마찬가지로 클래스 바깥에서도 다음과 같이 클래스 이름으로
    클래스 속성에 접근하면 된다."""


print(Person.bag)




# 참고: 속성, 메서드 이름을 찾는 순서


""" 파이썬에서는 속성, 메서드 이름을 찾을 때 인스턴스, 클래스 순으로 찾는다. 그래서 인스턴스 속성이 없으면 클래스 속성을 찾게 되므로 james.bag
    , maria.bag도 문제없이 동작한다. 겉보기에는 인스턴스 속성을 사용하는 것 같지만 실제로는 클래스 속성이다. 인스턴스와 클래스에서 __dict__ 속성을
    출력해보면 현재 인스턴스와 클래스의 속성을 딕셔너리로 확인할 수 있다.
    
    
            * 인스턴스.__dict__
            * 클래스.__dict__
    """


print(james.__dict__)
# {}

print(Person.__dict__)
# {'__module__': '__main__', 'bag': [], 'put_bag': <function Person.put_bag at 0x000001F99666CF40>,
#  '__dict__': <attribute '__dict__' of 'Person' objects>, 
# '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}






# 인스턴스 속성 사용하기

""" 만약 속성을 여러 사람이 공유하지 않으려면 어떻게 해야 할까? 그냥 bag을 인스턴스 속성으로 만들면 된다."""



class Person:
    def __init__(self):
        self.bag=[]

    def put_bag(self,stuff):
        self.bag.append(stuff)



james=Person()
james.put_bag('책')


maria=Person()
maria.put_bag('열쇠')

print(james.bag)
# ['책']

print(maria.bag)
# ['열쇠']


""" 즉 인스턴스 속성은 독립되어 있으며 서로 영향을 주지 않는다."""


""" 이제 클래스 속성과 인스턴스 속성의 차이점을 정리해보겠다.

    * 클래스 속성: 모든 인스턴스가 공유, 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
    * 인스턴스 속성: 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 때 사용
"""



# 비공개 클래스 속성 사용하기

""" 클래스 속성도 비공개 속성을 만들 수 있다. 클래스 속성을 만들 때  '__속성'과 같이 __(밑줄 두개)로 시작하면 비공개 속성이 된다. 따라서
    클래스 안에서만 접근할 수 있고, 클래스 바깥에서는 접근할 수 없다.
    
    class 클래스이름:
        __속성=값       # 비공개 클래스 속성
    
    """


""" 즉, 클래스에서 공개하고 싶지 않은 속성이 있으면 비공개 클래스를 사용해야 한다. 예를 들어 기사 케임 캐릭터는 아이템을 최대 10개까지만
    보유할 수 있다고 한다."""


class knight:
    __item_limit=10     # 비공개 클래스 속성

    def print_item_limit(self):
        print(knight.__item_limit)



x=knight()

x.print_item_limit()    # 10

# print(knight.__item_limit)      # 클래스 바깥에서는 접근할 수 없음


""" 실행을 해보면 클래스 Knight의 비공개 클래스 속성 __item_limit는 클래스 안의 print_item_limit 메서드에서만 접근할 수 있고 클래스 바깥에서 접근하면
    에러가 발생한다.
    
    
    이처럼 비공개 클래스 속성은 클래스 바깥으로 드러내고 싶지 않은 값에 사용한다."""






# 참고: 클래스와 메서드의 독스트링 사용하기

""" 함수와 마찬가지로 클래스와 메서드도 독스트링을 할 수 있다. 다음과 같이 클래스와 메서드를 만들 때 :(콜론) 바로 다음 줄에 큰따옴표 3개와 작은 따옴표
    3개를 문자열로 입력하면 된다. 그리고 클래스의 독스트링은 클래스.__doc__ 형식으로 사용하고, 메서드의 독스트링은 클래스.메서드.__doc__ 또는 
    인스턴스.메서드.__doc__ 형식으로 사용한다.""" 

class Person:
    ''' 사람 클래스입니다.'''
    def greeting(self):
        '''인사 메서드입니다.'''
        print('Hello')
    


print(Person.__doc__)           # 사람 클래스입니다.
#  사람 클래스입니다.
print(Person.greeting.__doc__)  # 인사 클래스입니다.
# 인사 메서드입니다.

maria=Person()
print(maria.greeting.__doc__)   # 인사 메서드입니다.
# 인사 메서드입니다.