# 메서드 오버라이딩 사용하기

""" 이번에는 파생 클래스에서 기반 클래스의 메서드를 새로 정의하는 메서드오버라이딩에 대해 알아본다.
    다음과 같이 Person의 greeting 메서드가 있는 상태에서 Student에도 greeting 메서드를 만든다."""


class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')


james=Student()
james.greeting()
# 안녕하세요. 저는 파이썬 코딩 도장 학생입니다.




""" james.greeting()처럼 Student의 greeting 메서드를 호출하니 '안녕하세요. 저는 파이썬 코딩 도장 학생입니다.'가
    출력되었다. 
    
    오버라이딩(overriding)은 무시하다, 우선하다 라는 뜻이 있는데 말 그대로 기반 클래스의 메서드를 무시하고 새로운
    메서드를 만든다는 의미이다. 여기서는 Person클래스의 greeting 메서드를 무시하고 Student 클래스에서 새로운 greeting
    메서드를 만들었다.
    
    그럼 메서드 오버라이딩은 왜 사용할까? 보통 프로그램에서 어떤 기능이 같은 메서드 기능으로 계속 사용되어야 할 때 메서드
    오버라이딩을 활용한다. 만약 Student 클래스에서 인사하는 메서드를 greeting2로 만들어야 한다면 모든 소스 코드에선 
    메서드 호출 부분을 greeting2로 수정해야 할 것이다.
    
    다시 Person 클래스의 greeting 메서드와 Student 클래스의 greeting 메서드를 보면 '안녕하세요.'라는 문구가 중복이 된다.
    
    
    이럴 때는 기반 클래스의 메서드를 재활용하면 중복을 줄일 수 있다. 다음과 같이 오버라이딩된 메서드에서 super()로 기반 클래스의
    메서드를 호출해본다."""


class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def greeting(self):
        super().greeting()  # 기반 클래스의 메서드 호출하여 중복을 줄임
        print('저는 파이썬 코딩 도장 학생입니다.')


james=Student()
james.greeting()


""" Student의 greeting에서 super().greeting()으로 Person의 greeting을 호출했다. 즉, 중복되는 기능은 파생 클래스에서 다시 만들지 않고
    기반 클래스의 기능을 사용하면 된다."""