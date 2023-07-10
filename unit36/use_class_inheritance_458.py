# 클래스 상속 사용하기

""" 상속은 무언가를 물려받는다는 뜻이다. 그래서 클래스 상속은 물려받은 기능을 유지한 채로 다른 기능을 추가할 때 사용하는 기능이다.
    여기서 기능을 물려주는 클래스를 기반 클래스(base class), 상속을 받아 새롭게 만드는 클래스를 파생 클래스(derived class)라고 한다."""


# 사람 클래스로 학생 클래스 만들기

""" 클래스 상속은 다음과 같이 클래스를 만들 때 ()(괄호)를 붙이고 안에 기반 클래스 이름을 넣는다.


    class 기반클래스이름:
        코드

    class 파생클래스이름(기반클래스 이름):
        코드


    그럼 간단하게 사람 클래스를 만들고 사람 클래스를 상속받아 학생 클래스를 만들어보겠다.

"""
class Person:
    def greeting(self):
        print('안녕하세요.')

    
class Student(Person):
    def study(self):
        print('공부하기')

james=Student()
james.greeting()    # 안녕하세요: 기반 클래스 Person의 매서드 호출
james.study()       # 공부하기: 파생 클래스 Student에 추가한 study 메서드



""" Student 클래스를 만들 때 class Student(Person): 과 같이 ()(괄호) 안에 기반 클래스인
    Person 클래스를 넣었다. 이렇게 하면 Person 클래스의 기능을 물려받은 Student클래스가 된다.
    
    Student 클래스에는 greeting 메서드가 없지만 Person 클래스를 상속받았으므로 greeting 메서드를 호출할
    수 있다."""








""" 이처럼 클래스 상속은 기반 클래스의 기능을 유지하면서 새로운 기능을 추가할 수 있다. 특히 클래스 상속은 연관되면서
    동등한 기능일 때 사용한다. 즉, 학생은 사람이므로 연관된 개념이고, 학생은 사람에서 역할만 확장되었을 뿐 동등한 개념이다."""


# 참고: 상속 관계 확인하기

""" 클래스의 상속관계를 확인하고 싶다면 issubclass 함수를 사용한다. 즉, 클래스가 기반 클래스의 파생 클래스인지 확인한다. 기반 클래스의 파생
    클래스가 맞으면 True, 아니면 False를 반환한다.
    
    
    issubclass(파생클래스, 기반클래스)
    
    """


class Person:
    pass

class Student(Person):
    pass


print(issubclass(Student, Person))
# True