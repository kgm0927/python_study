# 상속관계와 포함 관계 알아보기


""" 지금까지 기반 클래스를 상속하여 새로운 클래스를 만들어 보았다. 그런데 클래스 상속은 정확히 어디에 사용해야 할까?"""


# 상속관계


""" 앞에서 만든 Student 클래스는 Person 클래스를 상속받아 만들었다."""

class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def study(self):
        print('공부하기')


""" 상속은 명확하게 같은 종류이며 동등한 관계일 때 사용한다. 즉, '학생은 사람이다.'라고 했을 때 말일 되면 동등한 관계이다. 그래서
    상속 관계를 영어로 is-a 관계라고 부른다."""


# 포함관계

""" 만약 학생 클래스가 아니라 살마 목록을 관리하는 클래스를 만든다면 어떻게 해야 할까? 다음과 같이 리스트 속성에 Person 인스턴스를 넣어서 관리
    하면 된다."""


class Person:
    def greeting(self):
        print('안녕하세요.')

class PersonList:
    def __init__(self) -> None:
        self.Person_list=[]         # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self,person): # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.Person_list.append(person)



""" 여기서는 상속을 하지 않고 속성에 인스턴스를 넣어 관리하므로 PersonList가 Person을 포함하고 있다. 이러면 사람 목록 PersonList와 사람 Person은
    동등한 관계가 아니라 포함 관계이다. 즉, '사람 목록은 사람은 가지고 있다.'라고 말할 수 있다. 그래서 포함 관계를 영어로 has-a 관계라고 부른다.
    (PersonList has a Person).
    
    
    정리하자면 같은 종류에 동등한 관계일 때는 상속을 사용하고 그 이외에는 속성에 인스턴스를 넣는 포함 방식을 쓰면 된다."""




# 기반 클래스의 속성 사용하기


""" 이번에는 기반 클래스에 들어있는 인스턴스 속성을 사용해 보겠다. 다음과 같이 Person 클래스의 hello 속성이 있고 Person 클래스를 상속받아 Student 클래스를
    만든다. 그다음에 Student로 인스턴스를 만들고 hello 속성에 접근해본다."""

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello='안녕하세요.'


class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school='파이썬 코딩 도장'




# james=Student()
# print(james.school)
# print(james.hello)


""" 실행을 해 보면 에러가 발생한다. 왜냐하면 기반 클래스의 Person의 __init__ 메서드가 호출되지 않았기 때문이다. 실행 결과를 보면
    'Student __init__'만 출력되었다.
    
    즉, Person의 __init__ 메서드가 호출되지 않으면 self.hello='안녕하세요.'도 실행되지 않아서 속성이 만들어지지 않는다."""





# super()로 기반 클래스 초기화하기

""" 이때는 super()를 사용해서 기반 클래스의  __init__ 메서드를 호출해준다. 다음과 같이 super() 뒤에 .(점)을 붙여서 메서드를 호출하는 방식이다.
        
        
        * super().메서드()"""



class Person:
    def __init__(self):
        print('Person __init__')
        self.hello='안녕하세요.'

class Student(Person):
    def __init__(self):
        print('student __init__')
        super().__init__()              # super()로 기반 클래스의 __init__ 메서드 호출
        self.school='파이썬 코딩 도장'


james=Student()
print(james.school)
print(james.hello)


# student __init__
# Person __init__
# 파이썬 코딩 도장
# 안녕하세요.



""" 실행을 해 보면 기반 클래스 Person의 속성인 hello가 잘 출력이 된다. super().__init__()과 같이 기반 클래스의 Person의 __init__() 메서드를
    출력해주면 기반 클래스가 초기화되어 속성이 만들어진다. 실행 결과를 보면 'Student __init__'과 'Person __init__'양쪽 다 출력이 된다."""





# 기반 클래스를 초기화하지 않아도 되는 경유

""" 만약 파생 클래스에서 __init__ 메서드를 생략한다면 기반 클래스의 __init__이 자동으로 호출되므로 super()는 사용하지 않아도 된다."""



class Person:
    def __init__(self):
        print('Person __init__')
        self.hello='안녕하세요.'


class Student(Person):
    pass

james=Student()
print(james.hello)

# Person __init__
# 안녕하세요.



""" 이처럼 파생 클래스에 __init__ 메서드가 없다면 기반 클래스의 __init__이 자동으로 호출되므로 기반 클래스의 속성을 사용할 수 있다."""





# 참고: 좀 더 명확하게 super 사용하기

""" super는 다음과 같이 파생 클래스와 self를 넣어서 현재 클래스가 어떤 클래스인지 명확하게 표시하는 방법도 있다. 물론 super()와 기능은 같다.

    * super(파생클래스,self).메서드
    
"""

class Student(Person):
    def __init__(self):

        print('Student __init__')
        super(Student,self).__init__()  # super(파생클래스,self)로 기반 클래스의 메서드 호출
        self.school='파이썬 코딩 도장'



