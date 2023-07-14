# 매개변수와 반환값을 처리하는 데코레이터 만들기


""" 지금까지 매개변수와 반환값이 없는 함수의 데코레이터를 만들었다. 이번에는 매개변수와 반환값을 처리하는 데코레이터는 어떻게 만드는지
    알아보겠다."""


def trace(func):                                                 # 호출할 함수를 매개변수로 받음
    def wrapper(a,b):                                           # 호출함 함수 add(a,b)의 매개변수와 똑같이 지정
        r=func(a,b)                                             # func에 매개변수 a,b를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(a={1}, b={2})-> {3}'.format(func.__name__,a,b,r))
                                                                 # 매개변수에 반환값 지정

        return r                                                # func의 반환값을 반환
    return wrapper                                              # wrapper 함수 반환



@ trace                                   # @데코레이터
def add(a,b):                               # 매개변수는 2개
    return a+b                              # 매개변수 두 개를 더해서 반환

print(add(10,20))

# add(a=10, b=20)-> 30
# 30



""" add 함수를 호출했을 때 데코레이터를 통해서 매개변수와 반환값이 출력되었다. 매개변수와 반환값을 처리하는 데코레이터를 통해서
    매개변수와 반환값이 출력되었다. 매개변수와 반환값을 처리하는 데코레이터를 만들 때는 먼저 안쪽 wrapper함수의 매개변수를 호출할 함수
    add(a,b)의 매개변수와 똑같이 만들어준다.
    
    def trace(func):                                              
        def wrapper(a,b): 
    
    """


""" wrapper 함수 안에서는 func를 호출하고 반환값을 변수에 저장한다. 그 다음에 print로 매개변수와 반환값을 출력한다. 이때 func에는 매개변수
    a와 b를 그대로 넣어준다. 또한, add 함수는 두 수를 더하여 반환해야 하므로 func의 반환값을 return으로 반환해준다.
    
    
    
    def trace(func):                                                 # 호출할 함수를 매개변수로 받음
    def wrapper(a,b):                                           # 호출함 함수 add(a,b)의 매개변수와 똑같이 지정
        r=func(a,b)                                             # func에 매개변수 a,b를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(a={1}, b={2})-> {3}'.format(func.__name__,a,b,r))
                                                                 # 매개변수에 반환값 지정

        return r                                                # func의 반환값을 반환
    return wrapper  """



""" 만약 wrapper 함수에서 func의 반환값을 반환하지 않으면 add 함수를 호출해도 반환하지 않으므로 주의해야 한다. 참고로 wrapper 함수에서
    func의 반환값을 출력할 필요가 없다면, return func(a,b)처럼 func를 호출하여 바로 반환해도 된다."""


""" 데코레이터를 사용할 때는 @으로 함수 위에 지정해주면 된다. 또한. @으로 데코레이터를 사용했으므로 add 함수는 그대로 호출해 준다.

"""










# 가변 인수 함수 데코레이터


""" def add(a,b):는 매개변수 개수가 고정된 함수이다. 그러면 매개변수(인수)가 고정되지 않는 함수는 어떻게 처리하겠는가?
    이때는 wrapper 함수를 가변 인수 함수로 만들면 된다."""


def trace(func):                                        # 호출할 함수를 매개변수로 받음
    def wrapper(*args,**kwargs):                        # 가변 인수 함수를 만듦
        r=func(*args,**kwargs)                          # func에 args, kwargs를 언패킹하여 넣어줌
        print('{0}(args={1},kwargs={2})-> {3}'.format(func.__name__,args,kwargs,r))
                                                        # 매개변수와 반환값 출력
        return r                                        # func의 반환값을 반환
    return wrapper                                      # wrapper 함수 반환



@ trace
def get_max(*args):
    return max(args)


@ trace
def get_min(**kwargs):
    return min(kwargs.values())



print(get_max(10,20))
print(get_min(x=10,y=20,z=30))

# get_max(args=(10, 20),kwargs={})-> 20
# 20
# get_min(args=(),kwargs={'x': 10, 'y': 20, 'z': 30})-> 10
# 10
#
#
#



""" get_max 함수와 get_min 함수는 가변 인수 함수이다. 따라서 데코레이터도 가변 인수 함수로 만들어준다.
    이때 위치 인수와 키워드 인수를 모두 받을 수 있도록 *args 와 **kwargs를 지정한다."""



""" wrapper 함수 안에서는 func를 호출해주는데 args 튜플이고, kwargs는 딕셔너리이므로 func에 넣을 때는
    언패킹하여 넣어준다. 그리고 print로 매개변수와 반환값을 출력한다."""



""" 이렇게 만든 데코레이터 trace는 위치 인수와 키워드 인수를 모두 처리할 수 있다. 따라서 가변 함수뿐만 아니라 일반적인 함수에도 사용이 가능하다."""





# 참고 메서드에 데코레이터 사용하기

""" 클래스를 만들면서 메서드에 데코레이터를 사용할 때는 self를 주의해야 한다. 인스턴스 메서드는 항상 self를 받으므로 데코레이터를 만들 때도
    wrapper 함수의 첫 번째 매개변수는 self로 지정해야 한다(클래스 메서드는 cls). 마찬가지로 func를 호출할 때도 self와 매개변수를 그대로 넣어야 한다. """

def trace(func):
    def wrapper(self,a,b):  # 호출할 함수가 인스턴스 메서드므로
                            # 첫번째 매개변수는 self로 지정
        r=func(self,a,b)    # self와 매개변수를 그대로 넣어줌
        print('{0}(a={1}, b={2}->{3})'.format(func.__name__,a,b,r))
                            # 매개변수와 반환값 출력
        return r            # func의 반환값을 반환
    return wrapper

class Calc:
    @trace
    def add(self,a,b):      # add는 인스턴스 메서드
        return a+b
    

c=Calc()


print(c.add(10,20))


# add(a=10, b=20->30)
# 30