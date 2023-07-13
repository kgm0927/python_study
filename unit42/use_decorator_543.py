# 데코레이터 사용하기

""" 파이썬은 데코레이터(decorator)라는 기능을 사용한다. 데코레이터는 장식이다. """

""" 지금까지 클래스에서 메서드를 만들 때 @staticmethod, @classmethod, @abstractmethod 등을 붙였는데, 이렇게
    @로 시작하는 것들이 데코레이터이다. 즉, 함수(메서드)를 장식한다고 해서 이런 이름이 붙였다."""

class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)


""" 참고로 데코레이터는 장식자라고도 한다. 이 책에서는 데코레이터를 사용하겠다."""
    