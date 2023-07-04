# 반복문으로 딕셔너리 키-값 쌍을 모두 출력하기

"""키와 값을 모두 출력하려면 어떻게 하면 되겠는가? 이때는 for in 뒤에 딕셔너리를 지정하고 items를 사용해야 한다.



    for 키, 값 in 딕셔너리.items():
        반복할 코드"""



x={'a':10,'b':20,'c':30,'d':40}
for key,value in x.items():
    print(key,value)
# a 10
# b 20
# c 30
# d 40

""" for key,value in x.items(): 는 딕셔너리 x에서 키-값 쌍을 꺼내서 키는 key에 값은 value에 저장하고, 꺼낼 때마다 코드를 반복한다.
따라서 print로 key와 value를 출력하면 키-값 쌍을 모두 출력할 수 있다."""



# 딕셔너리의 키만 출력하기

""" 지금까지 items로 키와 값을 함께 가져왔는데, 키만 가져오거나 값만 가져오면서 반복할 수도 있다.

    items: 키-값 쌍을 모두 가져옴
    keys: 키를 모두 가져옴
    values: 값을 모두 가져옴

"""

x={'a':10,'b':20, 'c':30,'d':40}
for key in x.keys():
    print(key,end=' ')
# a b c d

""" 이는 딕셔너리의 키만 출력된 것이다. 이와 비슷하게 values()를 key() 대신에 쓰면 된다."""