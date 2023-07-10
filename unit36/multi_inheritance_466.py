# 다중 상속 사용하기

""" 다중 상속은 여러 기반 클래스로부터 상속을 받아서 파생 클래스를 만드는 방법이다. 다음과 같이 클래스를 만들 때 ()(괄호)안에
    클래스 이름은 ,(콤마)로 구분해서 넣는다.
    
    
        class 기반클래스이름1:
            코드
        
        class 기반클래스이름2:
            코드
            
        class 기반클래스이름(기반클래스이름1, 기반클래스이름2):
            
            
"""


class Person:
    def greeting(self):
        print('안녕하세요.')


class University:
    def manage_credit(self):
        print('학점 관리')


class Undergraduate(Person, University):
    def study(self):
        print('공부하기')


james=Undergraduate()
james.greeting()        # 안녕하세요: 기반 클래스 Person의 메서드 호출
james.manage_credit()   # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()           # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드


# 안녕하세요.
# 학점 관리
# 공부하기


""" 먼저 기반 클래스 Person과 University를 만들었다. 그 다음에 파생 클래스 Undergraduate를 만들 때 class Undergraduate(Person, University):
    와 같이 괄호 안에 Person과 University를 콤마로 구분해서 넣었다. 이렇게 하면 두 기반 클래스의 기능을 모두 상속받는다."""


""" 즉 다음과 같이 Undergraduate 클래스의 인스턴스로 Person의 greeting과 University의 manage_credit을 호출할 수 있다."""


# 다이아몬드 상속


""" 조금 복잡한 클래스 상속을 해보겠다. 여기서는 편의상 클래스 이름을 A, B, C, D로 만들겠다."""


class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')


class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B,C):
    pass

x=D()
x.greeting()

# 안녕하세요. B입니다.


""" 기반 클래스 A가 있고, B,C는 A를 상속받는다. 그리고 다시 D는 B,C를 상속받는다. 이 관계를 그림으로
    나타내면 다음과 같은 모양이 된다 클래스 같의 관계가 다이아몬드 같이 생긴 것이다."""


""" 여기서는 클래스 A를 상속받아서, B,C를 만들고, 클래스 B와 C를 상속받아서 D를 만들었다. 그리고 A, B, C 모두 greeting이라는 같은 메서드를 가지고 있다면
    D는 어떤 클래스의 메서드를 호출해야 할까? 조금 애매하다."""

""" 프로그래밍에서는 이렇게 명확하지 않고 애매한 상태를 좋아하지 않는다. 프로그램이 어떨 때는 A의 메서드를 호출하고, 또 어떨때는 B 또는 C의 메서드를 호출한다면
    큰 문제가 생긴다. 그래서 다이아몬드 상속은 문제가 많다고 해서 죽음의 다이아몬드라고 한다."""





# 메서드 탐색 순서 확인하기

""" 많은 프로그래밍 언어들이 다이아몬드 상속에 대한 해결책을 제시하고 있는데 파이썬에서는 메서드 탐색 순서(Method Resolution Order, MRO)를 따른다.
    다음과 같이 클래스 D에 메서드 mro를 사용해보면 메서드 탐색 순서가 나온다(클래스.__mro__ 형식도 같은 내용).
    
    
    * 클래스.mro()
    
    """

print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


""" MRO에 따르면 D의 메서드 호출 순서는 자기 자신 D, 그다음이 B이다. 따라서 D로 인스턴스를 만들고 greeting을 호출하면 B의 greeting이 호출이 된다
    (D는 greeting 메서드가 없으므로)."""


""" 파이썬은 다중 상속을 한다면 class D(B,C):의 클래스 목록 중 왼쪽에서 오른쪽 순서로 메서드를 찾는다. 그러므로 같은 메서드가 있다면 B가 우선한다.
    만약 상속관계가 복잡하게 얽혀 있다면 MRO를 살펴보는 것이 편리하다. """



# 참고: object 클래스

""" 파이썬에서 object는 모든 클래스의 조상이다. 그래서 int의 MRO를 출력해보면 int 자기 자신과 object가 출력이 된다."""

print(int.mro())
# [<class 'int'>, <class 'object'>]


""" 파이썬 3에서 모든 클래스는 object 클래스를 상속받으므로 기본적으로 object를 생략한다. 다음과 같이 클래스를 정의하면"""
class X:
    pass

""" 괄호 안에 object를 넣은 것과 같다."""

class X(object):
    pass


""" 파이썬 2에서는 class X:가 old-style 클래스를 만들고, class X(object): 가 new-style 클래스를 만들었다. 그래서 파이썬2 에서는 
    이 둘을 구분해서 사용해야 했지만, 파이썬 3에서는 old-style 클래스가 삭제되었고 class X:와 class X(object): 모두 new-style 클래스를 만든다.
    따라서 파이썬 3에서는 괄호 안에 object를 넣어도 되고 넣지 않아도 된다."""


# 추상 클래스 사용하기

""" 파이썬은 추상 클래스(abstract class)라는 기능을 제공한다. 추상 클래스는 메서드의 목록만 가진 클래스이며 상속받는 클래스에서 메서드 구현을 강제하기
    위해 사용한다.
    
    먼저 추상 클래스를 만들려면 import로 abc 모듈을 가져와야 한다. (abc 는 abstract base class의 약자이다) 그리고 클래스의 ()(괄호) 안에 metaclass=ABCMeta
    를 지정하고, 메서드를 만들 때 위에 @abstractmethod를 붙여서 추상 메서드로 지정한다.
    
    
    from abc import *

    class 추상클래스이름(metaclass=ABCMeta):
        @abstractmethod
        def 메서드이름(self):
            코드
    """



""" 여기서는 from abc import *로 abc 모듈의 모든 클래스와 메서드를 가져왔다. 만약 import abc로 모듈을 가져왔다면 abc.ABCMeta, @abc.abstractmethod로
    사용해야 한다. """


""" 그럼 학생 추상 클래스 StudentBase를 만들고 이 추상 클래스를 상속받아 학생 클래스 Student를 만들어보겠다."""



""" 여기서 주의해야 할 점은 추상 클래스 StudentBase에서는 추상 메서드로 study와 go_to_school을 정의한다. 하지만 StudentBase를 상속받은 
    Student에서는 Study 메서드만 구현하고, go_to_school 메서드는 구현하지 않았다면 에러가 발생한다."""









from abc import*


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass


    @abstractmethod
    def go_to_school(self):
        pass



class Student(StudentBase):
    def study(self):
        print('공부하기')
    
    def go_to_school(self):
        print("학교가기")


james=Student()
james.study()
james.go_to_school()
# 공부하기
# 학교가기

""" StudentBase는 학생이 반드시 해야 하는 일들을 추상 메서드로 만들었다. 그리고 Student에는 추상 클래스 StudentBase의 추상 메서드를 구현하여
    학생 클래스를 작성한다. 이처럼 추상 클래스는 파생 클래스가 반드시 구현해야 하는 메서드를 정해줄 수 있다.
    
    참고로 추상 클래스는 추상 메서드를 모두 구현했는지 확인하는 시점은 파생 클래스가 인스턴스를 만들 때이다. 따라서 james=Student()에서 확인한다
    (구현하지 않았다면 TypeError 발생)."""



# 추상 메서드를 빈 메서드로 만드는 이유

""" 한 가지 중요한 점은 추상 클래스는 인스턴스로 만들 수가 없다는 것이다. 다음과 같이 추상 클래스 StudentBase로 인스턴스를 만들면 에러가 발생한다."""


""" 그래서 지금까지 추상 메서드를 만들 때 pass만 넣어서 빈 메서드로 만든 것이다. 왜냐하면 추상 클래스는 인스턴스를 만들 수 없으니 호출할 일이 없다."""


""" 정리하자면 추상 클래스는 인스턴스로 만들 때는 사용하지 않으며 오로지 상속에만 사용한다. 그리고 파생 클래스에서 구현해야 할 메서드를 줄 때 사용한다."""


