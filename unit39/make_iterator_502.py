# 이터레이터 만들기

""" 이제 __iter__, __next__ 메서드를 구현해서 직접 이터레이터를 만들어보겠다. 간단하게 range(횟수)처럼 동작하는 이터레이터이다.

    class 이터레이터이름:
        def __iter__(self):
            코드
        
        def __next__(self):
            코드
            
"""


class Counter:
    def __init__(self,stop):
        self.current=0          # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop=stop          # 반복을 끝낼 숫자

    def __iter__(self):
        return self             # 현재 인스턴스를 반환
    
    def __next__(self):
        if self.current<self.stop:      # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r=self.current              # 반환할 숫자를 변수에 저장
            self.current +=1            # 현재 숫자를 1 증가시킴
            return r                    # 숫자를 반환
        else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration         # 예외 발생


for i in Counter(3):
    print(i,end=' ')


""" 실행을 해 보면 0 1 2가 나온다. 이렇게 0부터 지정된 숫자 직전까지 반복하는 이터레이터 Counter를 정의했다.

    먼저 클래스로 이터레이터를 작성하려면 __init__ 메서드를 만든다. 여기서는 Counter(3)처럼 반복을 끝낼 숫자를 받았으므로 self.stop에
    stop을 넣어준다. 그리고 반복할 때마다 현재 숫자를 유지해야 하므로 속성 self.current에 0을 넣어준다.
    (0부터 지정된 숫자 직전까지 반복하므로 0을 넣어준다.)
    
    그리고 __iter__ 메서드를 만드는데 여기서는 self만 반환하면 끝이다. 이 객체는, 리스트, 문자열, 딕셔너리, 세트, range처럼 __iter__를 호출해줄
    반복 가능한 객체(iterable)가 없으므로 현재 인스턴스를 반환하면 된다. 즉, 이 객체는 반복 가능한 객체이면서 이터레이터이다.
    
    
    그 다음에 __next__ 메서드를 만든다. __next__에서는 조건에 따라 숫자를 만들어내거나 StopIteration 예외를 만들어 낸다. 현재 숫자 self.current 반복을 
    끝낼 숫자 self.stop 보다 작을 때는 self.current를 1을 증가시키고 현재 숫자를 반환한다. 이때 1 증가한 숫자를 반환하지 않도록 숫자를 증가시키기 전에
    r=self.current처럼 반환할 숫자를 변수에 저장해 놓는다.
    
    그 후 self.current가 self.stop보다 크거나 같아질 때 raise StopIteration으로 예외를 발생시킨다."""






""" 지금까지 간단한 이터레이터를 만들어 보았다. 이터레이터를 마들 때는 __init__ 메서드에서 초깃값, __next__ 메서드에서 조건식과 현재값 부분을 조심해야 한다.
    반복횟수가 달라질 수 있으므로 꼼꼼히 살펴 보아야 한다."""






# 이터레이터 언패킹

""" 참고로 이터레이터는 언패킹(unpacking)이 가능하다. 즉, 다음과 같이 Counter()의 결과를 변수 여러 개에 할당할 수 있다.
    물론 이터레이터가 반복하는 횟수와 변수의 개수는 같아야 한다."""

a,b,c=Counter(3)


print(a,b,c)
# 0 1 2
a,b,c,d,e=Counter(5)

print(a,b,c,d,e)
# 0 1 2 3 4