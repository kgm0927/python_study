"""while 문은 초기식부터 시작하여 조건식을 판별한다.
이때 조건식이 참이면 반복할 코드와 변화식을 함께 수행한다.

그리고 다시 조건식을 판별하여 참 이면 코드를 계속 반복하고,
거짓이면 반복문을 끝낸 뒤 다음 코드를 실행한다."""

import time

i=0
print(i)

while i<100:
    print("Hello, world!")
    i+=1
    time.sleep(1)



    
    