
# split으로 결과를 매번 int로 변환을 하려고 하면 귀찮은 경우가 많다. 이때는 map을 함께 사용하면 된다.
# map에 int와 input().split()를 넣으면 split의 결과를 모두 int로 변환해준다. 
# (실수로 변환할 때에는 int 대신 float를 넣는다.)

# var1, var2=map(int, input().split())
# var1, var2=map(int,input().split('기준문자열'))
# var1, var2=map(int, input('문자열').split())
# var1, var2=map(int, input('문자열').split('기준문자열'))


a,b=map(int, input('숫자 두 개를 입력하세요: ').split())

print(a+b)


# split(', ')과 같이 분리할 기준 문자열을 콤마로 지정하였으므로 '10, 20'에서 10은 a,
# 20은 b에 저장된다. 