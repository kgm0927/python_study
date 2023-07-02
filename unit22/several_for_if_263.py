"""리스트 표현식은 for와 if를 여러 번 사용할 수 있다.

[식 for 변수1 in 리스트1 if 조건식1
    for 변수2 in 리스트2 if 조건식2
    ...
    for 변수n in 리스트2 if 조건식n]
    
    
list(식 for 변수1 in 리스트1 if 조건식1
    for 변수2 in 리스트2 if 조건식2
    ...
    for 변수n in 리스트2 if 조건식n)"""




""" 다음은 2단부터 9단까지 구구단을 생성한다."""
a=[i*j for j in range(2,10) for i in range(1,10)]
print(a)
