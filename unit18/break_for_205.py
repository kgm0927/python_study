
"""이번에는 break와 continue를 사용하여 반복문을 제어하는 방법이다.

break는 for와 while 문법에서 제어 흐름을 벗어나기 위해 사용한다. 즉, 루프를 완전히 중단한다. 밑에 있는 것이
continue와 break의 차이이다."""

# break: 제어 흐름 중단
# continue: 제어 흐름 유지, 코드 실행만 건너뜀

# continue와 break에는 :를 붙이지 않는다.


for i in range(10000):  # 0부터 9999까지 반복
    print(i)
    if i==100:  # i가 100일 때
        break   # 반복문을 끝냄. for의 제어 흐름을 벗어남


    