# 인덱스로 접근할 수 있는 이터레이터 만들기

""" 이제는 __getitem__ 메서드를 구현하여 인덱스로 접근할 수 있는 이터레이터를 만들어보겠다.

    앞에서 만든 Counter 이터레이터를 인덱스로 접근할 수 있도록 다시 만들어보겠다.
    
    class 이터레이터이름:
        def __getitem__(self,인덱스):
            코드"""


class Counter:
    def __init__(self,stop):
        self.stop=stop

    def __getitem__(self,index):
        if index< self.stop:
            return index
        else:
            raise IndexError


print(Counter(3)[0],Counter(3)[1],Counter(3)[2])


for i in Counter(3):
    print(i,end=' ')

# 0 1 2
# 0 1 2


""" Counter(3)[0]을 출력했을 때 0이 나왔다. 마찬가지로 Counter(3)[1]은 1, Counter(3)[2]는 2가지 나왔다. 그리고 for 반복문에 Counter를 사용했을 때도
    1, 2, 3이 나왔다.
     
    소스 코드를 잘 보면 __init__ 메서드와 __getitem__ 메서드만 있는데도 동작이 잘 된다. 클래스에서 __getitem__만 구현해도 이터레이터가 되며 
    __iter__, __next__는 생략해도 된다(초깃값이 없다면 __init__도 생략이 가능).
    
    
    그럼 __init__ 메서드부터 살펴보겠다. 여기서는 Counter(3)처럼 반복을 끝낼 숫자르 받았으므로 self.stop에 stop을 넣어준다. """



""" 이제 클래스에서 __getitem__ 메서드를 구현하면 인덱스로 접근할 수 있는 이터레이터가 된다. 먼저 __getitem__은 매개변수로 인덱스 index를 받는다. 그리고
    지정된 index가 반복을 끝낼 숫자 self.stop보다 작을 때 index를 반환한다. index가 self.stop보다 크거나 같으면 IndexError를 발생시킨다. 즉, Counter(3)
    과 같이 반복을 끝낼 숫자가 3이면 2까지 지정할 수 있다."""


""" 이렇게 하면 Counter(3)[0]처럼 이터레이터를 인덱스로 접근할 수 있다."""


""" 다른 방식으로 __getitem__을 만들 수 있는데 index*10을 반환하게 하여 0,10,20 처럼 10 단위로 숫자를 나오게 할 수 있다."""