
# 지금까지는 한 번에 하나의 값만 입력받았다. 그럼 input 한 번에 값을 여러 개 입력받으려면 어떻게 해야 할 까?
# 이때는 input에서 split을 사용한 변수 여러 개에 저장해주면 된다.

# var1, var2= input().split()
# var1, var2= input().split('기준문자열')
# var1, var2= input('문자열').split()
# var1, var2= input('문자열').split('기준문자열')

a,b =input('문자열 2 개를 입력하세요: ').split()

print(a)
print(b)

# 결과 :
#문자열 2 개를 입력하세요: Hello python
# Hello
# python
#